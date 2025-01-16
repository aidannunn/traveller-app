import UWPClass as UWC

class Planet:

    def __init__(self, Name, UWPString, Bases, TradeCodes, TravelZone):
        self.Name = Name
        self.UWPObject = UWC.UWP(UWPString)
        self.Bases = Bases
        self.TradeCodes = TradeCodes
        self.TravelZone = TravelZone

