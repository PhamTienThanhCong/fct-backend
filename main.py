from fastapi import FastAPI
from routes.index import credential

app = FastAPI()

app.include_router(credential, prefix="/credential", tags=["Credential"])
