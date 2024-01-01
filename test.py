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
#b = a.virtual_accounts.create_customer_virtual_account(Customer)
filter = {
    "transactionReference": "REFQVFJWNB75/1704003205952_1"

}
#b = a.virtual_accounts.filter_merchant_transaction(filter)
#b = a.virtual_accounts.get_customer_by_virtual_account_number('3456987768')
#b = a.virtual_accounts.get_customer_using_customer_identifier("hex11rthyuirjahdu")

customer_data = {
    "customer_bvn": "12298752255",
    "customer_identifier": "hex11rthyuirjahdu",
    "phone_number": "0813901194"
}
#b = a.virtual_accounts.update_customer_bvn(customer_data)
#b = a.virtual_accounts.query_all_merchant_virtual_account()
data = {
    "beneficiary_account": "1229706340",
    "virtual_account_number": "3998621828"
}
#b = a.virtual_accounts.update_beneficiary_account(data)
simulate =  {
    "virtual_account_number": "3998621828",
    "amount": "2000"
}
#b = a.virtual_accounts.simulate_payment(simulate)
#b = a.virtual_accounts.get_webhook_error_logs()
#b = a.virtual_accounts.query_customer_transaction_by_customer_identifier("CCC")
#print(b)

# print(b)

