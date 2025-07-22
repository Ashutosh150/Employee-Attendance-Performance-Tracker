from dotenv import load_dotenv
import getpass, os

from fastapi import Header, HTTPException
import  streamlit as st     # ✅ Required only for Streamlit login 


load_dotenv()


#  without FastAPI
# def verify_pin():
#     stored_pin = os.getenv("APP_PIN")

#     if not stored_pin:
#         print("❌ Environment variable 'APP_PIN' not found.")
#         return False

#     user_input = getpass.getpass("🔐 Enter PIN to access Employee Tracker: ")

#     if user_input == stored_pin:
#         print("✅ Access granted.\n")
#         return True
#     else:
#         print("❌ Invalid PIN. Access denied.")
#         return False

stored_pin = os.getenv("APP_PIN")

# FastAPI-compatible PIN-based auth
def verify_api_key(x_api_key: str = Header(...)):
    if not stored_pin:
        raise HTTPException(status_code=500, detail="Server misconfiguration: APP_PIN missing")

    if x_api_key == stored_pin:
        raise HTTPException(status_code=403, detail="Access denied: Invalid API key")
    return True

 
