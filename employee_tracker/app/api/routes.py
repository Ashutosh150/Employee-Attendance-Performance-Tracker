from fastapi import APIRouter, Depends, HTTPException
from app.employee_manager import EmployeeManager
from app.utils.auth_utils import verify_api_key


router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
    dependencies=[Depends(verify_api_key)]  # Applies to all endpoints inside
)
manager = EmployeeManager()
#-------

@router.get("/")
def get_all_employee():
    return manager.get_all_employees()
#-------

@router.get("/{emp_id}")
def get_emp_empID(emp_id : str):
    emp = manager.get_employee_by_id(emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp


from pydantic import BaseModel  #Pydantic model used to validate and parse incoming JSON.
#-------

# Define class request schema using Pydantic to take required input and parse as JSOn

class EmployeeCreateRequest(BaseModel):
    emp_id: str
    name: str
    department: str

@router.post("/addEmp")
def add_employee(req: EmployeeCreateRequest):
    success = manager.add_employee(req.emp_id, req.name, req.department)
    if not success:
        raise HTTPException(status_code=400, detail="Employee already exists")
    return {"message": f"Employee {req.emp_id} added successfully"}


@router.post("/{emp_id}/attendance")
def mark_attendance(emp_id: str):
    success = manager.mark_attendance(emp_id)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": f"Attendance marked for {emp_id}"}

#-------
class PerformanceRequest(BaseModel):
    comment: str

@router.post("/{emp_id}/performance")
def add_performance(emp_id: str, review: PerformanceRequest):
    success = manager.add_performance_review(emp_id, review.comment)
    if not success:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": f"Performance review added for {emp_id}"}



#---
class EmployeeUpdateRequest(BaseModel):
    name: str
    department: str

@router.put("/{emp_id}")
def update_employee(emp_id: str, data: EmployeeUpdateRequest):
    if emp_id not in manager.employees:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    emp = manager.employees[emp_id]
    emp.name = data.name.title()
    emp.department = data.department
    manager.save_empData__toStorage()

    return {"message": f"Employee {emp_id} updated successfully"}

#----
@router.delete("/{emp_id}")
def delete_employee(emp_id: str):
    if emp_id not in manager.employees:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    del manager.employees[emp_id]
    manager.save_empData__toStorage()
    
    return {"message": f"Employee {emp_id} deleted successfully"}


#----
# This endpoint is for uopdating the employee data as per update login from employee manager
@router.put("/{emp_id}/update")
def update_employee(emp_id: str, data: EmployeeUpdateRequest):
    if emp_id not in manager.employees:
        raise HTTPException(status_code=404, detail="Employee not found")

    emp = manager.employees[emp_id]
    emp.name = data.name.title()
    emp.department = data.department
    manager.save_empData__toStorage()

    return {"message": f"Employee {emp_id} updated successfully"}   