import csv
import pymysql

def process_csv_to_database(csv_file, database_name):
    try:
        # Connect to the database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='ETLdb'
        )

        cursor = connection.cursor()

        # Create the table if it doesn't exist
        cursor.execute("CREATE TABLE IF NOT EXISTS episodes (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255) NOT NULL, painting_date VARCHAR(255) NOT NULL);")
        connection.commit()

        with open(csv_file, 'r') as epifile:
            csv_reader = list(csv.reader(epifile))
            first_row = 0
            for row in csv_reader:
                if first_row == 0:
                    first_row += 1
                else:
                    title = row[0]
                    painting_date = row[1]
                    cursor.execute("INSERT INTO episodes (title, painting_date) VALUES (%s, %s)", (title, painting_date))
    
        connection.commit()

    except pymysql.Error as e:
        print("Error:", e)
    finally:
        connection.close()

process_csv_to_database('JOP_EpisodeDates.csv', 'ETLdb')