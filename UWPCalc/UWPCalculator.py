import unittest
from enum import Enum
import xml.etree.ElementTree as ET

class TestTablesMethods(unittest.TestCase):
    def setUp(self):
        self.UWPC_obj = UWPCalculator()

    def test(self):
        print(self.UWPC_obj.uwpTranslator())

    def test2(self):
        print(self.UWPC_obj.xmlReader())


class UWPCalculator:


    def xmlReader(self):
        tree = ET.parse("item.xml")
        root = tree.getroot()

        for planet in root.findall('Planet'):
            name = planet.find('Name').text
            UWP = planet.find('UWP').text
            tcodes = planet.find('TradeCodes').text


            print(f"Name: {name}, UWP: {UWP}, Trade Codes: {tcodes}")
            print("HI")



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