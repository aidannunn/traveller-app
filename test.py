import unittest
from unittest import mock
import trade_tables
from trade_tables import *


class TestTablesMethods(unittest.TestCase):
    def setUp(self):
        self.tables_obj = Tables()

    def test_value_table_freight(self):
        parsecs_input_array = [1, 2, 3, 4, 5, 6]
        expected_values_array = [1000, 1600, 2600, 4400, 8500, 32000]
        actual_values_array = []

        for distance in parsecs_input_array:
            actual_values_array.append(
                self.tables_obj.passage_and_freight_value_table(distance, 1, 0, 0)
            )

        self.assertEqual(expected_values_array, actual_values_array)

    def test_value_table_passage(self):
        parsecs_input_array = [1, 2, 3, 4, 5, 6]
        passage_quality_input_array = [0, 1, 2, 3]
        expected_values_array = [
            9000,
            6500,
            2000,
            700,
            14000,
            10000,
            3000,
            1300,
            21000,
            14000,
            5000,
            2200,
            34000,
            23000,
            8000,
            3900,
            60000,
            40000,
            14000,
            7200,
            210000,
            130000,
            55000,
            27000,
        ]
        actual_values_array = []

        for distance in parsecs_input_array:
            for quality in passage_quality_input_array:
                actual_values_array.append(
                    self.tables_obj.passage_and_freight_value_table(
                        distance, 0, quality, 1
                    )
                )
        self.assertEqual(expected_values_array, actual_values_array)
