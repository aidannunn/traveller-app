import xml.etree.ElementTree as ET
import PlanetClass


class PlanetAPI:

    def __init__(self):
        self.Planets = self.PopulatePlanetDictionaryFromXML()


    def PopulatePlanetDictionaryFromXML(self):
        tree = ET.parse("item.xml")
        root = tree.getroot()
        output = {}

        for item in root.findall('Planet'):

            new_planet = PlanetClass.Planet(item.find('Name').text,
                                item.find("UWP").text,
                                item.find("Bases").text,
                                item.find("TradeCodes").text.split(',').copy(),
                                item.find("TravelZone").text)
            output.update({new_planet.Name: new_planet})

        return output


