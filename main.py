from fastapi import FastAPI
from routes.index import credential

app = FastAPI(
    title="Users API",
    description="a REST API using python and mysql",
    version="0.0.1"
    )

app.include_router(credential)
