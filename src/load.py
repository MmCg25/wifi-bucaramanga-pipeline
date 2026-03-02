from src.database import get_connection

def load_to_database(df):
    conn = get_connection()
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO public.zonas_wifi_bucaramanga
            (nombre_zona_wifi, barrio, comuna, latitud, longitud)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            row['nombre_zona_wifi'],
            row['barrio'],
            row['comuna'],
            row['latitud'],
            row['longitud']
        ))

    conn.commit()
    cur.close()
    conn.close()