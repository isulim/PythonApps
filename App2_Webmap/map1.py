import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lats = list(data["LAT"])
lons = list(data["LON"])
names = list(data["NAME"])
elevs = list(data["ELEV"])

html = """
<h4>Volcano name:<br>
<a href="https://google.com/search?q={0}" target="_blank">{0}</a><br>
Height: {1} m
"""

def elevation_gradient(elevation):
    if elevation < 2000:
        return 'green'
    elif 2000 <= elevation <= 3000:
        return 'orange'
    else:
        return 'red'


map = folium.Map(location=(38.58, -99.09), zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name='Volcanoes in US')

for lat, lon, elev, name in zip(lats, lons, elevs, names):
    iframe = folium.IFrame(html=html.format(name, elev), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lat, lon], popup=folium.Popup(iframe), radius=5, fill=True, color=elevation_gradient(elev)))


fgp = folium.FeatureGroup(name='Population')
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                                    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                                                                    else 'yellow' if 10000000 <= x['properties']['POP2005'] <= 20000000 
                                                                                    else 'red'}))


map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("Map1.html")
