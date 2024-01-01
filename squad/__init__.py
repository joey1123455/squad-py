
from squad._squad import SquadClient
from squad.utils.exceptions import InvalidSecretKey
from squad.payments import PaymentTransaction
from squad.merchants import SquadMerchant
from squad.virtual_accounts import VirtualAccounts
from squad.dispute import Dispute

__all__ =  (
    "Squad",
)


class Squad(SquadClient):
    """ Squad Base Class"""
    def __init__(self, secret_key=None,test=True):
         if not secret_key:
              raise InvalidSecretKey("you must pass a secret_key from Squad Dashboard")
         SquadClient.__init__(self, secret_key=secret_key,test=test)
         self.payments = PaymentTransaction
         self.merchants = SquadMerchant
         self.virtual_accounts = VirtualAccounts
         self.dispute = Dispute


    