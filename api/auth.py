from fastapi import APIRouter
from models.auth import Token, CreateUSer

router = APIRouter(
    prefix="/auth"
)

@router.post("/sign-up", response_model=Token)
def sign_up():
    pass