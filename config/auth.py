import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from config.env_value import SECRET_KEY

class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"])

    secret = SECRET_KEY

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, password, hashed_password):
        return self.pwd_context.verify(password, hashed_password)

    def encode_token(self, account):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=30),
            'iat': datetime.utcnow(),
            'sub': account
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm='HS256'
        )

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=401, detail='Signature has expired')
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail='Invalid token')
    
    def auth_wrapper_super_admin(self, auth: HTTPAuthorizationCredentials = Security(security)):
        payload = self.decode_token(auth.credentials)
        if payload['role_id'] != 1:
            raise HTTPException(401, "Invalid token")
        return payload

    def auth_wrapper_admin(self, auth: HTTPAuthorizationCredentials = Security(security)):
        payload = self.decode_token(auth.credentials)
        if payload['role_id'] == 0:
            raise HTTPException(401, "Invalid token")
        return payload
    
    def auth_wrapper_user(self, auth: HTTPAuthorizationCredentials = Security(security)):
        payload = self.decode_token(auth.credentials)
        if payload['role_id'] != 0:
            raise HTTPException(401, "Invalid token")
        return payload
