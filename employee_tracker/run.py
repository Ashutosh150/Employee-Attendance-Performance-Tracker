from venv import logger
from app.utils.auth_utils import verify_api_key
if not verify_api_key() :
    exit()

from app.employee_manager import EmployeeManager

manager = EmployeeManager()

# testing add_employee
#manager.add_employee("E003", "Nanu", "Pycho_Doc")

# testing mark_attendance
#manager.mark_attendance("E003")

# testing add_performance   
#manager.add_performance_review("E003", "Average Performance.")

# testing get_all_employees and display item using __str__ method
# all_employees = manager.get_all_employees()
# for emp_id, emp_data in all_employees.items():
#     print(f"ID: {emp_id}, Data: {emp_data}")

# testing get_employee_by_id
emp_data = manager.get_employee_by_id("E003")
#print(emp_data)


from app.utils.emailReport_utils import send_email_report
# Example usage of send_email_report
send_email_report("Test Subject", "This is a test email from Employee Tracker.")
logger.info("Test email sent successfully.")

