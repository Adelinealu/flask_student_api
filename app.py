from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)
db_config = {
    'user': 'new_user',
    'password': 'new_password',
    'host': 'localhost',
    'database': 'students',
    'port': 3306,
}

db = mysql.connector.connect(**db_config)

# Rest of your code...


@app.route('/students', methods=['GET'])
def get_students():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students_table")
    students = cursor.fetchall()
    cursor.close()
    return jsonify(students)

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students_table WHERE id = %s", (id,))
    student = cursor.fetchone()
    cursor.close()
    return jsonify(student)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    name = data['name']
    age = data['age']
    course = data['course']
    cursor = db.cursor()
    cursor.execute("INSERT INTO students_table (name, age, course) VALUES (%s, %s, %s)", (name, age, course))
    db.commit()
    cursor.close()
    return jsonify({'message': 'Student added successfully'})

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    name = data['name']
    age = data['age']
    course = data['course']
    cursor = db.cursor()
    cursor.execute("UPDATE students_table SET name = %s, age = %s, course = %s WHERE id = %s", (name, age, course, id))
    db.commit()
    cursor.close()
    return jsonify({'message': 'Student updated successfully'})

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM students_table WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    return jsonify({'message': 'Student deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
