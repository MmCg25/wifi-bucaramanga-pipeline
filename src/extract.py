import requests
import json
import pandas as pd
from pathlib import Path
from datetime import datetime
from src.paths import RAW_DIR


def extract_from_source(url: str):
    response = requests.get(url)
    data = response.json()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = RAW_DIR / f"Wifi_Zones_{timestamp}.json"
    
    with open(filepath, "w") as f:
        json.dump(data, f, indent = 4)
    
    df = pd.json_normalize(data)

    return df
