from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",  
    "password": "XXXXXXXXX", 
    "database": "flask_app_db",  
}

# Connect to MySQL
def get_db_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Database Connection Error: {err}")
        return None

#  READ - Get All Employees(GET)
@app.route("/employees", methods=["GET"])
def get_employees():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(employees), 200
# CREATE - Add New Employee(POST)
@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.json
    name = data.get("name")
    salary = data.get("salary")
    date_of_join = data.get("date_of_join")

    if not name or not salary or not date_of_join:
        return jsonify({"error": "Missing required fields"}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor()
    query = "INSERT INTO employees (name, salary, date_of_join) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, salary, date_of_join))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Employee added successfully"}), 201

#  UPDATE - Modify Employee(PUT)
@app.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):
    data = request.json
    name = data.get("name")
    salary = data.get("salary")
    date_of_join = data.get("date_of_join")

    if not name and not salary and not date_of_join:
        return jsonify({"error": "No fields to update"}), 400
conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor()
    query = "UPDATE employees SET name=%s, salary=%s, date_of_join=%s WHERE id=%s"
    cursor.execute(query, (name, salary, date_of_join, id))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Employee updated successfully"}), 200

#  DELETE - Remove Employee(DELETE)
@app.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    cursor = conn.cursor()
    query = "DELETE FROM employees WHERE id=%s"
    cursor.execute(query, (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Employee deleted successfully"}), 200

# Run Flask App
if __name__ == "__main__":
    app.run(debug=True)
