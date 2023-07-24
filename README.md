# flask_student_api

This is a simple Flask API for managing student data using a MySQL database. It provides endpoints to perform CRUD operations on student records.
Installation
Clone the repository: git clone https://github.com/your_username/flask-student-api.git
Change to the project directory: cd flask-student-api
Install dependencies: pip install -r requirements.txt
Set up the MySQL database and update db_config in app.py.
Run the server: python app.py
Usage
GET /students: Get all students.
GET /students/<int:id>: Get a specific student by ID.
POST /students: Add a new student.
PUT /students/<int:id>: Update a student by ID.
DELETE /students/<int:id>: Delete a student by ID.
Example Requests
Get all students: curl -X GET http://localhost:5000/students
Get a student by ID: curl -X GET http://localhost:5000/students/<id>
Add a new student: curl -X POST -H "Content-Type: application/json" -d '{"name":"John","age":20,"course":"CS"}' http://localhost:5000/students
Update a student: curl -X PUT -H "Content-Type: application/json" -d '{"name":"Updated","age":22,"course":"Math"}' http://localhost:5000/students/<id>
Delete a student: curl -X DELETE http://localhost:5000/students/<id>
Note: This API is for educational purposes and not for production use. Secure your database credentials before deployment.

