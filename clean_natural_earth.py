import xarray as xr
import matplotlib.pyplot as plt         

ds= xr.open_dataset('Regions_from_geo_marine.nc')

atl = ['North_Atlantic_Ocean','South_Atlantic_Ocean','Gulf_of_Guinea','Gulf_of_Mexico','Caribbean_Sea','Labrador_Sea', 'North_Sea', 'Norwegian_Sea','Greenland_Sea','Bay_of_Biscay','Bay_of_Fundy','Gulf_of_Saint_Lawrence','Scotia_Sea','Straits_of_Florida','Gulf_of_Honduras','Irish_Sea','Delaware_Bay','Massachusetts_Bay','Denmark_Strait']
pac = ['North_Pacific_Ocean','South_Pacific_Ocean','Philippine_Sea','South_China_Sea','Sea_of_Japan','East_China_Sea','Sea_of_Okhotsk','Yellow_Sea','Gulf_of_Alaska','Bismarck_Sea','Solomon_Sea','Coral_Sea','Tasman_Sea','Sulu_Sea','Celebes_Sea','Banda_Sea','Arafura_Sea','Molucca_Sea','Halmahera_Sea','Ceram_Sea','Timor_Sea','Bay_of_Plenty','Golfo_de_California','Luzon_Strait']
ind=['INDIAN_OCEAN','Bay_of_Bengal','Arabian_Sea','Red_Sea','Persian_Gulf','Mozambique_Channel','Laccadive_Sea','Gulf_of_Thailand','Gulf_of_Oman','Gulf_of_Aden','Bab_el_Mandeb','Gulf_of_Aqaba']
med=['Mediterranean_Sea','Mediterranean_Sea_2','Tyrrhenian_Sea','Golfe_du_Lion','Adriatic_Sea','Ionian_Sea','Gulf_of_Gabès','Ligurian_Sea','Alboran_Sea','Sea_of_Crete','Aegean_Sea','Balearic_Sea','Dardanelles']
arc = ['Arctic_Ocean','Beaufort_Sea','Barents_Sea','Kara_Sea','Bering_Sea','Chukchi_Sea','Laptev_Sea','East_Siberian_Sea','Baffin_Bay']
tmaskatl = sum([ds['tmask'+sub] for sub in atl])
plot_region(tmaskatl)
tmaskpac = sum([ds['tmask'+sub] for sub in pac])
plot_region(tmaskpac)
tmaskind = sum([ds['tmask'+sub] for sub in ind])
plot_region(tmaskind)
tmaskmed = sum([ds['tmask'+sub] for sub in med])
plot_region(tmaskmed)
tmaskarc = sum([ds['tmask'+sub] for sub in arc])
plot_region(tmaskarc)

for sub in atl+pac+ind+med+arc:
    print('Droping '+sub)
    ds = ds.drop('tmask'+sub)

def plot_region(region):
    """
    Creates a simple plot of the mask
    """
    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs
    import cartopy.feature as cfea

    fig = plt.figure(figsize=(12,6))
    ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
    mapa = region.plot(x='nav_lon',y='nav_lat',ax=ax,transform=ccrs.PlateCarree(),add_colorbar=False)
    ax.set_title('EC-Earth3.2 ');ax.coastlines(resolution='50m');ax.add_feature(cfea.LAND, zorder=100);
    gl=ax.gridlines(draw_labels=True);gl.xlabels_top = False;gl.ylabels_right = False;
    plt.show()


