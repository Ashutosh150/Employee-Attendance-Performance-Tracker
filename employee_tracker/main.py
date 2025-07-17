from fastapi import FastAPI
from app.api.routes import router as employee_router

app = FastAPI(title="Employee Tracker API")

# Register all routes from routes.py
app.include_router(employee_router, prefix="/employees")