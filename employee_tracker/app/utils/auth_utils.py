from dotenv import load_dotenv
import getpass, os

load_dotenv()

def verify_pin():
    stored_pin = os.getenv("APP_PIN")

    if not stored_pin:
        print("❌ Environment variable 'APP_PIN' not found.")
        return False

    user_input = getpass.getpass("🔐 Enter PIN to access Employee Tracker: ")

    if user_input == stored_pin:
        print("✅ Access granted.\n")
        return True
    else:
        print("❌ Invalid PIN. Access denied.")
        return False
