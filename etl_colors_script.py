#!/usr/bin/env python3
# Fetch data from CSV file
# Add data to an array
# Insert the array data into a MySQL database
import csv
import pymysql

try:   
    # connect to the database
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='ETLdb'
    )
    # Open the CSV ColorsUsed file
    with open('JOP_ColorsUsed.csv', 'r') as color_file:
        color_reader = list(csv.reader(color_file))
        row = color_reader[0]
    
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS colors (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(30) NOT NULL)")
    connection.commit()
    i = 10
    length = len(row)
    sql = f'INSERT INTO colors (name) VALUES (%s)'
    while i < length:
        cursor.execute(sql, (row[i]))
        i += 1
    connection.commit()
        
except pymysql.Error as e:
    print("Error:", e)
finally:
    connection.close()
            