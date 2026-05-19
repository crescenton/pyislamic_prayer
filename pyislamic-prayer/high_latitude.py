def night_portion(angle):
    return angle / 60

def adjust_fajr(fajr, sunrise, portion):
    if fajr > sunrise - portion:
        return sunrise - portion
    return fajr

def adjust_isha(isha, sunset, portion):
    if isha < sunset + portion:
        return sunset + portion
    return isha