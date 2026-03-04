
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import mplcursors
from src.database import get_connection
from src.paths import IMAGES_DIR

def get_data():
    conn = get_connection()
    query = 'SELECT * FROM zonas_wifi_bucaramanga;'

    df = pd.read_sql(query, conn)

    conn.close()

    return df

df = get_data()

gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df['longitud'], df['latitud']), crs="EPSG:4326")

gdf = gdf.to_crs(epsg=3857)


fig, ax = plt.subplots(figsize=(7, 10), dpi=80)
sc = ax.scatter(gdf.geometry.x, gdf.geometry.y, s=40)

cursor = mplcursors.cursor(sc, hover=True)

@cursor.connect("add")
def on_add(sel):
    idx = sel.index
    sel.annotation.set_text(
        f"{gdf.iloc[idx]['nombre_zona_wifi']}\n"
        f"{gdf.iloc[idx]['barrio']}\n"
        f"{gdf.iloc[idx]['comuna']}"
    )


ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)

fig.suptitle(r'Mapa de las zonas Wifi en Bucaramanga', fontsize=16, fontweight='bold')
ax.set_axis_off()
plt.savefig(IMAGES_DIR / "Zonas_wifi_bucaramanga_png", dpi=300)
plt.show()


