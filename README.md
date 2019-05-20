# What is Regions_maskd_generator ?
This tools aims at generating regions mask in netcdf format in a way that it can be ported to any configuration and / or any model, to allow for simple comparisons when dealing with regional studies from larger models.

The script run_create_regions.py provides a simple example of all the steps and functions. 

## What is the general philosophy ?
There are two options to define a region:
- by hand: provide a region name and a list of [lon, lat] points that define a polygon
- via a kmz file: these are file that can be easily edited via Google Maps or (better Google Earth). The kmz file has
 to include a list of Polygons that defines the area of the region requested.
Regions defined are stored into a dictionary called "regions_dict" that can be modified and saved to netcdf and kmz format.

## What do I need to run this ?
Python 3 and the following librairies:
- xarray : http://xarray.pydata.org/en/stable/index.html
- regionmask : https://regionmask.readthedocs.io/en/stable/

## How to start ?
1) Add create_regions.py to a directory in your PYTHONPATH (or current directory)
2) open a python console
3) Import create_regions and define your configuration (cf. example in run_create_regions.py)
4) Start define your regions
5) Save your regions to kmz and / or netcdf files

## How to create regions by hand ?
Check examples in run_create_regions.py
create_region function takes 3 arguments :
- name of the region
- abbreviated name (in the netcdf file, mask will be named "tmaskxxxx" xxxx begin the abbreviated name
- list of [lon,lat] points defining a closed polygon that will define the area of the region

## How to create regions from kmz file ?
Use the function create_regions_from_kmz('my_kmz_file.kmz')

## How to create a kmz file with multiple polygons ?
In Google Earth:
1) Right-click on "My Places" -> Add -> Folder
2) Right-click on the new Folder -> Add -> Polygon
Repeat 2) for every new region
3) Right-click on the new Folder -> Save Place As

## How to modify a polygon in Google Earth ?
Right-click on the Polygon -> Properties -> Right-click on points of the Polygon to suppress them / Left-click to add a new point

## How do I know the regions already defined ?
Use the function get_list_regions()

## I've defined some regions, but I'm not totaly happy with one that I'd like to modify. What should I do ?
This can be done in 3 simple steps:
1) store the Polygon of the region you want to modify using the function get_polygon
2) do the modification on this Polygon
3) update the region definition with the new polygon using update_region. This will also update the mask of the region.

## Ok, my regions are well defined, how do I generate a netcdf file with all the regions ?
Use the function create_nc('my_nc_file.nc')

## And what about saving a proper kmz file with the polygons of all the regions defined ?
Use the function create_kmz('my_kmz_file.kmz')

## I have a nice kmz file that I already used to generate regions, and I want to use it to generate the same region masks for my brand new configuration. How should I do ?
Use the function create_nc_from_kmz('my_kmz_file.kmz','my_nc_file.nc')
