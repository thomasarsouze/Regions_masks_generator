import create_regions as cr

"""
mask_file : name of the file that contains longitude, latitude and 2D landsea mask file
lon_name  : name of the longitude variable
lat_name  : name of the latitude variable
mask_name : name of the global mask variable
"""

#user defined configuration
###########################
mask_file = "/esarchive/autosubmit/con_files/mesh_mask_nemo.N3.6_O1L75.nc"
lon_name  = "nav_lon"
lat_name  = "nav_lat"
mask_name = "tmask"

cr.define_config(mask_file,lon_name,lat_name,mask_name)

#Defining regions
#################
# Some examples of hand-defined regions
# North Hemisphere
cr.create_region('Northern hemisphere','NH',[[-180, 0], [180, 0], [180, 90], [-180,90], [-180, 0]])
# South Hemisphere
cr.create_region('Southern hemisphere','SH',[[-180, -90], [180, -90], [180, 0], [-180,0], [-180, -90]])
# Antarctic Ocean 
cr.create_region('Southern Ocean','SO',[[-180, -90], [180, -90], [180, -46.5], [-180,-46.5], [-180, -90]])
# Artcic
cr.create_region('Arctic Ocean','arc',[[-180, 62.5], [180, 62.5], [180, 90], [-180, 90], [-180, 62.5]])
# GIN Seas
cr.create_region('GIN Seas', 'gin', [[-45,50], [15,50], [15,85], [-45,85], [-45,50]])
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
cr.create_region('Nino 1+2', 'ni1', [[-90,-10], [-80,-10], [-80,0], [-90,0], [-90,-10]])

# Example of kmz defined regions
cr.create_regions_from_kmz('Example.kmz')

# List all the regions already defined
cr.get_list_regions()

# Modify on region
test1_polygon = cr.get_polygon('test1')
test1_polygon.pop(3) # removes the 3rd point of the polygon
test1_polygon.insert(3,[-31,36]) # Add this new pint in third position
cr.update_region('test1',test1_polygon)

#Saving regions
#################
# Save to netcdf all the regions masks
cr.create_nc('Regions.nc')

# Save to kmz all the regions polygons
cr.create_kmz('Regions.kmz')

#Apply regions to new configuration
###################################
# Now define a new configuration
mask_file = "/esarchive/autosubmit/con_files/mesh_mask_nemo.N3.6_O25L75.nc"
cr.define_config(mask_file,lon_name,lat_name,mask_name)

cr.create_nc_from_kmz('Regions.kmz','Regions_HR.nc')

