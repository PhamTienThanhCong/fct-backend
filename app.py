from fastapi import FastAPI
from routes.index import role, rescue_service, car_type
from config.env_value import APP_NAME, DESCRIPTION_APP, VERSION

app = FastAPI(
    title="API For {} App".format(APP_NAME),
    description=DESCRIPTION_APP,
    version=VERSION
)

app.include_router(car_type, prefix="/car-type", tags=["Car Type"])
app.include_router(role, prefix="/role", tags=["Role"])
app.include_router(rescue_service, prefix="/rescue-service", tags=["Rescue Service"])