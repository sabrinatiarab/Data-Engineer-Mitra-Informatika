import mysql.connector
import sys
import os

# Add the directory containing 'config' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'config')))

from db_config import DB_CONFIG  # Import from the correct directory

# Database connection details
conn = mysql.connector.connect(
    database=DB_CONFIG['database'],
    user=DB_CONFIG['user'],
    password=DB_CONFIG['password'],
    host=DB_CONFIG['host'],
    port=DB_CONFIG['port']
)

cur = conn.cursor()

# Create table
try:
    with open(os.path.join(os.path.dirname(__file__), 'sql', 'create_table.sql'), 'r') as file:
        create_table_query = file.read()
    cur.execute(create_table_query)
    conn.commit()
except mysql.connector.Error as err:
    print(f"Error creating table: {err}")
    conn.rollback()

# Function to parse a line of data
def parse_line(line):
    key, value = line.split("=", 1)
    key = key.strip().replace(" ", "_")
    value = value.strip().replace("<NULL>", "None")
    if value in ["TRUE", "FALSE"]:
        value = value == "TRUE"
    return key, value

# Function to load data into the database
def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            data = {}
            for line in file:
                if line.strip() == "":
                    continue
                key, value = parse_line(line)
                data[key] = value

                if len(data) > 0 and "Administrative_State" in data:
                    cur.execute("""
                    INSERT INTO NodeB_Data (
                        NodeB_Name, NodeB_ID, Subrack_No, Subrack_Name, Slot_No, Subsystem_No,
                        IUB_Trans_Bearer_Type, IP_Trans_Apart_Ind, IUB_Trans_Delay, Satellite_Trans_Ind,
                        NodeB_Protocol_Version, Resource_Management_Mode, NodeB_Trace_Switch, NodeB_Host_Type,
                        Peer_RNC_ID, Peer_NodeB_ID, Sharing_Type_Of_NodeB, Cn_Operator_Index, DSS_NodeB_Flag,
                        Administrative_State
                    ) VALUES (
                        %(NodeB_Name)s, %(NodeB_ID)s, %(Subrack_No)s, %(Subrack_Name)s, %(Slot_No)s, %(Subsystem_No)s,
                        %(IUB_Trans_Bearer_Type)s, %(IP_Trans_Apart_Ind)s, %(IUB_Trans_Delay)s, %(Satellite_Trans_Ind)s,
                        %(NodeB_Protocol_Version)s, %(Resource_Management_Mode)s, %(NodeB_Trace_Switch)s, %(NodeB_Host_Type)s,
                        %(Peer_RNC_ID)s, %(Peer_NodeB_ID)s, %(Sharing_Type_Of_NodeB)s, %(Cn_Operator_Index)s, %(DSS_NodeB_Flag)s,
                        %(Administrative_State)s
                    );
                    """, data)
                    data = {}
        conn.commit()
    except mysql.connector.Error as err:
        print(f"Error loading data: {err}")
        conn.rollback()

# Path to your data file
file_path = os.path.join(os.path.dirname(__file__), 'data', 'DTE - Technical Test.txt')

# Load data into the database
load_data(file_path)

# Close the connection
cur.close()
conn.close()
print('Data successfully inserted and connection closed.')