import jwt
import datetime

SECRET_KEY = "my_super_secret_password"
ALGORITHM = "HS256"

header = {
    "alg": "HS256",
    "typ": "JWT"
}

payload = {
    "sub": "1234567",
    "name": "josh",
    "iat": datetime.datetime.now(datetime.timezone.utc),
    "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=30)
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print(f"Token: {token}")

dec_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
print(f"Decoded token: {dec_token}")