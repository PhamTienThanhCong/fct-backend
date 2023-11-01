from enum import Enum

CHARING_STATUS = {
    'NOT_ORDER': 0,
    'FREE': 1,
    'BUSY': 2,
    'WAITING_ORDER': 3,
    'ORDERED': 4,
    'CANCEL': 5,
}

CHARING_STATUS_TEXT = {
    0: 'Not order',
    1: 'Free',
    2: 'Busy',
    3: 'Waiting order',
    4: 'Ordered',
}

ORDER_STATUS = {
    'NOT_ORDER': 0,
    'ORDERED': 1,
    'CONFIRM_ORDER': 2,
    'CANCEL_ORDER': 3,
    'FINISH_ORDER': 4,
}

ORDER_STATUS_TEXT = {
    0: 'Not order',
    1: 'Ordered',
    2: 'Confirm order',
    3: 'Cancel order',
    4: 'Finish order',
}

CHARING_PORT_STATUS = {
    'free': 1,
    'busy': 2,
    'broken': 0,
}

class AcceptType(str, Enum):
    accept = "accept"
    cancel = "cancel"
    finish = "finish"

class ChargingPortStatus(str, Enum):
    free: str = "free"
    busy: str = "busy"
    broken: str = "broken"