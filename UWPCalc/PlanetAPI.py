import xml.etree.ElementTree
from UWPCalc.PlanetClass import Planet
from pathlib import Path


class PlanetAPI:

    def __init__(self):
        self.database_path = Path(__file__).parent
        self.Planets = self.populate_planet_dictionary_from_xml()

    def populate_planet_dictionary_from_xml(self):
        tree = xml.etree.ElementTree.parse(self.database_path / "item.xml")
        root = tree.getroot()
        output = {}

        for item in root.findall("Planet"):

            new_planet = Planet(
                item.find("Name").text,
                item.find("UWP").text,
                item.find("Bases").text,
                item.find("TradeCodes").text.split(",").copy(),
                item.find("TravelZone").text,
            )
            output.update({new_planet.Name: new_planet})

        return output
