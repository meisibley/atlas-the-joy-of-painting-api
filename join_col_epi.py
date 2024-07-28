#!/usr/bin/env python3
# Fetch color ids from JOP_ColorsUsed.csv for each id(painting title) and add them to a list
# Fetch episode id from episodes table where episode title equals this csv file's title
# Insert this episode id and its related color ids into MySQL table epi_col 
import csv
import pymysql

try:
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='ETLdb'
    )
    cursor = connection.cursor()

    with open('JOP_ColorsUsed.csv', 'r') as col_file:
        col_reader = list(csv.reader(col_file))
        first_row = 0
        for col_row in col_reader:
            if first_row == 0:
                first_row = 1
                continue

            title = col_row[3].lower()
            print("title:", title)
            cursor.execute("SELECT id FROM episodes WHERE lower(episodes.title) = %s", (title,))
            episode_id = cursor.fetchone()
            # void the first row
            if episode_id is not None:
                epi_iid = episode_id[0]

            # sql = "INSERT IGNORE INTO epi_col (epi_id, col_id) VALUES (%s, %s)"
            # Insert data using prepared statement
            for i in range(10, 28):
                if col_row[i] == '1':
                    col_id = i
                    print(f"epi_iid is {epi_iid}, col_row[{i}] is {col_row[i]}, col_id: {col_id}")
                    try:
                        # cursor.execute(sql, (epi_iid, col_id))
                        cursor.execute("INSERT IGNORE INTO epi_col (epi_id, col_id) VALUES (%s, %s)", (epi_iid, col_id))
                        connection.commit()
                    except pymysql.Error as e:
                        print(f"Error inserting data: {e}, epi_iid is {epi_iid}, col_id: {col_id}")

except pymysql.Error as e:
    print("Error:", e)
finally:
    connection.close()
