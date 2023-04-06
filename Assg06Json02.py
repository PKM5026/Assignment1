import json
class Employee:
    def _init_(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

    def _str_(self):
        return f"Name: {self.name}, dob: {self.dob}, Height: {self.height}, City: {self.city}, State: {self.state}"

# Read employee information from JSON file
with open("employee.json", "r") as f:
    data = json.load(f)

# Create list of Employee objects
employees = []
for emp in data["employees"]:
    emp_obj = Employee(emp["name"], emp["dob"], emp["height"], emp["city"], emp["state"])
    employees.append(emp_obj)

# Print list of Employee objects
for emp in employees:
    print(emp)