# -*- coding: utf-8 -*-
import create_regions as cr
import cartopy.io.shapereader as shpreader

#user defined configuration
###########################
mask_file = "/esarchive/autosubmit/con_files/mesh_mask_nemo.N3.6_O25L75.nc"
#TA mask_file = "/esarchive/autosubmit/con_files/mesh_mask_nemo.N3.6_O1L75.nc"
#TA mask_file = "/Users/arsouze/Documents/Files/NEMO/mesh_mask_nemo.N3.6_O1L75.nc"
lon_name  = "nav_lon"
lat_name  = "nav_lat"
mask_name = "tmask"

cr.define_config(mask_file,lon_name,lat_name,mask_name)

# Define oceanic regions from Natural_Earth dtb
shpfilename = shpreader.natural_earth(resolution='10m',category='physical',name='geography_marine_polys')
reader = shpreader.Reader(shpfilename)
cpt=0  # counter for un-named regions
for basin,poly in zip(reader.records(),reader.geometries()):
    if basin.attributes['name']:
        cr.create_region(basin.attributes['name'],basin.attributes['name'].replace(' ','_'),poly)
    else:
        cpt+=1
        cr.create_region('Unknow'+str(cpt),'Unknow'+str(cpt),poly)

# List all the regions already defined
cr.get_list_regions()

# Complete the regions with some user-defined ones
##################################################
# North Hemisphere
cr.create_region('Northern hemisphere','NH',[[-180, 0], [180, 0], [180, 90], [-180,90], [-180, 0]])
# South Hemisphere
cr.create_region('Southern hemisphere','SH',[[-180, -90], [180, -90], [180, 0], [-180,0], [-180, -90]])
# Gulf Stream
cr.create_region('Gulf Stream', 'gus', [[-84, 30], [-56,30], [-56,42], [-84,42], [-84, 30]])
# Agulhas
cr.create_region('Agulhas current', 'agu', [[15,-42], [35,-42], [35,-30], [14,-30], [15,-42]])
# Nino3.4
cr.create_region('Nino 3_4', 'nin', [[-170,-5], [-120,-5], [-120,5], [-170,5], [-170,-5]])
# Nino3
cr.create_region('Nino 3', 'ni3', [[-150,-5], [-90,-5], [-90,5], [-150,5], [-150,-5]])
# Nino4
cr.create_region('Nino 4', 'ni4', [[160,-5], [210,-5], [210,5], [160,5], [160,-5]])
# Nino1+2
cr.create_region('Nino 1+2', 'ni12', [[-90,-10], [-80,-10], [-80,0], [-90,0], [-90,-10]])


# Do some plots
###############
#for region in cr.regions_dict.keys():
#    cr.plot_region(region)

#Saving regions
###############
# Save to netcdf all the regions masks
cr.create_nc('Regions_from_geo_marine.nc')

# Save to kmz all the regions polygons
#cr.create_kmz('Regions_from_geo_marine.kmz')

