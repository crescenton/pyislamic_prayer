class Method:
    def __init__(self, fajr, isha):
        self.fajr = fajr
        self.isha = isha

MWL = Method(18, 17)
EGYPT = Method(19.5, 17.5)
KARACHI = Method(18, 18)
UMM_AL_QURA = Method(18.5, None)  # Isha = Maghrib + 90 min