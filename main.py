from src.extract import extract_from_source
from src.transform import clean_data
from src.load import load_to_database


def main():
    df = extract_from_source("https://www.datos.gov.co/resource/SERVICIO-DE-CONECTIVIDAD-ZONA-WIFi.json")

    df = clean_data(df, "latitud")
    df = clean_data(df, "longitud")

    load_to_database(df)

if __name__ == "__main__":
    main()