#!/usr/bin/env python3
# Fetch data from CSV file
# Add data to a list
# Insert list data into a MySQL database
import csv
import MySQLdb

# Connect to the MySQLdb
connection = MySQLdb.connect(host='localhost', user='root', password='root',)
    
# Create a cursor object
if connection.is_connect():
    cursor = connection.cursor()
    cursor.execute("CREATE DATABASE ETL IF NOT EXISTS")
    print("Dababase ETL is created")
else:
    print("Error while connecting to MySQL")
    
# Open the CSV file
with open('JOP_ColorsUsed.csv', 'r') as csvfile:
    # Create a CSV reader object
    csv_reader = csv.reader(csvfile)
    
    # Iterate over the rows of the CSV file
    