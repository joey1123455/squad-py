
from squad._squad import SquadClient
from squad.utils.exceptions import InvalidSecretKey
from squad.payments import PaymentTransaction
__all__ =  (
    "Squad",
)


class Squad(SquadClient):
    """ Squad Base Class"""
    def __init__(self, secret_key=None):
         if not secret_key:
              raise InvalidSecretKey("you must pass a secret_key from Squad Dashboard")
         SquadClient.__init__(self, secret_key=secret_key)
         self.payments = PaymentTransaction

    