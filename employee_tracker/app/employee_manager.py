import json, os
from datetime import datetime
from app.models.employee import Employee

class EmployeeManager :

    def __init__(self, storage_file = "app/storage.json"):
        self.storage_file = storage_file
        self.employees = self.load_empData_fromStorage()

    def load_empData_fromStorage(self):
        if os.path.exists(self.storage_file):
            try :
                with open(self.storage_file, 'r') as f:
                    data = json.load(f)
                    return {
                        emp_id : Employee.from_dict(emp_id, data)
                        for emp_id, data in data.items()
                    }
            except json.JSONDecodeError:
                return {}
        return {}
        
    def save_empData__toStorage(self):
        try:
            data = {emp_id : emp.to_dict() for emp_id, emp in self.employees.items()}

            with open(self.storage_file, 'w') as f:
                json.dump(data, f, indent=4)
                print("Employee saved successfully to file.")

        except Exception as e:
            print(f"Failed to save Employee: {e}")




    # ------------------ ACTUAL LOGIC STARTS ---------------
    #1. add employee
    def add_employee(self, emp_id, name, department):

        #checking empi_id should be unique
        if emp_id in self.employees:
            print(f"Employee {emp_id} already exists")
            return False
        
        #validating emp_id format
        if not Employee.validateEmp(emp_id):
            print("Invalid Employee ID entered. It must start with 'E' and be AlphaNumeric")
            return False
        
        #creating instance and adding
        emp = Employee(emp_id, name, department)
        self.employees[emp_id] = emp    

        print(f"Employee Added {emp_id}")
        self.save_empData__toStorage()
        
        return True


    #2. Add attendance for employee that exists and save to storage
    def mark_attendance(self, emp_id):
        if emp_id not in self.employees:
            print(f"Employee {emp_id} does not exist")
            return False
        
        emp = self.employees[emp_id]
        emp.mark_attendance()
        self.save_empData__toStorage()
        
        print(f"Attendance marked for {emp_id}")
        return True
    
    #3. Add performance review for employee that exists and save to storage
    def add_performance_review(self, emp_id, comment):
        emp = self.employees[emp_id]

        if not emp:
            print(f"Employee {emp_id} does not exist")
            return False
        
        
        emp.add_performance(comment)
        self.save_empData__toStorage()
        
        print(f"Performance review added for {emp_id}")
        return True
    
    #4. Get all employee details
    def get_all_employees(self):
        return {emp_id: emp.to_dict() for emp_id, emp in self.employees.items()}
    
    #5. Get employee details by ID
    def get_employee_by_id(self, emp_id):
        emp = self.employees[emp_id]
        if not emp:
            print(f"Employee {emp_id} does not exist")
            return None
        
        return self.employees[emp_id].to_dict()
        





    