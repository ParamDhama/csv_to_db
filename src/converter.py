import sqlite3
import pandas as pd

def csv_to_database(csv_file, database_name, table_name):
    df = pd.read_csv(csv_file)
    conn = sqlite3.connect(database_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

if __name__ == "__main__":
    csv_file = "../data/data.csv"
    database_name = "../data//backup/data.db"
    table_name = "csv_data"

    csv_to_database(csv_file, database_name, table_name)
    print(f"CSV data successfully converted and stored in {database_name}.{table_name}")
