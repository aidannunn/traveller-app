from enum import Enum

class UWP:
    def __init__(self, UWPString):
        self.UWPString = UWPString
        self.Starport = UWPString[0]
        self.Size = UWPString[1]
        self.AtmosphereType = UWPString[2]
        self.HydroPercentage = UWPString[3]
        self.Population = UWPString[4]
        self.Government = UWPString[5]
        self.LawLevel = UWPString[6]
        self.TechLevel = UWPString[8]

        self.Tr = TranslationDictionaries

    def get_starport_description(self):
        if self.Tr.LetterToNumber[self.Starport] is not None:
            return self.Tr.StarportDescription[self.Tr.LetterToNumber[self.Starport].value]
        else:
            return self.Tr.StarportDescription[self.Starport]

    def get_size_description(self):
        return self.Size

    def get_tech_description(self):
        return self.TechLevel



class TranslationDictionaries:
    TradeCodes = {"Ag":"Agricultural",
                "As":"Astroid",
                "Ba":"Barren",
                "De":"Desert",
                "Fl":"Fluid Oceans",
                "Ga":"Garden",
                "Hi":"High Population",
                "Ht":"High Tech",
                "Ic":"Ice-Capped",
                "In":"Industrial",
                "Lo":"Low Population",
                "Lt":"Low Tech",
                "Na":"Non-Agricultural",
                "Ni":"Non-Industrial",
                "Po":"Poor",
                "Ri":"Rich",
                "Va":"Vacuum",
                "Wa":"Water World"
                }
    TravelZones = {"A": "Amber Zone",
                   "R": "Red Zone"
                   }
    StarportDescription = {0: "None",
                           1: "None",
                           2: "None",
                           3: "None",
                           4: "None",
                           5: "None",
                           6: "None",
                           7: "None",
                           8: "None",
                           9: "None",
                           10 : "Excellent",
                           11 : "Good",
                           12 : "Routine",
                           13 : "Poor",
                           14 : "Frontier"}

    SizeDescriptions = {"A": "Agricultural Size",}
    GravityDescriptions = {"A": "Agricultural Gravity",}
    AtmosphereDescriptions = {"A": "Astroid Atmosphere",}




    class LetterToNumber(Enum):
        A = 10
        B = 11
        C = 12
        D = 13
        E = 14
        F = 15
        X = 0