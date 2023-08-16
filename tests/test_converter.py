import unittest
import os
from src import converter

class TestConverter(unittest.TestCase):

    def setUp(self):
        self.csv_file = "../data/data.csv"
        self.database_name = "../data/backup/test_data.db"
        self.table_name = "test_csv_data"

    def tearDown(self):
        if os.path.exists(self.database_name):
            os.remove(self.database_name)

    def test_csv_to_database(self):
        converter.csv_to_database(self.csv_file, self.database_name, self.table_name)
        self.assertTrue(os.path.exists(self.database_name))

if __name__ == "__main__":
    unittest.main()
