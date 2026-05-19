from pyislamic_prayer import PrayerTimes, Madhab, KARACHI, qibla_direction

# 📍 Srinagar / Bandipora Coordinates
lat = 34.0837
lon = 74.7973
tz = 5.5  # IST

# 🕌 Karachi Method + Hanafi Madhab (closest to Rahemiyah base)
pt = PrayerTimes(
    lat=lat,
    lon=lon,
    tz=tz,
    madhab=Madhab.HANAFI,
    method=KARACHI
)

# 📊 Calculate prayer times
times = pt.calculate()

# 🖨️ Output
print("📍 Location: Srinagar / Bandipora")
print(f"Latitude: {lat}, Longitude: {lon}\n")

print("🕌 Prayer Times (Pure Calculation):")
for name, time in times.items():
    print(f"{name:8}: {time}")

print("\n🧭 Qibla Direction:")
print(f"{qibla_direction(lat, lon):.2f}° from North")