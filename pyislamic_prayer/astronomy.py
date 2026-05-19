import math
from datetime import date

def deg2rad(d): return d * math.pi / 180
def rad2deg(r): return r * 180 / math.pi

def julian(d):
    return d.toordinal() + 1721424.5

def declination(j):
    n = j - 2451545.0
    g = deg2rad((357.529 + 0.98560028 * n) % 360)
    q = deg2rad((280.459 + 0.98564736 * n) % 360)

    L = q + deg2rad(1.915) * math.sin(g) + deg2rad(0.020) * math.sin(2 * g)

    e = deg2rad(23.439 - 0.00000036 * n)

    return math.asin(math.sin(e) * math.sin(L))

def equation(j):
    n = j - 2451545.0

    g = deg2rad((357.529 + 0.98560028 * n) % 360)
    q = deg2rad((280.459 + 0.98564736 * n) % 360)

    L = q + deg2rad(1.915) * math.sin(g) + deg2rad(0.020) * math.sin(2 * g)

    e = deg2rad(23.439 - 0.00000036 * n)

    ra = math.atan2(math.cos(e) * math.sin(L), math.cos(L))

    eqt = q - ra
    return rad2deg(eqt) * 4