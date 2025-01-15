import unittest
from UWPCalc.PlanetAPI import PlanetAPI


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.planetApi_obj = PlanetAPI()

    def test(self):
        print('Running PlanetTestRunner')
        print('PlanetAPI: ', self.planetApi_obj.Planets.items())





if __name__ == '__main__':
    unittest.main()