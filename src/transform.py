import re

def coord_to_decimal(coord: str):
    pattern = r"(\d+)°\s*(\d+)'\s*(\d+(?:\.\d+)?)\"([NSEO])"
    coordinate = re.match(pattern, coord)
    if coordinate is not None:
        degrees = float(coordinate.group(1))
        minutes = float(coordinate.group(2))
        seconds = float(coordinate.group(3))
        direction = coordinate.group(4)

        decimals = degrees + minutes/60 + seconds/3600

        if direction in ['S', 'O']:
            decimals *= -1
    else: 
        decimals = "NaN"
    return decimals

def clean_data(df, coord: str):
    df[coord] = df[coord].apply(coord_to_decimal)
    df = df.loc[~(df['longitud'] == "NaN")]
    return df