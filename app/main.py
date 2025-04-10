from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated DB
students = []

@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students), 200

@app.route("/students", methods=["POST"])
def add_student():
    data = request.json
    students.append(data)
    return jsonify({"message": "Student added"}), 201

@app.route("/students/<int:index>", methods=["PUT"])
def update_student(index):
    if index >= len(students):
        return jsonify({"error": "Student not found"}), 404
    students[index] = request.json
    return jsonify({"message": "Student updated"}), 200

@app.route("/students/<int:index>", methods=["DELETE"])
def delete_student(index):
    if index >= len(students):
        return jsonify({"error": "Student not found"}), 404
    students.pop(index)
    return jsonify({"message": "Student deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
