from dotenv import dotenv_values
from squad import Squad

config = dotenv_values(".env")
a = Squad(secret_key=config["SECRET_KEY"])
transaction_data = {
    "email": "recipient@example.com",
    "amount": 1000,
    "initiate_type": "inline",
    "currency": "USD",
}
print(a.payments.initiate_transaction(transaction_data))
