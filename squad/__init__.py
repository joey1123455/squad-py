"""
Squad API Package
=================

Module providing a Python client for interacting with the Squad API, offering functionalities for payment and financial operations.

Package Structure:
------------------
- `squad._squad`: Main module containing the `SquadClient` class.
- `squad.utils.exceptions`: Module with custom exceptions, including `InvalidSecretKey`.
- `squad.payments`: Module for payment-related operations, including `PaymentTransaction`.
- `squad.merchants`: Module for merchant-related operations, including `SquadMerchant`.
- `squad.virtual_accounts`: Module for virtual account-related operations, including `VirtualAccounts`.
- `squad.dispute`: Module for dispute-related operations, including `Dispute`.
- `squad.wallet`: Module for wallet-related operations, including `Wallet`.
- `squad.transfer`: Module for fund transfer-related operations, including `SquadTransfer`.
- `squad.pos`: Module for point-of-sale (POS) operations, including `SquadPOS`.

Classes:
--------
1. `SquadClient`: Represents the main client for interacting with the Squad API.
    - Attributes:
        - `payments`: Provides access to payment transaction operations.
        - `merchants`: Provides access to SquadMerchant operations.
        - `virtual_accounts`: Provides access to virtual account operations.
        - `dispute`: Provides access to dispute operations.
        - `wallet`: Provides access to wallet operations.
        - `transfer`: Provides access to SquadTransfer operations.
        - `pos`: Provides access to SquadPOS operations.

2. `Squad`: Represents the main interface for interacting with the Squad API, inheriting from `SquadClient`.
    - Attributes:
        - `payments`: Provides access to PaymentTransaction operations.
        - `merchants`: Provides access to SquadMerchant operations.
        - `virtual_accounts`: Provides access to VirtualAccounts operations.
        - `dispute`: Provides access to Dispute operations.
        - `wallet`: Provides access to Wallet operations.
        - `transfer`: Provides access to SquadTransfer operations.
        - `pos`: Provides access to SquadPOS operations.
    - Methods:
        - `__init__(self, secret_key=None, test=True)`: Initializes the Squad instance.

Global Attributes:
------------------
- `InvalidSecretKey`: Custom exception raised when the secret key is invalid.

Example:
--------
```python
# Create a Squad instance
squad_instance = Squad(secret_key='your_secret_key')

# Access payment transactions
payments_result = squad_instance.payments.list_payments()

# Access merchant information
merchant_info = squad_instance.merchants.get_merchant_info(merchant_id='merchant123')
```

For more information on API operations, refer to the Squad API documentation.

Note: Make sure to handle exceptions appropriately, especially the InvalidSecretKey exception.
"""

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
    """Squad API Client for Payment and Financial Operations.

    This class serves as the main interface for interacting with the Squad API,
    providing functionalities related to payments, merchants, virtual accounts,
    disputes, wallets, transfers, and point of sale (POS) operations.

    Parameters:
    - secret_key (str): The secret key obtained from the Squad Dashboard.
    - test (bool): A flag indicating whether to use the test environment (default is True).

    Raises:
    - InvalidSecretKey: If the `secret_key` is not provided.

    Attributes:
    - payments (class): Provides access to PaymentTransaction operations.
    - merchants (class): Provides access to SquadMerchant operations.
    - virtual_accounts (class): Provides access to VirtualAccounts operations.
    - dispute (class): Provides access to Dispute operations.
    - wallet (class): Provides access to Wallet operations.
    - transfer (class): Provides access to SquadTransfer operations.
    - pos (class): Provides access to SquadPOS operations.

    Example:
    ```python
    # Create a Squad instance
    squad_instance = Squad(secret_key='your_secret_key')

    # Access payment transactions
    payments_result = squad_instance.payments.list_payments()

    # Access merchant information
    merchant_info = squad_instance.merchants.get_merchant_info(merchant_id='merchant123')
    ```

    For more information on API operations, refer to the Squad API documentation.

    Note: Make sure to handle exceptions appropriately, especially the InvalidSecretKey exception.
    """
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

    