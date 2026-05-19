import math

def qibla_direction(lat, lon):
    kaaba_lat = math.radians(21.4225)
    kaaba_lon = math.radians(39.8262)

    lat = math.radians(lat)
    lon = math.radians(lon)

    dlon = kaaba_lon - lon

    angle = math.atan2(
        math.sin(dlon),
        math.cos(lat)*math.tan(kaaba_lat) - math.sin(lat)*math.cos(dlon)
    )

    return (math.degrees(angle) + 360) % 360