
from squad._squad import SquadClient
from squad.utils.exceptions import InvalidSecretKey
from squad.payments import PaymentTransaction
from squad.merchants import SquadMerchant
from squad.virtual_accounts import VirtualAccounts
from squad.value_added_service import SquadServices_Client
from squad.dispute import Dispute
from squad.wallet import Wallet
from squad.transfer import SquadTransfer
from squad.pos import SquadPOS


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
         self.value_added_service = SquadServices_Client
         self.dispute = Dispute
         self.wallet = Wallet
         self.transfer = SquadTransfer
         self.pos = SquadPOS

    