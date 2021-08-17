import folium
import pandas
from pandas.io.parsers import read_csv

data = pandas.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data['NAME'])
location = list(data['LOCATION'])
status = list(data['STATUS'])
timeframe = list(data['TIMEFRAME'])

html = """
<strong>name:</strong> 
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a>
<br>
<strong>Height:</strong> %s m
<br>
<strong>Location:</strong> %s
<br>
<strong>Status:</strong> %s
<br> 
<strong>TimeFrame:</strong> %s
"""

def color_producer(el):
    if el < 2000:
        return 'green'
    elif el >= 2000 and el < 3000:
        return 'orange'
    elif el > 3000:
        return 'red'
    else:
        return 'blue'

map = folium.Map(location = [38, -99], zoomstart=0, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, nm, el, loc, st, tf in zip(lat, lon, name, elev, location, status, timeframe):
    iframe = folium.IFrame(html = html % (nm, nm, el, loc, st, tf), width=200, height=100)
    fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon = folium.Icon(color = color_producer(el))))
    
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))
    
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")


