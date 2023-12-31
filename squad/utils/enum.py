from enum import Enum

class Currency(Enum):
    USD = "USD"
    NGN = "NGN"


class PaymentChannel(Enum):
    CARD = "card"
    BANK = "bank"
    USSD = "ussd"
    TRANSFER = "transfer"