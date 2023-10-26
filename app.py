from fastapi import FastAPI
from routes.index import user, auth
from config.env_value import APP_NAME, DESCRIPTION_APP, VERSION

app = FastAPI(
    title="API For {} App".format(APP_NAME),
    description=DESCRIPTION_APP,
    version=VERSION
)

app.include_router(auth)
app.include_router(user)
