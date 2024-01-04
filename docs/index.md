# <center>SQUAD-PY<center/>

This site contains the project documentation for the
**`squad-py`** project that is a wrapper built over squad api endpoints
a payment gateway facilitated by GTBank.
[squad docs](
    https://squadinc.gitbook.io/squad-api-documentation/).

## Installation
```bash
pip install squadco
```

### Before you Begin
1. Create a free Squad account [Here](https://dashboard.squadco.com/sign-up) (for Test, create a [Sandbox Account](https://sandbox.squadco.com/sign-up))
2. Integrate Squad payment gateway.
3. Copy your private key from your Dashboard.


### Sample Usage
```python
# Create a Squad instance
squad_instance = Squad(secret_key='your_secret_key')

# Access payment transactions
payments_result = squad_instance.payments.list_payments()

# Access merchant information
merchant_info = squad_instance.merchants.get_merchant_info(merchant_id='merchant123')
```

## Table Of Contents

1. [Squad Package](squad.md)
2. [Payment Package](payment.md)
3. [Merchants Package](merchants.md)
4. [Virtual Accounts Package](virtual_accounts.md)
5. [Wallet Package](wallet.md)
6. [Pos Package](pos.md)
7. [Transfer Package](transfer.md)
8. [Value Added Sevices Package](value_added.md)


Quickly find what you're looking for depending on
your use case by looking at the different pages.

## Acknowledgements

I want to thank [Uche David](https://github.com/debugtitan) for leading the project and writing most parts of it. Also, I want to thank [Adetunji peter](https://github.com/Grenate22), [Joseph Folayan](https://github.com/joey1123455) and that sweet grass for also contributing.

