from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.index import role, rescue_service, car_type, user, customer, car_info, station, charging_port, comment, order, chat, fake_data
from chat.index import chatRoute
from constants.env_value import APP_NAME, DESCRIPTION_APP, VERSION

app = FastAPI(
    title="API For {} App".format(APP_NAME),
    description=DESCRIPTION_APP,
    version=VERSION,
    # root_path="/api/{0}".format(VERSION),
)

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(fake_data, prefix="/fake-data", tags=["Fake Data"])
app.include_router(chat, prefix="/chat", tags=["chat"])
app.include_router(chatRoute, prefix="/bot", tags=["bot"])
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