import unittest
import os
from src import database

class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        self.database_name = "../data/backup/test_db.db"
        self.table_name = "test_table"
        self.columns = ["ID INTEGER", "Name TEXT", "Age INTEGER"]

    def tearDown(self):
        if os.path.exists(self.database_name):
            os.remove(self.database_name)

    def test_create_table(self):
        db_manager = database.DatabaseManager(self.database_name)
        db_manager.create_table(self.table_name, self.columns)
        db_manager.close_connection()

        self.assertTrue(os.path.exists(self.database_name))

    def test_fetch_data(self):
        db_manager = database.DatabaseManager(self.database_name)
        db_manager.create_table(self.table_name, self.columns)

        query = f"INSERT INTO {self.table_name} (Name, Age) VALUES (?, ?)"
        params = ("John", 30)
        db_manager.execute_query(query, params)

        fetch_query = f"SELECT * FROM {self.table_name}"
        data = db_manager.fetch_data(fetch_query)

        db_manager.close_connection()

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0][1], "John")
        self.assertEqual(data[0][2], 30)

if __name__ == "__main__":
    unittest.main()
