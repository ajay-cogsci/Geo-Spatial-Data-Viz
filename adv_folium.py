

from flask import Flask
import folium

from branca.element import Figure

fig = Figure(width = 550 , height= 350)



app = Flask(__name__)
@app.route('/')
def index():
    start_coords = (51.389167,30.099444) #Coordiniates of Chernobyl
    folium_map = folium.Map(width=550, height=350, location=start_coords, zoom_start=11, min_zoom=8, max_zoom=14)
    fig.add_child(folium_map)

    folium.TileLayer('Stamen Terrain').add_to(folium_map)
    folium.TileLayer('Stamen Toner').add_to(folium_map)
    folium.TileLayer('Stamen Water Color').add_to(folium_map)
    folium.TileLayer('cartodbpositron').add_to(folium_map)
    folium.TileLayer('cartodbdark_matter').add_to(folium_map)
    folium.LayerControl().add_to(folium_map)



    return  fig._repr_html_()



if __name__ == '__main__':
    app.run(debug=True)
