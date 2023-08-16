import sqlite3

class DatabaseManager:
    def __init__(self, database_name):
        self.database_name = database_name
        self.conn = sqlite3.connect(database_name)

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        self.execute_query(query)

    def execute_query(self, query, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        self.conn.commit()
        cursor.close()

    def fetch_data(self, query, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        return data

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    database_name = "../data/backup/data.db"
    db_manager = DatabaseManager(database_name)

    table_name = "csv_data"
    columns = ["Name TEXT", "Num INTEGER"]
    db_manager.create_table(table_name, columns)

    query = "SELECT * FROM csv_data"
    data = db_manager.fetch_data(query)
    print(data)

    db_manager.close_connection()
