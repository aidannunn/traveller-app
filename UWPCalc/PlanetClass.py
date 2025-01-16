class Planet(object):
    Name = ""
    UWP = ""
    Bases = ""
    TradeCodes = ()
    TravelZone = ""

    def __init__(self, Name, UWP, Bases, TradeCodes, TravelZone):
        self.Name = Name
        self.UWP = UWP
        self.Bases = Bases
        self.TradeCodes = TradeCodes
        self.TravelZone = TravelZone

def make_planet(Name, UWP, Bases, TradeCodes, TravelZone):
    Planet.Name = Name
    Planet.UWP = UWP
    Planet.Bases = Bases
    Planet.TradeCodes = TradeCodes
    Planet.TravelZone = TravelZone
    return Planet