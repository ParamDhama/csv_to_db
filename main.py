import configparser
import os
from src import converter, database

def main():
    # Load configuration from config.ini
    config = configparser.ConfigParser()
    config.read("config/config.ini")
    database_name = os.path.abspath(config["Database"]["database_name"])

    # Paths for CSV and database
    csv_file = "data/data.csv"
    table_name = "csv_data"

    # Create a database manager instance
    db_manager = database.DatabaseManager(database_name)

    # Convert CSV to database
    print("Converting CSV to database...")
    converter.csv_to_database(csv_file, database_name, table_name)
    print(f"CSV data successfully converted and stored in {database_name}.{table_name}")

    # Fetch and display data from the database
    print("\nFetching data from the database:")
    query = f"SELECT * FROM {table_name}"
    data = db_manager.fetch_data(query)
    for row in data:
        print(row)

    # Close the database connection
    db_manager.close_connection()

if __name__ == "__main__":
    main()
    print("hello")
