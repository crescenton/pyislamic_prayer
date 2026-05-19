from pyislamic_prayer import PrayerTimes, Madhab, KARACHI, qibla_direction

def test_prayer_times():
    lat = 34.0837
    lon = 74.7973
    tz = 5.5

    pt = PrayerTimes(
        lat=lat,
        lon=lon,
        tz=tz,
        madhab=Madhab.HANAFI,
        method=KARACHI
    )

    times = pt.calculate()

    print("🕌 Prayer Times Test")
    for k, v in times.items():
        print(k, ":", v)

    assert "Fajr" in times
    assert "Dhuhr" in times
    assert "Asr" in times

def test_qibla():
    direction = qibla_direction(34.0837, 74.7973)
    print("🧭 Qibla:", direction)
    assert isinstance(direction, (int, float))

if __name__ == "__main__":
    test_prayer_times()
    test_qibla()
    print("ALL TESTS PASSED ✔")
