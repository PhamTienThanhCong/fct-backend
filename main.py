from fastapi import FastAPI
from routes.index import user, credential, category, sub_category, location, suggestion

app = FastAPI()

app.include_router(user, prefix="/user", tags=["user"])
app.include_router(credential, prefix="/credential", tags=["credential"])
app.include_router(category, prefix="/category", tags=["category"])
app.include_router(sub_category, prefix="/sub_category", tags=["sub_category"])
app.include_router(location, prefix="/location", tags=["location"])
app.include_router(suggestion, prefix="/suggestion", tags=["suggestion"])
