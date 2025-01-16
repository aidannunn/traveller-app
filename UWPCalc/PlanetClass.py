import UWPClass

class Planet:

    def __init__(self, Name, UWPString, Bases, TradeCodes, TravelZone):
        self.Name = Name
        self.UWPObject = UWPClass.UWP(UWPString)
        self.Bases = Bases
        self.TradeCodes = TradeCodes
        self.TravelZone = TravelZone

