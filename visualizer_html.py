import pandas as pd
import folium as fl
from folium.plugins import MarkerCluster
from src.database import get_connection
from src.paths import IMAGES_DIR
import branca.element

def get_data():
    conn = get_connection()
    query = 'SELECT * FROM zonas_wifi_bucaramanga;'

    df = pd.read_sql(query, conn)

    conn.close()

    return df

df = get_data()

city_centre = [df["latitud"].mean(), df["longitud"].mean()]


mp = fl.Map(location=city_centre, zoom_start=13)

marker_cluster = MarkerCluster().add_to(mp)


for _, row in df.iterrows():
    
    wifi_position =  [row["latitud"], row["longitud"]]
    html = f"""
<b>Zona WiFi:</b> {row['nombre_zona_wifi']}<br>
<b>Comuna:</b> {row['comuna']}<br>
<b>Barrio:</b> {row['barrio']}<br>
"""
    popup = fl.Popup(html, max_width=300)


    fl.Marker(wifi_position, popup, icon=fl.Icon(icon="wifi", prefix="fa")).add_to(marker_cluster)

mp.save(IMAGES_DIR / "Zonas_wifi_bucaramanga_html.html")


