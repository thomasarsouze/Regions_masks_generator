# coding: utf8
import xarray as xr
import matplotlib.pyplot as plt         
import numpy as np

grid='ORCA025'

grid_name={'ORCA1':'/esarchive/scratch/barakuda/climatology/'+grid+'.L75/mesh_mask.nc4',
           'ORCA025':'/esarchive/scratch/barakuda/climatology/'+grid+'.L75/mesh_mask_ORCA025.L75_ece3.2_2017.nc4',
           'ORCA12':'/esarchive/releases/models/nemo/v3.6_ecearth/inidata/nemo/ORCA12L75/mesh_mask_ORCA12_3.6.nc'}
tmask = xr.open_dataset(grid_name[grid]).tmask.isel(z=0).squeeze()
ds= xr.open_dataset('Regions_from_geo_marine_'+grid+'.nc')
tmask=tmask.to_dataset().merge(ds.coords).to_array().drop('variable').squeeze()

atl = ['North_Atlantic_Ocean','South_Atlantic_Ocean','Inner_Seas','Irish_Sea','North_Sea','Norwegian_Sea','Greenland_Sea','Scotia_Sea','Golfo_de_Urabá','Golfo_San_Jorge','Gulf_of_Guinea','Gulf_of_Honduras','Gulf_of_Maine','Gulf_of_Mexico','Gulf_of_Saint_Lawrence','Caribbean_Sea','Labrador_Sea','Bahía_Blanca','Baía_de_Marajó','Bay_of_Biscay','Bay_of_Fundy','Bight_of_Benin','Bight_of_Biafra','Chesapeake_Bay','Delaware_Bay','Massachusetts_Bay','Wager_Bay','English_Channel','Bristol_Channel','Skagerrak','Straits_of_Florida','Denmark_Strait','Yucatan_Channel','Bahía_de_Campeche','Río_de_la_Plata','Canal_Perigoso','Canal_do_Sul','Canal_do_Norte','Amazon_River','Bahía_Grande','Lagoa_dos_Patos','Bras_d\'Or_Lake','Boca_Grande','Golfo_San_Matías','Baía_de_São_Marcos','Hamilton_Inlet','Waddenzee','Strait_of_Belle_Isle','Lago_de_Maracaibo','Long_Island_Sound','Albemarle_Sound','Pamlico_Sound','Lake_Pontchartrain','Saint_Lawrence_River','Boknafjorden','St._Helena_Bay','Kattegat','Øresund']
pac = ['North_Pacific_Ocean','South_Pacific_Ocean','Bali_Sea','Banda_Sea','Bering_Sea','Bismarck_Sea','Celebes_Sea','Ceram_Sea','Coral_Sea','East_China_Sea','Flores_Sea','Halmahera_Sea','Inner_Sea','Java_Sea','Molucca_Sea','Philippine_Sea','Sea_of_Japan','Solomon_Sea','South_China_Sea','Sea_of_Okhotsk','Sulu_Sea','Tasman_Sea','Yellow_Sea','Bay_Inútil','Bay_of_Plenty','Golfo_de_California','Golfo_de_Panamá','Gulf_of_Alaska','Gulf_of_Thailand','Luzon_Strait','Queen_Charlotte_Sound','Smith_Sound','Gulf_of_Tonkin','Korea_Strait','Taiwan_Strait','Cook_Inlet','Shelikhova_Gulf','Bo_Hai','Great_Barrier_Reef','Karaginskiy_Gulf','San_Francisco_Bay','Monterey_Bay','Ragay_Gulf','Yangtze_River','Columbia_River','Salish_Sea','Hecate_Strait','Cordova_Bay','Gulf_of_Buli','Gulf_of_Kau','Bohol_Sea','Samar_Sea','Tayabas_Bay','Seno_de_Skyring','Seno_Otway','Gulf_of_Anadyr\'','Davao_Gulf','Gulf_of_Tomini','Sibuyan_Sea','Selat_Dampier','Leyte_Gulf','Visayan_Sea','Dixon_Entrance','Golfo_Corcovado','Kronotskiy_Gulf','Bristol_Bay','Uda_Bay','Uchiura_Bay','Tsugaru_Strait','Tatar_Strait','Golfo_de_Tehuantepec','Golfo_de_Guayaquil','La_Pérouse_Strait','East_Korea_Bay','Qiongzhou_Strait','Cook_Strait','Torres_Strait','Gulf_of_Papua','Porpoise_Bay','Norton_Sound','Golfo_de_Penas','Queen_Charlotte_Strait','Gulf_of_Sakhalin','Gulf_of_Kamchatka','Hangzhou_Bay','Estrecho_de_Magellanes','Prince_William_Sound','Makassar_Strait','Surigao_Strait','Selat_Bali']
ind=['INDIAN_OCEAN','Andaman_Sea','Arabian_Sea','Arafura_Sea','Red_Sea','Timor_Sea','Savu_Sea','Bay_of_Bengal','Persian_Gulf','Mozambique_Channel','Laccadive_Sea','Gulf_of_Oman','Gulf_of_Aden','Bab_el_Mandeb','Gulf_of_Aqaba','Gulf_of_Carpentaria','Great_Australian_Bight','Strait_of_Malacca','Strait_of_Singapore','Gulf_of_Mannar','Gulf_of_Kutch','Gulf_of_Khambhät','Palk_Strait','Shark_Bay','Gulf_of_Masira','Geographe_Bay','Gulf_of_Suez','Gulf_of_Martaban','Joseph_Bonaparte_Gulf','Baia_de_Maputo','Gulf_St._Vincent','Antongila_Bay','Bass_Strait']
med=['Mediterranean_Sea','Mediterranean_Sea_2','Tyrrhenian_Sea','Golfe_du_Lion','Adriatic_Sea','Ionian_Sea','Gulf_of_Gabès','Ligurian_Sea','Alboran_Sea','Sea_of_Crete','Aegean_Sea','Balearic_Sea','Dardanelles','Strait_of_Gibraltar','Gulf_of_Sidra','Sea_of_Marmara']
arc = ['Arctic_Ocean','Norwegian_Sea','Greenland_Sea','Beaufort_Sea','Barents_Sea','Kara_Sea','Chukchi_Sea','Laptev_Sea','East_Siberian_Sea','Baffin_Bay','Davis_Strait','White_Sea','The_North_Western_Passages','Melville_Bay','Amundsen_Gulf','Viscount_Melville_Sound','Lincoln_Sea','Murchison_Sound','Robeson_Channel','Kennedy_Channel','Darnley_Bay','Prince_of_Wales_Strait','Minto_Inlet','Richard_Collinson_Inlet','Prince_ALbert_Sound','Liddon_Gulf','Wynniatt_Bay','Hadley_Bay','Bathurst_Inlet','Goldsmith_Channel','Sherman_Basin','Fury_and_Hecla_Strait','Jones_Sound','Eclipse_Sound','Uummannaq_Fjord','Matochkin_Shar_Strait','Ozero_Mogotoyevo','Guba_Gusinaya','Franklin_Bay','M\'Clure_Strait','Cumberland_Sound','Frobisher_Bay','Disko_Bay','Karskiye_Strait','Vil\'kitskogo_Strait','Kotzebue_Sound','Gulf_of_Boothia','Kane_Basin','Foxe_Basin','Gulf_of_Yana','Dmitriy_Laptev_Strait','Gulf_of_Ob','Yenisey_Gulf','Baird_Inlet','Husky_Lakes','Hall_Basin','Kangertittivaq','Chaun_Bay','Mackenzie_Bay','Khatanga_Gulf','Gulf_of_Olen‘k']
soc = ['SOUTHERN_OCEAN','Amundsen_Sea','Bellingshausen_Sea','Davis_Sea','Ross_Sea','Ross_Sea_2','Weddell_Sea','Drake_Passage','Marguerite_Bay','Prydz_Bay','Sulzberger_Bay','Vincennes_Bay','Peacock_Sound','George_VI_Sound','Wrigley_Gulf','Ronne_Entrance','Bransfield_Strait','McMurdo_Sound','Lützow-Holm_Bay']
nwatl = ['Hudson_Bay','James_Bay','Hudson_Strait','Wager_Bay','Ungava_Bay']
nna = ['North_Atlantic_Ocean','Labrador_Sea','Norwegian_Sea','Greenland_Sea','Baltic_Sea','Storfjorden','Gulf_of_Finland','Scotia_Sea','English_Channel','North_Sea','Bristol_Channel','Inner_Seas','Irish_Sea','Gulf_of_Bothnia','Mecklenburger_Bucht','Øresund','Stettiner_Haff','Vestfjorden','Skagerrak','Sognefjorden','Trondheimsfjorden','Kattegat','Gulf_of_Riga','Denmark_Strait']
balt = ['Baltic_Sea','Gulf_of_Finland','Gulf_of_Bothnia','Mecklenburger_Bucht','Stettiner_Haff','Kaliningrad','Gulf_of_Riga']
casp = ['Caspian_Sea','Garabogaz_Bay']
blk = ['Black_Sea','Sea_of_Azov','Bosporus']
indo = ['Arafura_Sea','Bali_Sea','Banda_Sea','Celebes_Sea','Ceram_Sea','Flores_Sea','Halmahera_Sea','Java_Sea','Molucca_Sea','Philippine_Sea','Savu_Sea','South_China_Sea','Timor_Sea','Makassar_Strait','Gulf_of_Buli','Bohol_Sea','Surigao_Strait','Ragay_Gulf','Samar_Sea','Tayabas_Bay','Selat_Bali','Gulf_of_Tomini','Selat_Dampier']
gomex = ['Bahía_de_Campeche','Gulf_of_Mexico','Yucatan_Channel','Boca_Grande','Lake_Pontchartrain','Straits_of_Florida','Yucatan_Channel']
carib = ['Caribbean_Sea','Golfo_de_Urabá']
sargasso = ['Sargasso_Sea']
gin = ['Norwegian_Sea','Greenland_Sea']

maskattrs={'atl':{'Desciption':'Atlantic Ocean Mask',
                  'Details':'This mask is the sum of %s masks' % ', '.join(atl),
                  'Additional':'Latitude is limited to -55S '},
           'pac':{'Desciption':'Pacific Ocean Mask',
                  'Details':'This mask is the sum of %s masks' % ', '.join(pac),
                  'Additional':'Latitude is limited to -43S '}, 
           'ind':{'Desciption':'Indian Ocean Mask',
                  'Details':'This mask is the sum of %s masks' % ', '.join(ind),
                  'Additional':'Latitude is limited to -43S '},          
           'med':{'Desciption':'Mediterranean Ocean Mask',
                  'Details':'This mask is the sum of %s masks' % ', '.join(med)},
           'arc':{'Desciption':'Arctic Ocean Mask',
                  'Details':'This mask is the sum of %s masks' % ', '.join(arc)},
           'soc':{'Desciption':'Southern Ocean Mask',
                  'Details':'This mask is the sum of %s masks' % ', '.join(soc),
                  'Additional':'Latitude is extended to -43S'},
           'nna':{'Desciption':'North Atlantic North basin Mask',
                  'Details':'This mask is the sum of %s masks' % ', '.join(nna)},
           'gin':{'Desciption':'Greenland, Iceland, Norwegian Seas Mask',
                  'Details':'This mask is the sum of %s masks' % ', '.join(gin)},
           'bal':{'Desciption':'Batlic Sea Mask',
                  'Details':'This mask is the sum of %s masks' % ', '.join(balt)},
           'ido':{'Desciption':'Indonesian Seas Mask',
                  'Details':'This mask is the sum of %s masks' % ', '.join(indo)},
           'blk':{'Desciption':'Black Sea Mask',
                  'Details':'This mask is the sum of %s masks' % ', '.join(blk)},
           'gum':{'Desciption':'Gulf of Mexico Mask',
                  'Details':'This mask is the sum of %s masks' % ', '.join(gomex)},
           'car':{'Desciption':'Carribean Sea Mask',
                  'Details':'This mask is the sum of %s masks' % ', '.join(carib)},
           'lab':{'Desciption':'Labrador Sea Mask'},
           'wed':{'Desciption':'Weddel Sea Mask',
                  'Additional':'Latitude is extended to -62S, longitude between -60E and 0E'},
           'NoH':{'Desciption':'Northern Hemisphere Mask'},
           'SoH':{'Desciption':'Southern Hemisphere Mask'},
           'gus':{'Desciption':'Gulf Stream region Mask'},
           'agu':{'Desciption':'Agulhas region Mask'},
           'nin':{'Desciption':'Nino3+4 box Mask'},
           'ni3':{'Desciption':'Nino3 box Mask'},
           'ni4':{'Desciption':'Nino4 box Mask'},
           'n12':{'Desciption':'Nino1+2 box Mask'},
            }

tmaskatl = sum([ds['tmask'+sub] for sub in atl])
tmaskatl = xr.where(ds.nav_lat<-55.,0,tmaskatl) 
tmaskpac = sum([ds['tmask'+sub] for sub in pac])
tmaskpac = xr.where(ds.nav_lat<-43,0,tmaskpac)
tmaskpac = xr.where((ds.nav_lon>179) & (ds.nav_lat>=-43) & (ds.nav_lat<25),np.minimum(tmask+tmaskpac,1),tmaskpac)
tmaskind = sum([ds['tmask'+sub] for sub in ind])
tmaskind = xr.where(ds.nav_lat<-43,0,tmaskind)
tmaskmed = sum([ds['tmask'+sub] for sub in med])
tmaskarc = sum([ds['tmask'+sub] for sub in arc])
tmasksoc = sum([ds['tmask'+sub] for sub in soc])
tmasksoc = xr.where(ds.nav_lat<-43,np.minimum(tmask+tmasksoc,1),tmasksoc)
tmaskgin = sum([ds['tmask'+sub] for sub in gin])
tmasknna = sum([ds['tmask'+sub] for sub in nna])
tmasknna = xr.where(ds.nav_lat>47.,tmasknna,0)
tmaskbal = sum([ds['tmask'+sub] for sub in balt])
tmaskblk = sum([ds['tmask'+sub] for sub in blk])
tmaskgum = sum([ds['tmask'+sub] for sub in gomex])
tmaskido = sum([ds['tmask'+sub] for sub in indo])
tmaskcar = sum([ds['tmask'+sub] for sub in carib])
tmasklab = ds.tmaskLabrador_Sea
tmaskwed = ds.tmaskWeddell_Sea
tmaskwed = xr.where((ds.nav_lat<-62) & (ds.nav_lon >-60) & (ds.nav_lon <0),np.minimum(tmask+tmaskwed,1),tmaskwed)
tmaskNoH = ds.tmaskNH
tmaskSoH = ds.tmaskSH
tmaskgus = ds.tmaskgus
tmaskagu = ds.tmaskagu
tmasknin = ds.tmasknin
tmaskni3 = ds.tmaskni3
tmaskni4 = ds.tmaskni4
tmaskn12 = ds.tmaskni12


for basin in maskattrs.keys():
    for attr,value in maskattrs[basin].items():
        eval('tmask'+basin).attrs[attr]=value 
        eval('tmask'+basin).name='tmask'+basin

basins=[eval('tmask'+basin) for basin in list(maskattrs.keys())]
ds_out=xr.merge(basins)
ds_out.to_netcdf('subbasins_'+grid+'.nc')

def plot_region(region):
    """
    Creates a simple plot of the mask
    """
    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs
    import cartopy.feature as cfea

    fig = plt.figure(figsize=(12,6))
    ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
    mapa = region.plot(x='nav_lon',y='nav_lat',ax=ax,transform=ccrs.PlateCarree())
    land_50m = cfea.NaturalEarthFeature('physical', 'land', '50m', 
                                         edgecolor='face', 
                                         facecolor=cfea.COLORS['land'])
    ax.set_title('EC-Earth3.2 ');ax.coastlines(resolution='50m');ax.add_feature(land_50m,zorder=100);
    gl=ax.gridlines(draw_labels=True);gl.xlabels_top = False;gl.ylabels_right = False;
    plt.show()


