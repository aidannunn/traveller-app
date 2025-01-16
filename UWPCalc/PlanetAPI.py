from enum import Enum
import xml.etree.ElementTree as ET


import PlanetClass



class PlanetAPI:
    Planets = {}


    def __init__(self):
        self.Planets = self.PopulatePlanetDictionaryFromXML()


    def PopulatePlanetDictionaryFromXML(self):
        tree = ET.parse("item.xml")
        root = tree.getroot()
        output = {}
        pc = PlanetClass

        for item in root.findall('Planet'):
            new_planet = (pc.make_planet(item.find('Name').text,
                                         item.find("UWP").text,
                                         item.find("Bases").text,
                                         item.find("TradeCodes").text.split(',').copy(),
                                         item.find("TravelZone").text))
            output.update({new_planet.Name: new_planet})
        return output


    def uwpTranslator(self, uwpcode):
        print(uwpcode)


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

    def UWPLookupTable(self, uwpcode):
        print("UWPLookupTable")


class LetterToNumber(Enum):
    A = 10
    B = 11
    C = 12
    D = 13
    E = 14
    F = 15
    X = 0