from fastapi import FastAPI
from profile.student_router import router as student_router

app = FastAPI(title="Career LMS API")
app.include_router(student_router, prefix="/api")
