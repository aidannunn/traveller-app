import json
import re


class Tables:
    def __init__(self):
        self.passage_value_dict = {
            1: [9000, 6500, 2000, 700, 1000],
            2: [14000, 10000, 3000, 1300, 1600],
            3: [21000, 14000, 5000, 2200, 2600],
            4: [34000, 23000, 8000, 3900, 4400],
            5: [60000, 40000, 14000, 7200, 8500],
            6: [210000, 130000, 55000, 27000, 32000],
        }
        self.passenger_traffic_dict = {
            1: 0,
            2: 1,
            3: 1,
            4: 2,
            5: 2,
            6: 2,
            7: 3,
            8: 3,
            9: 3,
            10: 3,
            11: 4,
            12: 4,
            13: 4,
            14: 5,
            15: 5,
            16: 6,
            17: 7,
            18: 8,
            19: 9,
            20: 10,
        }
        self.freight_traffic_dict = {
            1: 0,
            2: 1,
            3: 1,
            4: 2,
            5: 2,
            6: 3,
            7: 3,
            8: 3,
            9: 4,
            10: 4,
            11: 4,
            12: 5,
            13: 5,
            14: 5,
            15: 6,
            16: 6,
            17: 7,
            18: 8,
            19: 9,
            20: 10,
        }

    def passage_and_freight_value_table(
        self, parsecs_travelled, freight, passage_quality, passenger
    ):
        if passenger:
            return self.passage_value_dict[parsecs_travelled][passage_quality]
        if freight:
            return self.passage_value_dict[parsecs_travelled][4]
        else:
            return 0
