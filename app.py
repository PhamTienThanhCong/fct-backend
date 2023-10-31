from fastapi import Depends, FastAPI
from config.auth import AuthHandler
from routes.index import role, rescue_service, car_type, user, customer, car_info, station, charging_port, comment, order
from config.env_value import APP_NAME, DESCRIPTION_APP, VERSION

app = FastAPI(
    title="API For {} App".format(APP_NAME),
    description=DESCRIPTION_APP,
    version=VERSION,
    # root_path="/api/{0}".format(VERSION),
)
auth_handler = AuthHandler()

app.include_router(order, prefix="/order", tags=["Order"])
app.include_router(comment, prefix="/comment", tags=["Comment"])
app.include_router(customer, prefix="/customer", tags=["Customer"])
app.include_router(user, prefix="/user", tags=["Admin"])
app.include_router(station, prefix="/station", tags=["Station"])
app.include_router(charging_port, prefix="/port", tags=["Station Port"])
app.include_router(car_info, prefix="/car-info", tags=["Car Info"])
app.include_router(car_type, prefix="/car-type", tags=["Car Type"])
app.include_router(role, prefix="/role", tags=["Role"])
app.include_router(rescue_service, prefix="/rescue-service", tags=["Rescue Service"])