from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, UserResponse, Token
from app.services.auth import get_password_hash, verify_password, create_access_token

router = APIRouter()

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def register_user(user_in: UserCreate):
    # Lógica de comprobación e inserción en DB
    hashed_pwd = get_password_hash(user_in.password)
    # Guardar nuevo usuario...
    return {"id": "new-user-id", "email": user_in.email, "full_name": user_in.full_name}

@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Lógica para autenticar con DB
    # user = await get_user_by_email(form_data.username)
    access_token = create_access_token(data={"sub": "user-id-ejemplo"})
    return {"access_token": access_token, "token_type": "bearer"}