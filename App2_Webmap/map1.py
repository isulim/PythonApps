import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

html = """
<h4>Volcano name:<br>
<a href="https://google.com/search?q={0}" target="_blank">{0}</a><br>
Height: {1} m
"""

map = folium.Map(location=(38.58, -99.09), zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name='My Map')

for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html.format(nm, el), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")
