# coding: utf8
import xarray as xr
import matplotlib.pyplot as plt         


tmask = xr.open_dataset('/esarchive/scratch/barakuda/climatology/ORCA1.L75/mesh_mask.nc4').tmask.isel(z=0).squeeze()
ds= xr.open_dataset('Regions_from_geo_marine.nc')

atl = ['North_Atlantic_Ocean','South_Atlantic_Ocean','Gulf_of_Guinea','Gulf_of_Mexico','Caribbean_Sea','Labrador_Sea','Bay_of_Biscay','Scotia_Sea','English_Channel','North_Sea','Bristol_Channel','Inner_Seas','Irish_Sea','Skagerrak','Bay_of_Fundy','Gulf_of_Saint_Lawrence','Straits_of_Florida','Gulf_of_Honduras','Delaware_Bay','Massachusetts_Bay','Denmark_Strait','Bahía_de_Campeche','Río_de_la_Plata','Gulf_of_Maine','Chesapeake_Bay','Yucatan_Channel','Canal_Perigoso','Canal_do_Sul','Canal_do_Norte','Amazon_River','Bahía_Grande','Lagoa_dos_Patos','Bras_d\'Or_Lake','Boca_Grande','Baía_de_Marajó','Golfo_San_Matías','Baía_de_São_Marcos','Hamilton_Inlet','Waddenzee','Bight_of_Benin','Bight_of_Biafra','Strait_of_Belle_Isle','Bahía_Blanca','Lago_de_Maracaibo','Long_Island_Sound','Albemarle_Sound','Pamlico_Sound','Lake_Pontchartrain','Saint_Lawrence_River','Boknafjorden','St._Helena_Bay','Golfo_de_Urabá','Wager_Bay','Ungava_Bay']

pac = ['North_Pacific_Ocean','South_Pacific_Ocean','Philippine_Sea','South_China_Sea','Sea_of_Japan','East_China_Sea','Sea_of_Okhotsk','Yellow_Sea','Gulf_of_Alaska','Bismarck_Sea','Solomon_Sea','Coral_Sea','Tasman_Sea','Sulu_Sea','Celebes_Sea','Banda_Sea','Molucca_Sea','Halmahera_Sea','Ceram_Sea','Bay_of_Plenty','Golfo_de_California','Luzon_Strait','Queen_Charlotte_Sound','Gulf_of_Tonkin','Korea_Strait','Taiwan_Strait','Cook_Inlet','Shelikhova_Gulf','Bo_Hai','Golfo_de_Panamá','Great_Barrier_Reef','San_Francisco_Bay','Monterey_Bay','Yangtze_River','Columbia_River','Salish_Sea','Hecate_Strait','Cordova_Bay','Gulf_of_Buli','Gulf_of_Kau','Bohol_Sea','Samar_Sea','Tayabas_Bay','Seno_de_Skyring','Seno_Otway','Davao_Gulf','Gulf_of_Tomini','Sibuyan_Sea','Selat_Dampier','Leyte_Gulf','Visayan_Sea','Dixon_Entrance','Golfo_Corcovado','Kronotskiy_Gulf','Uda_Bay','Uchiura_Bay','Tsugaru_Strait','Tatar_Strait','Golfo_de_Tehuantepec','Golfo_de_Guayaquil','La_Pérouse_Strait','East_Korea_Bay','Qiongzhou_Strait','Cook_Strait','Torres_Strait','Gulf_of_Papua','Porpoise_Bay','Golfo_de_Penas','Queen_Charlotte_Strait','Bay_Inútil','Gulf_of_Sakhalin','Gulf_of_Kamchatka','Hangzhou_Bay','Estrecho_de_Magellanes','Prince_William_Sound','Inner_Sea','Flores_Sea','Java_Sea','Gulf_of_Thailand','Makassar_Strait','Arafura_Sea','Gulf_of_Carpentaria','Bali_Sea','Surigao_Strait','Selat_Bali']

ind=['INDIAN_OCEAN','Bay_of_Bengal','Arabian_Sea','Red_Sea','Persian_Gulf','Mozambique_Channel','Laccadive_Sea','Gulf_of_Oman','Gulf_of_Aden','Bab_el_Mandeb','Gulf_of_Aqaba','Andaman_Sea','Great_Australian_Bight','Strait_of_Malacca','Strait_of_Singapore','Gulf_of_Mannar','Gulf_of_Kutch','Ragay_Gulf','Gulf_of_Khambhät','Palk_Strait','Shark_Bay','Gulf_of_Masira','Geographe_Bay','Gulf_of_Suez','Gulf_of_Martaban','Joseph_Bonaparte_Gulf','Baia_de_Maputo','Gulf_St._Vincent','Antongila_Bay','Timor_Sea','Savu_Sea','Bass_Strait']

med=['Mediterranean_Sea','Mediterranean_Sea_2','Tyrrhenian_Sea','Golfe_du_Lion','Adriatic_Sea','Ionian_Sea','Gulf_of_Gabès','Ligurian_Sea','Alboran_Sea','Sea_of_Crete','Aegean_Sea','Balearic_Sea','Dardanelles','Strait_of_Gibraltar','Golfo_San_Jorge','Gulf_of_Sidra','Sea_of_Marmara']

arc = ['Arctic_Ocean','Norwegian_Sea','Greenland_Sea','Beaufort_Sea','Barents_Sea','Kara_Sea','Bering_Sea','Chukchi_Sea','Laptev_Sea','East_Siberian_Sea','Baffin_Bay','Davis_Strait','White_Sea','The_North_Western_Passages','Bristol_Bay','Melville_Bay','Amundsen_Gulf','Viscount_Melville_Sound','Lincoln_Sea','Gulf_of_Anadyr\'','Murchison_Sound','Robeson_Channel','Kennedy_Channel','Darnley_Bay','Prince_of_Wales_Strait','Minto_Inlet','Richard_Collinson_Inlet','Prince_ALbert_Sound','Liddon_Gulf','Wynniatt_Bay','Hadley_Bay','Bathurst_Inlet','Goldsmith_Channel','Sherman_Basin','Fury_and_Hecla_Strait','Jones_Sound','Eclipse_Sound','Uummannaq_Fjord','Matochkin_Shar_Strait','Ozero_Mogotoyevo','Guba_Gusinaya','Franklin_Bay','M\'Clure_Strait','Cumberland_Sound','Frobisher_Bay','Disko_Bay','Karskiye_Strait','Vil\'kitskogo_Strait','Norton_Sound','Kotzebue_Sound','Gulf_of_Boothia','Kane_Basin','Foxe_Basin','Gulf_of_Yana','Dmitriy_Laptev_Strait','Gulf_of_Ob','Yenisey_Gulf','Smith_Sound','Baird_Inlet','Husky_Lakes','Hall_Basin','Kangertittivaq','Chaun_Bay','Khatanga_Gulf','Karaginskiy_Gulf','Gulf_of_Olen‘k']

soc = ['SOUTHERN_OCEAN','Ross_Sea','Ross_Sea_2','Weddell_Sea','Bellingshausen_Sea','Amundsen_Sea','Drake_Passage','Marguerite_Bay','Prydz_Bay','Vincennes_Bay','Peacock_Sound','George_VI_Sound','Wrigley_Gulf','Sulzberger_Bay','Ronne_Entrance','Bransfield_Strait','McMurdo_Sound','Mackenzie_Bay','Lützow-Holm_Bay','Davis_Sea']

nwatl = ['Hudson_Bay','James_Bay','Hudson_Strait','Wager_Bay','Ungava_Bay']

tmasktmpnna = xr.where(ds.nav_lat>47.,ds.tmaskNorth_Atlantic_Ocean,0)
nna = ['Labrador_Sea','Norwegian_Sea','Greenland_Sea','Baltic_Sea','Storfjorden','Gulf_of_Finland','Scotia_Sea','English_Channel','North_Sea','Bristol_Channel','Inner_Seas','Irish_Sea','Gulf_of_Bothnia','Mecklenburger_Bucht','Øresund','Stettiner_Haff','Vestfjorden','Skagerrak','Sognefjorden','Trondheimsfjorden','Kattegat','Gulf_of_Riga','Denmark_Strait']

balt = ['Baltic_Sea','Gulf_of_Finland','Gulf_of_Bothnia','Mecklenburger_Bucht','Øresund','Stettiner_Haff','Kaliningrad','Kattegat','Gulf_of_Riga','Skagerrak']
casp = ['Caspian_Sea','Garabogaz_Bay']
blk = ['Black_Sea','Sea_of_Azov','Bosporus']
indo = ['Java_Sea','Solomon_Sea','Coral_Sea','Sulu_Sea','Celebes_Sea','Banda_Sea','Arafura_Sea','Molucca_Sea','Halmahera_Sea','Ceram_Sea','Timor_Sea','Andaman_Sea','Makassar_Strait','Savu_Sea','Gulf_of_Buli','Bohol_Sea','Surigao_Strait','Ragay_Gulf','Samar_Sea','Tayabas_Bay','Bali_Sea','Selat_Bali','Gulf_of_Tomini','Flores_Sea','Selat_Dampier','Makassar_Strait']
gomex = ['Bahía_de_Campeche','Gulf_of_Mexico','Yucatan_Channel','Boca_Grande','Lake_Pontchartrain']
carib = ['Golfo_de_Urabá']
sargasso = ['Sargasso_Sea']
gin = ['Norwegian_Sea','Greenland_Sea']

tmaskatl = sum([ds['tmask'+sub] for sub in atl])
tmaskpac = sum([ds['tmask'+sub] for sub in pac])
tmaskind = sum([ds['tmask'+sub] for sub in ind])
tmaskmed = sum([ds['tmask'+sub] for sub in med])
tmaskarc = sum([ds['tmask'+sub] for sub in arc])
tmasksoc = sum([ds['tmask'+sub] for sub in soc])
tmaskgin = sum([ds['tmask'+sub] for sub in gin])
tmasknna = sum([ds['tmask'+sub] for sub in nna])+tmasktmpnna
tmasklab = ds.tmaskLabrador_Sea
tmaskwed = ds.tmaskWeddell_Sea
plot_region(tmaskatl)
plot_region(tmaskpac)
plot_region(tmaskind)
plot_region(tmaskmed)
plot_region(tmaskarc)
plot_region(tmasksoc)
plot_region(tmasklab)
plot_region(tmaskwed)
plot_region(tmaskgin)
plot_region(tmasknna)


for sub in atl+pac+ind+med+arc+soc+balt+blk+nwatl+casp:
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
    mapa = region.plot(x='nav_lon',y='nav_lat',ax=ax,transform=ccrs.PlateCarree())
    land_50m = cfea.NaturalEarthFeature('physical', 'land', '50m', 
                                         edgecolor='face', 
                                         facecolor=cfea.COLORS['land'])
    ax.set_title('EC-Earth3.2 ');ax.coastlines(resolution='50m');ax.add_feature(land_50m,zorder=100);
    gl=ax.gridlines(draw_labels=True);gl.xlabels_top = False;gl.ylabels_right = False;
    plt.show()


