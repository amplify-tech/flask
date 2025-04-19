from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory DB (for demo)
students = []

# Create
@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json()
    students.append(data)
    return jsonify({"message": "Student added"}), 201

# Read all
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

# Read one
@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    if student_id < 0 or student_id >= len(students):
        return jsonify({"error": "Student not found"}), 404
    return jsonify(students[student_id])

# Delete
@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    if student_id < 0 or student_id >= len(students):
        return jsonify({"error": "Student not found"}), 404
    students.pop(student_id)
    return jsonify({"message": "Student deleted"}), 200

# Health check
@app.route("/health", methods=["GET"])
def home():
    return "Flask Student API is running on port 8080 🚀", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
