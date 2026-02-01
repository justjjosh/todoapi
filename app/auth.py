from passlib.context import CryptContext
from jose import JWTError, jwt
import datetime
import os
from dotenv import load_dotenv


pwd_context = CryptContext (
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__ident="2b"
)
load_dotenv()
JWT_SECRET_KEY = (os.getenv("JWT_SECRET_KEY"))
JWT_ALGORITHM = (os.getenv("JWT_ALGORITHM"))
JWT_EXPIRATION_MINUTES = int(os.getenv("JWT_EXPIRATION_MINUTES"))

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=JWT_EXPIRATION_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm = JWT_ALGORITHM)
    return encoded_jwt

def verify_token(token: str) -> dict | None:
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=JWT_ALGORITHM)
        return payload
    except Exception as e:
        print(f"JWT verification failed: {e}")
        return None
    
if __name__ == "__main__":
    password = "mypassword1"
    hashed = hash_password(password)
    print(f"Hashed: {hashed}")
    print(f"Verify correct password: {verify_password(password, hashed)}")
    print(f"Verify wrong password: {verify_password('wrongpassword', hashed)}")

    token = create_access_token({"sub": "user123", "name": "joshua"})
    print(f"Token: {token}")
    decoded = verify_token(token)
    print(f"Decoded: {decoded}")
