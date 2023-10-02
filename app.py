from flask import Flask, request, jsonify

app = Flask(__name__)


employees = [
    {"id": 1, "name": "John", "position": "Software Engineer"},
    {"id": 2, "name": "Alice", "position": "Data Analyst"},
    {"id": 3, "name": "Bob", "position": "Product Manager"},
]


@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    if "name" in data and "position" in data:
        new_employee = {
            "id": len(employees) + 1,
            "name": data["name"],
            "position": data["position"]
        }
        employees.append(new_employee)
        return jsonify({"message": "Employee created successfully"}), 201
    else:
        return jsonify({"error": "Name and position are required"}), 400


@app.route('/employees', methods=['GET'])
def get_employees():
    return jsonify({"employees": employees})


@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    employee = next((employee for employee in employees if employee["id"] == employee_id), None)
    if employee is not None:
        return jsonify(employee)
    else:
        return jsonify({"error": "Employee not found"}), 404


@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.get_json()
    employee = next((employee for employee in employees if employee["id"] == employee_id), None)
    if employee is not None:
        employee["name"] = data.get("name", employee["name"])
        employee["position"] = data.get("position", employee["position"])
        return jsonify({"message": "Employee updated successfully"})
    else:
        return jsonify({"error": "Employee not found"}), 404


@app.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    employee = next((employee for employee in employees if employee["id"] == employee_id), None)
    if employee is not None:
        employees.remove(employee)
        return jsonify({"message": "Employee deleted successfully"})
    else:
        return jsonify({"error": "Employee not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
