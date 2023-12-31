
from squad._squad import SquadClient
from squad.payments import PaymentTransaction
__all__ =  (
    "Squad",
)


class Squad(SquadClient):
    """ Squad Base Class"""
    def __init__(self, secret_key=None):
         SquadClient.__init__(self, secret_key=secret_key)
         self.payments = PaymentTransaction

    