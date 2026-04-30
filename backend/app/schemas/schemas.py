from pydantic import BaseModel, EmailStr

class RegisterIn(BaseModel):
    email: EmailStr
    password: str

class LoginIn(RegisterIn):
    pass

class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ProfileUpdate(BaseModel):
    full_name: str = ""
    desired_role: str = ""
    years_experience: int = 0
    location: str = ""
    work_mode: str = "remote"
    languages: str = ""
    skills: str = ""

class ApplicationCreate(BaseModel):
    platform: str
    company: str
    title: str

class DashboardOut(BaseModel):
    sent: int
    companies: int
    interviews: int
    response_rate: float
