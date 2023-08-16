# CSV to Database Conversion Project

Effortlessly convert CSV files into an SQLite database using Python. Streamline data storage and analysis with customizable settings.

## Features

- Convert CSV data to SQLite database
- Customize database settings in `config.ini`
- Fetch and display data from the database

## Usage

1. Place your CSV file in the `data/` directory.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the conversion: `python main.py`
4. Data is converted and ready for analysis.

## Configuration

Customize database name and more in `config.ini`.

## Future Enhancements

- Data validation and transformation
- User-friendly CLI/GUI
- Data visualization

csv_to_database_conversion/
│
├── data/
│   ├── data.csv
│   ├── backup/
│   │   ├── backup_data.db
│
├── config/
│   ├── config.ini
│
├── src/
│   ├── converter.py
│   ├── database.py
│
├── tests/
│   ├── test_converter.py
│   ├── test_database.py
│
├── main.py
├── requirements.txt
├── LICENSE
├── README.md

