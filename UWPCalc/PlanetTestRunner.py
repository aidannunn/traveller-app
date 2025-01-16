import unittest
from UWPCalc.PlanetAPI import PlanetAPI


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.planetApi_obj = PlanetAPI()

    def test_getPlanets(self):
        print('PlanetAPI: ', self.planetApi_obj.Planets.items())


    def test_getPlanetByName(self):
        print('PlanetAPI return from Corgi: ', self.planetApi_obj.Planets["Corgi"])

    def test_getUWPCodeFromPlanet(self):
        print('Return UWP code from Planet: ', self.planetApi_obj.Planets["Corgi"].UWPObject.UWPString)
        print('Return Starport code from Planet: ', self.planetApi_obj.Planets["Corgi"].UWPObject.Starport)
        print('Return UWP description from Planet: ', self.planetApi_obj.Planets["Corgi"].UWPObject.get_starport_description())

if __name__ == '__main__':
    unittest.main()