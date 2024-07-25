import pymysql

def create_db_if_not_exists():
    """Creates a database and a table if it doesn't exist."""
    try:
        # Connect to the MySQL server without specifying the database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root'
        )

        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ETLdb;")
        connection.commit()
    except pymysql.Error as e:
        print("Error creating database:", e)
    finally:
        connection.close()
