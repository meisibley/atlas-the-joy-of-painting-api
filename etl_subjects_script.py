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
    with open('JOP_SubjectMatter.csv', 'r') as subject_file:
        subject_reader = list(csv.reader(subject_file))
        row = subject_reader[0]
    
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS subjects (id INT AUTO_INCREMENT PRIMARY KEY, subject VARCHAR(30) NOT NULL)")
    connection.commit()
    i = 2
    length = len(row)
    sql = f'INSERT INTO subjects (subject) VALUES (%s)'
    while i < length:
        cursor.execute(sql, (row[i]))
        i += 1
    connection.commit()
    
except pymysql.Error as e:
    print("Error:", e)
finally:
    connection.close()
            