import streamlit as st
from app.employee_manager import EmployeeManager

from app.utils.auth_utils import verify_api_key


# logic to verify API key (PIN) for Streamlit app and authenticate verification
import streamlit as st
from dotenv import load_dotenv
import os
from app.employee_manager import EmployeeManager  # example import

load_dotenv()

def authenticate_user():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.title("🔐 Secure Access - Employee Tracker")
        pin_input = st.text_input("Enter PIN", type="password")
        correct_pin = os.getenv("APP_PIN")

        if st.button("Login"):
            if pin_input == correct_pin:
                st.session_state.authenticated = True
                st.success("✅ Access Granted")
            else:
                st.error("❌ Incorrect PIN")
        st.stop()

# 🚨 Call before app content
authenticate_user()

# Then continue with your app logic
# Title
st.title("👨‍💼 Employee Tracker - Dashboard")

# Initialize the manager
manager = EmployeeManager()


# ------------------------
# MAIN STREAMLIT LOGIC
# ------------------------

# Sidebar navigation
menu = ["🏠 Home", "➕ Add Employee", "📅 Mark Attendance", "📈 Add Performance", "👁️ View Employee", "✏️ Update Employee"]
choice = st.sidebar.selectbox("Navigation", menu)


#breaking down each menu block's
if choice == "🏠 Home":
    st.subheader("Welcome to the Employee Attendance & Performance Tracker!")

# Add Employee
elif choice == "➕ Add Employee":
    st.subheader("Add New Employee")

    emp_id = st.text_input("Employee ID")
    name = st.text_input("Full Name")
    department = st.text_input("Department")

    if st.button("Add Employee"):
        success = manager.add_employee(emp_id, name, department)
        if success:
            st.success(f"Employee {name} added successfully!")
        else:
            st.error("Employee already exists or invalid input.")

# Mark Employee Attendance
elif choice == "📅 Mark Attendance":
    st.subheader("Mark Employee Attendance")

    if not manager.employees:
        st.warning("⚠️ No employees found. Please add employees first.")
    else:
        #getting all emp_id and presenting as list from which user can select 1 and mark attendance 
        emp_ids = list(manager.employees.keys())
        selected_emp = st.selectbox("Select Employee ID", emp_ids)

        if st.button("✅ Mark Attendance"):
            success = manager.mark_attendance(selected_emp)
            if success:
                st.success(f"Attendance marked for employee {selected_emp}")
            else:
                st.error("Failed to mark attendance.")


# Mark Employee Performance
elif choice == "📈 Add Performance":
    st.subheader("Employee Performance Review")

    if not manager.employees:
        st.warning("⚠️ No employees found. Please add employees first.")
    else:
        #getting all emp_id and presenting as list from which user can select 1 and mark attendance 
        emp_ids = list(manager.employees.keys())
        selected_emp = st.selectbox("Select Employee ID", emp_ids)

        comment = st.text_area("Performance Review")

        if st.button("📝 Add Review"):
            if comment.strip() == "":
                st.error("⚠️ Comment cannot be empty.")
            else:
                success = manager.add_performance_review(selected_emp, comment.strip())
                if success:
                    st.success(f"Performance review added for employee {selected_emp}")
                else:
                    st.error("Failed to add performance review.")


# View Employee Deatails that ask user All Employees or Specific Employee by emp_id
elif choice == "👁️ View Employee":
    st.subheader("View Employee Details")

    if not manager.employees:
        st.warning("⚠️ No employees found. Please add employees first.")
    else:
        view_choice = st.selectbox("View Options", ["All Employees", "Specific Employee"])

        if view_choice == "All Employees":
            st.write("### 👥 All Employees")
            for emp_id, emp in manager.employees.items():
                st.markdown(f"**🆔 ID:** {emp.emp_id}")
                st.write(f"👤 **Name:** {emp.name}")
                st.write(f"🏢 **Department:** {emp.department}")
                st.write(f"🕒 **Attendance Count:** {len(emp.attendance)}")
                st.write("📈 **Performance Reviews:**")
                if emp.performance:
                    for review in emp.performance:
                        st.markdown(f"- _{review['date']}_: {review['comment']}")
                else:
                    st.info("No reviews yet.")
                st.markdown("---")

        elif view_choice == "Specific Employee":
            emp_ids = list(manager.employees.keys())
            selected_emp = st.selectbox("Select Employee ID", emp_ids)

            if selected_emp:
                emp = manager.employees[selected_emp]
                st.markdown(f"### 🔍 Details for **{emp.name}**")
                st.write(f"🆔 **ID:** {emp.emp_id}")
                st.write(f"🏢 **Department:** {emp.department}")
                st.write(f"🕒 **Attendance Count:** {len(emp.attendance)}")

                st.write("📈 **Performance Reviews:**")
                if emp.performance:
                    for review in emp.performance:
                        st.markdown(f"- _{review['date']}_: {review['comment']}")
                else:
                    st.info("No reviews yet.")


# Update Employee Details   
elif choice == "✏️ Update Employee":
    st.subheader("Update Employee Details")

    if not manager.employees:
        st.warning("⚠️ No employees found. Please add employees first.")
    else:
        emp_ids = list(manager.employees.keys())
        selected_emp = st.selectbox("Select Employee ID", emp_ids)

        if selected_emp:
            emp = manager.employees[selected_emp]
            name = st.text_input("Full Name", value=emp.name)
            department = st.text_input("Department", value=emp.department)

            if st.button("Update Employee"):
                success = manager.update_employee(selected_emp, name, department)
                if success:
                    st.success(f"Employee {selected_emp} updated successfully!")
                else:
                    st.error("Failed to update employee details.")


