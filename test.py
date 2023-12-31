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
#print(a.payments.initiate_transaction(transaction_data))
#txn_ref =  "SQDEBU6383961457377100021"
#print(a.payments.verify_transaction(txn_ref))
merchant = {
    "display_name": "Uche David",
    "account_name": "Uchechukwu Agbakwuru",
    "account_number": "1229706340",
    "bank_code": "901",
    "bank": "Access Bank"
}
print(a.merchants.create_sub_users(merchant))