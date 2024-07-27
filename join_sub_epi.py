#!/usr/bin/env python3
# Fetch data from CSV file
# Add data to a list
# Insert the list data into a MySQL database
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

    with open('JOP_SubjectMatter.csv', 'r') as sub_file:
        sub_reader = list(csv.reader(sub_file))
        first_row = 0
        for sub_row in sub_reader:
            if first_row == 0:
                first_row = 1
                continue

            title = sub_row[1].lower()
            print("title:", title)
            cursor.execute("SELECT id FROM episodes WHERE lower(episodes.title) = %s", (title,))
            episode_id = cursor.fetchone()
            if episode_id is not None:
                epi_iid = episode_id[0]
            # print("type of episode_id:", type(episode_id), "epi_iid:", type(epi_iid))
            # i = 2
            # while i < 67 + 2:
            #     # print(f"sub_row[{i}] is {sub_row[i]}")
            #     if (sub_row[i] == "1"):
            #         sub_id = int(i - 1)
            #         # print("type of sub_id:", type(sub_id))
            #         try:
            #             cursor.execute("INSERT INTO epi_sub (epi_id, sub_id) VALUES (%d, %d)", (epi_iid, sub_id))
            #             connection.commit()
            #         except pymysql.Error as e:
            #             print(f"Error inserting data: {e}")
            #     i += 1
            sql = "INSERT IGNORE INTO epi_sub (epi_id, sub_id) VALUES (%s, %s)"
            # Insert data using prepared statement
            for i in range(2, 68):
                if sub_row[i] == '1':
                    sub_id = i - 1
                    print(f"sub_row[{i}] is {sub_row[i]}, sub_id: {sub_id}")
                    # print("sub_id:", sub_id)
                    cursor.execute(sql, (epi_iid, sub_id))
                    connection.commit()

except pymysql.Error as e:
    print("Error:", e)
finally:
    connection.close()
