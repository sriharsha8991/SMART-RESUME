from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Optional
from datetime import datetime

class Education(BaseModel):
    degree: str
    institution: str
    start_year: int
    end_year: int
    cgpa: float

class Project(BaseModel):
    title: str
    description: str
    tech_stack: List[str]
    github_url: Optional[HttpUrl]

class Certification(BaseModel):
    title: str
    issuer: str
    year: int

class Experience(BaseModel):
    role: str
    company: str
    duration: str
    description: str

class Contribution(BaseModel):
    type: str
    title: str
    description: str
    link: Optional[HttpUrl]

class StudentProfile(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    dob: datetime
    location: str
    career_objective: str
    education: List[Education]
    skills: List[str]
    projects: List[Project]
    certifications: Optional[List[Certification]] = []
    experience: Optional[List[Experience]] = []
    contributions: Optional[List[Contribution]] = []
    github_url: Optional[HttpUrl]
    linkedin_url: Optional[HttpUrl]
    interests: Optional[List[str]]
    languages: Optional[List[str]]

class SkillsUpdate(BaseModel):
    action: str = "replace"  # "add", "remove", "replace"
    skills: List[str]

class ExperienceUpdate(BaseModel):
    action: str = "add"  # "add", "remove", "replace"
    experience: Optional[Experience] = None
    index: Optional[int] = None

class StudentProfilePartialUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    dob: Optional[datetime] = None
    location: Optional[str] = None
    career_objective: Optional[str] = None
    education: Optional[List[Education]] = None
    skills: Optional[List[str]] = None
    projects: Optional[List[Project]] = None
    certifications: Optional[List[Certification]] = None
    experience: Optional[List[Experience]] = None
    contributions: Optional[List[Contribution]] = None
    github_url: Optional[HttpUrl] = None
    linkedin_url: Optional[HttpUrl] = None
    resume_link: Optional[HttpUrl] = None
    interests: Optional[List[str]] = None
    languages: Optional[List[str]] = None
    
    class Config:
        extra = "forbid"  # Prevent extra fields
