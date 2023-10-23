from fastapi import FastAPI
from routes.index import user, credential, category, sub_category, location, suggestion

app = FastAPI()

app.include_router(user)
app.include_router(credential)
app.include_router(category)
app.include_router(sub_category)
app.include_router(location)
app.include_router(suggestion)
