# Data-Engineer

# NodeB Data Ingestion

This project parses and loads NodeB data into a PostgreSQL database.

## Folder Structure
project_root/
│
├── data/
│ └── raw_data.txt # Your raw data file
│
├── sql/
│ └── create_table.sql # SQL DDL file for table creation
│
├── config/
│ └── db_config.py # Configuration file for database connection details
│
│─── load_data.py # Python script for parsing and loading data
|
└── README.md # Project description and instructions


## Setup

1. **Database Configuration:**
   - Update `config/db_config.py` with your actual PostgreSQL connection details.

2. **Create Database Table:**
   - Run the SQL script in `sql/create_table.sql` to create the `NodeB_Data` table in your PostgreSQL database.

3. **Load Data:**
   - Place your raw data file in the `data` directory.
   - Run the Python script in `src/load_data.py` to parse the data and insert it into the database.

## Running the Script

```bash
python src/load_data.py


This folder structure ensures that your project is organized and easy to manage. Each component is separated into its own directory, making it easier to maintain and understand.
