from fastapi import APIRouter, HTTPException, status
from profile.models import StudentProfile
from profile.mongo import student_collection
from datetime import datetime
from typing import  Dict, Any
from bson import ObjectId


router = APIRouter()

def serialize_document(doc: Dict[str, Any]) -> Dict[str, Any]:
    """Convert MongoDB document to JSON serializable format"""
    if doc and "_id" in doc:
        doc["_id"] = str(doc["_id"])
    return doc

@router.post("/students/create",tags=["Students"], status_code=status.HTTP_201_CREATED)
async def create_student_profile(profile: StudentProfile):
    try:
        existing = await student_collection.find_one({"email": profile.email})
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="Student with this email already exists."
            )
        
        profile_dict = profile.model_dump(mode='json')
        profile_dict["created_at"] = datetime.utcnow()
        profile_dict["updated_at"] = datetime.utcnow()

        result = await student_collection.insert_one(profile_dict)
        return {
            "message": "Student profile created successfully",
            "student_id": str(result.inserted_id)
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create profile: {str(e)}"
        )

@router.get("/students/{student_id}",tags=["Students"])
async def get_student_profile(student_id: str):
    try:
        if not ObjectId.is_valid(student_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid student ID format"
            )
        
        student = await student_collection.find_one({"_id": ObjectId(student_id)})
        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student profile not found"
            )
        
        return serialize_document(student)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve profile: {str(e)}"
        )

@router.get("/students/email/{email}",tags=["Students"])
async def get_student_by_email(email: str):
    try:
        student = await student_collection.find_one({"email": email})
        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student profile not found"
            )
        
        return serialize_document(student)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve profile: {str(e)}"
        )

@router.put("/students/{student_id}",tags=["Students"])
async def update_student_profile(student_id: str, profile: StudentProfile):
    try:
        if not ObjectId.is_valid(student_id):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid student ID format"
            )
        
        # Check if the student exists first
        existing_student = await student_collection.find_one({"_id": ObjectId(student_id)})
        if not existing_student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student profile not found"
            )
        
        # Validate email uniqueness if email is being updated
        if profile.email != existing_student.get("email"):
            email_exists = await student_collection.find_one({
                "email": profile.email,
                "_id": {"$ne": ObjectId(student_id)}
            })
            if email_exists:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already exists for another student"
                )
        
        profile_dict = profile.model_dump(mode='json')
        profile_dict["updated_at"] = datetime.utcnow()
        
        # Preserve original creation timestamp
        if "created_at" in existing_student:
            profile_dict["created_at"] = existing_student["created_at"]
        
        result = await student_collection.update_one(
            {"_id": ObjectId(student_id)},
            {"$set": profile_dict}
        )
        
        if result.modified_count == 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No changes were made to the profile"
            )
        
        # Return the updated student profile
        updated_student = await student_collection.find_one({"_id": ObjectId(student_id)})
        return {
            "message": "Student profile updated successfully",
            "student": serialize_document(updated_student)
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to update profile: {str(e)}"
        )

@router.get("/students",tags=["Students"])
async def list_student_profiles(skip: int = 0, limit: int = 100):
    try:
        cursor = student_collection.find().skip(skip).limit(limit)
        students = await cursor.to_list(length=limit)
        
        return {
            "students": [serialize_document(student) for student in students],
            "count": len(students)
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to retrieve profiles: {str(e)}"
        )
