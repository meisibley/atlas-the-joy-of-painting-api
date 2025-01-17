from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql

try:
        # Connect to the database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='root',
            database='ETLdb'
        )
        cursor = connection.cursor()
except:
    print("Error: db connection error")

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Load environment variables (if using .env file)
app.config.from_object('config')  # Assuming a config.py file with environment variables

# app.register_blueprint(router)  # Register routes
@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello from Flask!'})

@app.route('/episodes', methods=['POST'])
def episodes():
    month = request.get_json().get("month")
    cursor.execute("SELECT * FROM episodes WHERE painting_date like '%" + month + "%';")
    episodes = cursor.fetchall()
    return jsonify(episodes)
    
@app.route('/subjects', methods=['POST'])
def subjects():
    title = request.get_json().get("subject")
    cursor.execute("SELECT episodes.id, episodes.title, subjects.subject \
        FROM episodes \
            INNER JOIN epi_sub ON epi_sub.epi_id = episodes.id \
                INNER JOIN subjects ON subjects.id = epi_sub.sub_id \
                    WHERE subjects.subject LIKE %s \
                        ORDER BY episodes.id ASC;", (title))   
    subjects = cursor.fetchall()
    return jsonify(subjects)

@app.route('/colors', methods=['POST'])
def colors():
    color = request.get_json().get("name")
    cursor.execute("SELECT colors.id, episodes.title, colors.name \
        FROM colors \
            INNER JOIN epi_col ON epi_col.col_id = colors.id \
                INNER JOIN episodes ON episodes.id = epi_col.epi_id \
                    WHERE colors.name LIKE %s \
                        ORDER BY episodes.id ASC;", (color))
    colors = cursor.fetchall()
    return jsonify(colors)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9002)