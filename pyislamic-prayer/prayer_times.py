import math
from datetime import date
from .astronomy import *
from .madhab import Madhab
from .high_latitude import *
from .methods import *

class PrayerTimes:
    def __init__(self, lat, lon, tz, madhab=Madhab.SHAFI, method=MWL):
        self.lat = deg2rad(lat)
        self.lon = lon
        self.tz = tz
        self.madhab = madhab
        self.method = method

    def _hour_angle(self, angle, decl):
        x = (
            (math.sin(angle) - math.sin(self.lat) * math.sin(decl)) /
            (math.cos(self.lat) * math.cos(decl))
        )
        x = max(-1, min(1, x))  # Clamp to avoid math domain error
        return math.acos(x)

    def calculate(self, d=date.today()):
        j = julian(d)
        decl = declination(j)
        eqt = equation(j)

        noon = 12 + self.tz - self.lon / 15 - eqt / 60

        # Core times
        fajr = noon - rad2deg(self._hour_angle(deg2rad(-self.method.fajr), decl)) / 15
        SUN_ANGLE = deg2rad(-0.833 - 0.0347 * math.sqrt(self.lat * 180 / math.pi))

        sunrise = noon - rad2deg(self._hour_angle(SUN_ANGLE, decl)) / 15
        sunset  = noon + rad2deg(self._hour_angle(SUN_ANGLE, decl)) / 15
        dhuhr = noon + (2 / 60)

        # ✅  ASR 
        shadow = self.madhab.value
        angle = math.atan(1 / (shadow + math.tan(abs(self.lat - decl))))
        asr = noon + rad2deg(self._hour_angle(angle, decl)) / 15

        # Isha
        if self.method.isha:
            isha = noon + rad2deg(self._hour_angle(deg2rad(-self.method.isha), decl)) / 15
        else:
            isha = sunset + (90 / 60)  # 90 minutes (Umm al-Qura)

        # ✅ HIGH LATITUDE ADJUSTMENT
        night = sunset - sunrise

        fajr_portion = night_portion(self.method.fajr)
        isha_portion = night_portion(self.method.isha if self.method.isha else 18)

        fajr = adjust_fajr(fajr, sunrise, fajr_portion)
        isha = adjust_isha(isha, sunset, isha_portion)

        return {
            "Fajr": self._fmt(fajr),
            "Sunrise": self._fmt(sunrise),
            "Dhuhr": self._fmt(dhuhr),
            "Asr": self._fmt(asr),
            "Maghrib": self._fmt(sunset),
            "Isha": self._fmt(isha)
        }

    def _fix_time(self, t):
        while t < 0:
            t += 24
        while t >= 24:
            t -= 24
        return t

    def _fmt(self, t):
        t = self._fix_time(t)
        h = int(t)
        m = int(round((t - h) * 60))

        if m == 60:
            h += 1
            m = 0
        return f"{h:02d}:{m:02d}"