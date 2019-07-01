# coding: utf8
# Adapted from https://gist.github.com/jbeezley/3442777 for kmz files handling

import xarray as xr
import numpy as np
import regionmask
import os
import sys
from xml.dom.minidom import parseString
from zipfile import ZipFile
from io import StringIO
from distutils.util import strtobool
import shapely

try:
  basestring
except NameError:
  basestring = str

regions_dict = dict()
list_abbrevs=[]

def clean():
    """
    Cleans everything to start a new definition of regions
    """
    regions_dict = dict()
    list_abbrevs=[]

def define_config(fmask,lon_name,lat_name,mask_name='tmask'):
    """
    Loads information about the configuration you want to use
    input :
        fmask     : name of the mesh_mask file of the configuration
        lon_name  : name of the longitude variable
        lat_name  : name of the latitude variable
        mask_name : name of the mask variable. Default is 'tmask'. If set to None: no land-sea mask will be used.
    """
    global longitude, latitude, mask_data
    longitude = xr.open_dataset(fmask)[lon_name]
    latitude  = xr.open_dataset(fmask)[lat_name]
    if mask_name:
        mask_data = xr.open_dataset(fmask)[mask_name].isel(t=0,z=0)
    else:
        mask_data = xr.DataArray(np.ones(longitude.shape),dims=('y','x'))

def create_region(name,abbrev,limits,wrap_lon=False):
    """
    Creates a region mask and stores it into regions_dict dictionnary
    """
    print('Creating region %s' % name)
    #Dealing with the case of attempt to define two times the same region
    if name in regions_dict.keys():
        choice=None
        while not choice:
            choice=input('!!! region %s already defined, do you want to create it anyway ? (y/n)' % name).lower()
            if choice=='y':
                choice=True
                name=_update_names(name)
            elif choice=='n':
                choice=True
                print('ok, this region will not be created')
                return None
            else:            
                sys.stdout.write('Please respond with \'y\' or \'n\'.\n')
                choice=None
    abbrev=_update_abbrevs(abbrev)
    short_name = 'tmask'+abbrev
    region      = regionmask.Regions_cls(short_name, [0], [name], [abbrev], [limits])
    region_mask = region.mask(longitude,latitude,wrap_lon=wrap_lon)
    region_mask = (mask_data * xr.where(region_mask,0,1)).astype('int8').rename(short_name)
    regions_dict[name]=(region_mask,limits)

def _openKMZ(filename):
    zip=ZipFile(filename)
    for z in zip.filelist:
        if z.filename[-4:] == '.kml':
            fstring=zip.read(z)
            break
    else:
        raise Exception("Could not find kml file in %s" % filename)
    return fstring

def _openKML(filename):
    try:
        fstring=_openKMZ(filename)
    except Exception:
        fstring=open(filename,'r').read()
    return parseString(fstring)

def _readPolygon(filename):
    def _parseData(d):
        dlines=d.split()
        poly=[]
        for l in dlines:
            l=l.strip()
            if l:
                point=[]
                for x in l.split(','):
                    point.append(float(x))
                poly.append(point[:2])
        return poly

    xml=_openKML(filename)
    nodes=xml.getElementsByTagName('Placemark')
    desc={}
    for n in nodes:
        names=n.getElementsByTagName('name')
        try:
            desc['name']=names[0].childNodes[0].data.strip()
        except Exception:
            pass

        descriptions=n.getElementsByTagName('description')
        try:
            desc['description']=names[0].childNodes[0].data.strip()
        except Exception:
            pass

        polys=n.getElementsByTagName('Polygon')
        for poly in polys:
            invalid=False
            c=n.getElementsByTagName('coordinates')
            if len(c) != 1:
                print('invalid polygon found')
                continue
            if not invalid:
                c=c[0]
                d=c.childNodes[0].data.strip()
                data=_parseData(d)
                yield (data,desc)


def _writePolygon(p,fname):
    if isinstance(fname,basestring):
        f=open(fname,'w')
    else:
        f=fname
    for i in p:
        f.write('%.10f,%.10f,0.\n' % (i[0],i[1]))
##        f.write('%19.16f,%19.16f,0.\n' % (i[0],i[1]))
    f.flush()

def get_list_regions():
    """
    Simply prints the list of regions defined so far, 
    whether via import an kmz file or via the create_region function
    """
    print('List of regions defined so far :')
    for key in regions_dict: print(key)

def get_polygon(region):
    """
    returns the polygon associated with the region requested
    input:
        region: name of the region requested
    """
    try:
        return regions_dict[region][1]
    except:
        print('This region is not defined, pick one region defined in the list below')
        get_list_regions()

def update_region(region,polygon):
    """
    Associates the polygon to the region and updates the mask 
    input:
        region: name of the region to be updated with the new polygon
        polygon: polygone, defined as a list of points on the format :[[x1,y1],...[xn,yn],[x1,y1]]
    """
    # First update the polygon
    regions_dict[region]=(regions_dict[region][0],polygon)
    # Then update the mask
    wrap_lon=False
    for point in polygon:
        if (point[0]>180):
           wrap_lon=True
    create_region(region,regions_dict[region][0].name[5:],polygon,wrap_lon)

def _update_abbrevs(abbrev):
    while abbrev in list_abbrevs:
        abbrev=input(abbrev+' short name is already used for another region, please provide a new one : ')
    list_abbrevs.append(abbrev)
    return abbrev

def _update_names(name):
    while name in regions_dict.keys():
        name=input(name+' region is already defined, please provide a new name for the region : ')
    return name

def create_regions_from_kmz(kmz_file='regions.kmz',set_abbrevs=True,append=True):
    """
    Reads the kmz file and all the Polygons defined inside. Adds them to regions_dict dictionary
    input:
        kmz_file: name of the kmz file
        set_abbrevs: if True, user will be asked to give a short name for each region
                     if False, short name is set to the first 3 letters of the name of the region
        append: if True, adds the new regions to regions_dict, else, it deletes all regions defined previously 
    """
    if ~append:
        regions_dict=dict()
        list_abbrevs=[]
    if ~set_abbrevs:
        print('Name of masks will be defined automaticaly using the first 3 letters of each region')
    i=0
    for p in _readPolygon(kmz_file):
        p,desc=p
        wrap_lon=False
        for point in p:
            if (point[0]>180):
                wrap_lon=True
        if set_abbrevs:
            abbrev=input('Set a short name for mask '+desc['name']+' : ')
        else:
            abbrev=desc['name'][0:3]
        create_region(desc['name'],abbrev,p,wrap_lon)
        i=i+1

def create_nc(nc_file='regions.nc'):
    """
    Merges all the dataarrays in 'regions_dict' into a single netcdf file
    input:
        nc_file : name of the output netcdf file. If file exists, will append the file, else will create it.
    """
    try:
        ds_regions = xr.open_dataset(nc_file)
        print('File '+nc_file+' exists, please change the name !')
        sys.exit(1)
    except FileNotFoundError:
        print("Creating file "+nc_file)
        ds_out = xr.Dataset()

    for region in regions_dict.keys():
        ds_out = xr.merge((ds_out,regions_dict[region][0]))
    ds_out.rename({'lon':'nav_lon','lat':'nav_lat'}).to_netcdf(nc_file)

def create_kmz(kmz_file='regions.kmz'):
    """
    Merges all the dataarrays in 'regions_dict' into a single kml file
    input :
        kml_file : name of the output kml file. If file exists, will append the file, else will create it.
    """
    kmlstr=\
    '''<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom">
<Document>
    <name>%s</name>
      <open>1</open>
      %s
</Document>
</kml>'''

    polystr=\
    '''     <Placemark>
         <name>%s</name>
         <Polygon>
           <altitudeMode>clampedToGround</altitudeMode>
           <outerBoundaryIs>
           <LinearRing>
             <coordinates>
             %s
             </coordinates>
           </LinearRing>
           </outerBoundaryIs>
         </Polygon>
       </Placemark>'''

    multipolystr=\
    '''     <Placemark>
         <name>%s</name>
         <Polygon>
           <altitudeMode>clampedToGround</altitudeMode>
           <outerBoundaryIs>
           <LinearRing>
             <coordinates>
             %s
             </coordinates>
           </LinearRing>
           </outerBoundaryIs>
         </Polygon>
       </Placemark>'''



    strs=[]
    i=0
    for region in regions_dict:
        i=i+1
        f=StringIO()
        if ((isinstance(regions_dict[region][1],shapely.geometry.multipolygon.MultiPolygon)) & (len(list(regions_dict[region][1]))>1)):
            print('This is a multipolygon: we do not deal with that. Sorry but region %s will not be written into the kmz file' % region)
        else:
            if ((isinstance(regions_dict[region][1],shapely.geometry.multipolygon.MultiPolygon)) & (len(list(regions_dict[region][1]))==1)):
                _writePolygon(list(map(list, zip(*regions_dict[region][1][0].exterior.coords.xy))),f)
            elif (isinstance(regions_dict[region][1],shapely.geometry.polygon.Polygon)):
                _writePolygon(list(map(list, zip(*regions_dict[region][1].exterior.coords.xy))),f)
            else:
                _writePolygon(regions_dict[region][1],f)
            strs.append(polystr % (region,f.getvalue()))
    s='\n'.join(strs)
    s=kmlstr % (kmz_file,s)
    kml_file=kmz_file[:-3]+'kml'
    open(kml_file,'w').write(s)
    zf=ZipFile(kmz_file,'w')
    zf.write(kml_file)
    zf.close()


def create_nc_from_kmz(kmz_file='regions.kmz',nc_file='regions.nc',set_abbrevs=False,append=False):
    """
    Creates a netcdf file with all the regions defined in a kmz file.
    Simply successive calls to create_region_from_kmz and create_nc functions
    input  : 
        kmz_file : name of the kmz file, by default regions.kmz
    output : 
        nc_file  : name of the netcdf file, by default regions.nc
    """
    regions_dict=dict()
    list_abbrevs=[]
    create_regions_from_kmz(kmz_file,set_abbrevs,append)
    create_nc(nc_file)


def plot_region(region):
    """
    Creates a simple plot of the mask
    """
    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs
    import cartopy.feature as cfea

    fig = plt.figure(figsize=(12,6))
    ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
    mapa = regions_dict[region][0].plot(x='lon',y='lat',ax=ax,transform=ccrs.PlateCarree(),add_colorbar=False)
    ax.set_title('EC-Earth3.2 - '+regions_dict[region][0].name);ax.coastlines(resolution='50m');ax.add_feature(cfea.LAND, zorder=100);
    gl=ax.gridlines(draw_labels=True);gl.xlabels_top = False;gl.ylabels_right = False;
    plt.savefig(regions_dict[region][0].name+'.png')
    plt.close()
 
