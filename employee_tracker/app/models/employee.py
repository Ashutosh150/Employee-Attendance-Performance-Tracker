from datetime import datetime

class Employee:

    def __init__(self, emp_id, name, department):
        
        if not self.validateEmp(emp_id):
            raise ValueError("Invalid Employee ID entered. It must start with 'E' and be AlphaNumeric")
        
        self.emp_id = emp_id
        self.name = name.title()
        self.department = department
        self.attendance = []
        self.performance = []


    @staticmethod
    def validateEmp(emp_id) :
        return emp_id.isalnum() and emp_id.startswith("E")

    #appending attedance on daily basics
    def mark_attendance(self):
        self.attendance.append(str(datetime.now()))

    def add_performance(self, comment):
        self.performance.append({
            "comment" : comment,
            "date" : str(datetime.now())
        })

    def to_dict(self):
        return {
            "name" : self.name,
            "department" : self.department,
            "attendance" : self.attendance,
            "performance" : self.performance
        }
    
    @classmethod
    def from_dict(cls, emp_id, data) : 
        obj = cls(emp_id, data["name"], data["department"])
        obj.attendance = data.get("attendance", [])
        obj.performance = data.get("performance", [])
        return obj
    
    def __str__(self):
        return f"{self.name} | Department : {self.department} | Attendance : {len(self.attendance)} days | Review : {len(self.performance)}"