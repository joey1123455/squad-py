"""
Wallet Package
==============

Module providing a Python client for interacting with the Squad API, offering functionalities related to Squad Wallet.

Package Structure:
------------------
- `squad.wallet.wallet`: Module containing the `Wallet` class.

Classes:
--------
1. `Wallet(SquadClient)`: Represents a class providing functionalities related to Squad Wallet within the Squad API.
    - Methods:
        - `balance(cls, currency_id: str = "NGN") -> JSONDict`: Get Squad Wallet Balance.
            - Parameters:
                - `currency_id` (str): Currency code for the wallet balance (default is "NGN").

Example:
--------
```python
# Create an instance of Wallet
wallet_instance = Wallet()

# Get Squad Wallet Balance
balance_result = wallet_instance.balance(currency_id='NGN')
```
"""

from squad._squad import SquadClient

class Wallet(SquadClient):
    """ Squad Wallet Base"""

    @classmethod
    def balance(cls, currency_id: str ="NGN"):
        """
        This endpoint allows you get your Squad Wallet Balance.\n
        Please be informed that the wallet balance is in KOBO. (Please note that you can't get wallet balance for Dollar transactions)

        Parameters
            
        ## Required:
                - `currency_id` (str): It only takes the value "NGN". (Please note that you can't get wallet balance for Dollar transactions)
        """
        return cls().requests._send_request(f"/merchant/balance","get",data={"currency_id": currency_id})