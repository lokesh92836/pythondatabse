from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
load_dotenv() 

from database import Base, engine
from routers import auth, students

import models.user     
import models.student  
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management API", version="1.0.0")

FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://frontend-one-sooty-87.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(students.router, prefix="/students", tags=["Students"])

@app.get("/")
def root():
    return {"message": "Student API is running"}

