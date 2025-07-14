from fastapi import APIRouter, HTTPException
from profile.models import StudentProfile
from profile.mongo import student_collection
from datetime import datetime

router = APIRouter()

@router.post("/students/create")
async def create_student_profile(profile: StudentProfile):
    existing = await student_collection.find_one({"email": profile.email})
    if existing:
        raise HTTPException(status_code=400, detail="Student with this email already exists.")
    
    profile_dict = profile.dict()
    profile_dict["created_at"] = datetime.utcnow()
    profile_dict["updated_at"] = datetime.utcnow()

    await student_collection.insert_one(profile_dict)
    return {"message": "Student profile created successfully"}
