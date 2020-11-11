import folium
import pandas as pd

df = pd.read_csv('mapy/Volcanoes.csv')

sty = "<h3> %s </h3> <b> %s </b> meters high"

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    
    elif 1000 <= elevation < 2500:
        return 'orange'
    
    else:
        return 'red'


map = folium.Map(location = [38.58,-99.09], zoom_start=6, tiles="Stamen Terrain")

#fg = folium.FeatureGroup("My Map")

fgv = folium.FeatureGroup(name='Volcanoes')
for lt, ln, lc, el in zip(df.LAT, df.LON, df.NAME, df.ELEV):
    iframe = folium.IFrame(html=sty % (lc, str(el)), width=200, height=100)
    fgv.add_child(folium.CircleMarker(
        location=[lt, ln], radius = 8,
        popup= folium.Popup(iframe), fill_color = color_producer (el), color =color_producer (el), fill_opacity = 0.7,))

fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('mapy/world.json', 'r', encoding='utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgp)
map.add_child(fgv)
map.add_child(folium.LayerControl())

map.save('mapy/Map1.html')


