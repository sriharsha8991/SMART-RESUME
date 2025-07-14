from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Optional
from datetime import date

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
    dob: date
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
    resume_link: Optional[HttpUrl]
    interests: Optional[List[str]]
    languages: Optional[List[str]]
