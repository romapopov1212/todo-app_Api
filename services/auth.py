from fastapi import HTTPException, status

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.crypto.scrypt import validate
from passlib.hash import bcrypt
from pydantic import ValidationError

from models.auth import User
from jose import jwt, JWTError

from settings import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/sign-in")

# def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
#     return AuthS

class AuthService:

    @classmethod
    def verify_password(cls, password: str, hash_pass: str) -> bool:
        return bcrypt.verify(password, hash_pass)

    @classmethod
    def hash_password(cls, password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def validate_token(cls, token: str) -> User:

        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Cold not validate",
            headers={
                'WWW_Authenticate' : 'Bearer'
            }
        )

        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm],
            )
        except JWTError:
            raise exception from None

        user_data = payload.get('user')

        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user

