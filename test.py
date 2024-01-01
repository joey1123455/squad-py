from dotenv import dotenv_values
from squad import Squad

config = dotenv_values(".env")
a = Squad(secret_key=config["SK2"])
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
#print(a.merchants.create_sub_users(merchant))
business = {
        "customer_identifier": "CCC",
        "business_name": "Techzilla-Joseph Okoye",
        "mobile_num": "08139011943",
        "bvn": config["BVN"],
        "beneficiary_account": "4920299492"
    }


Customer =  {
    "customer_identifier": "CCC",
    "first_name": "BusinessName-Joesph",
    "last_name": "Ayodele",
    "mobile_num": "08139011943",
    "email": "ayo@gmail.com",
    "bvn": config["BVN"],
    "dob": "30/10/1990",
    "address": "22 Kota street, UK",
    "gender": "1",
    "beneficiary_account": "4920299492"
}
#b = a.virtual_accounts.create_business_virtual_account(business)
b = a.virtual_accounts.create_customer_virtual_account(Customer)
print(b)