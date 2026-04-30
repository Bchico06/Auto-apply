from collections import Counter
from fastapi import APIRouter, Depends, HTTPException
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.core.config import JWT_ALGORITHM, JWT_SECRET
from app.core.db import get_db
from app.core.security import create_access_token, hash_password, verify_password
from app.models.models import JobApplication, User
from app.schemas.schemas import ApplicationCreate, DashboardOut, LoginIn, ProfileUpdate, RegisterIn, TokenOut

router = APIRouter()

def get_user_from_token(token: str, db: Session):
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        user_id = int(payload.get("sub"))
    except (JWTError, TypeError, ValueError):
        raise HTTPException(status_code=401, detail="Token inválido")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.post('/auth/register', response_model=TokenOut)
def register(data: RegisterIn, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=400, detail='Email ya registrado')
    user = User(email=data.email, password_hash=hash_password(data.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return TokenOut(access_token=create_access_token(str(user.id)))

@router.post('/auth/login', response_model=TokenOut)
def login(data: LoginIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail='Credenciales inválidas')
    return TokenOut(access_token=create_access_token(str(user.id)))

@router.put('/profile/{token}')
def update_profile(token: str, data: ProfileUpdate, db: Session = Depends(get_db)):
    user = get_user_from_token(token, db)
    for k, v in data.model_dump().items():
        setattr(user, k, v)
    db.commit()
    return {'ok': True}

@router.post('/applications/{token}')
def create_application(token: str, data: ApplicationCreate, db: Session = Depends(get_db)):
    user = get_user_from_token(token, db)
    app = JobApplication(user_id=user.id, platform=data.platform, company=data.company, title=data.title)
    db.add(app)
    db.commit()
    return {'ok': True}

@router.get('/dashboard/{token}', response_model=DashboardOut)
def dashboard(token: str, db: Session = Depends(get_db)):
    user = get_user_from_token(token, db)
    apps = db.query(JobApplication).filter(JobApplication.user_id == user.id).all()
    sent = len(apps)
    companies = len(set(a.company for a in apps))
    interviews = sum(1 for a in apps if a.interview)
    statuses = Counter(a.status for a in apps)
    answered = statuses.get('answered', 0) + statuses.get('interview', 0)
    rate = (answered / sent * 100) if sent else 0
    return DashboardOut(sent=sent, companies=companies, interviews=interviews, response_rate=round(rate, 1))
