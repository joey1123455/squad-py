import unittest
from dotenv import dotenv_values
from squad import Squad

config = dotenv_values(".env")
secret_key = config["SK2"]
bvn = config["BVN"]
a = Squad(secret_key=secret_key)

class TestSquadVirtualAccounts(unittest.TestCase):

    def setUp(self):
        self.squad_client = Squad(secret_key=secret_key)

    def test_create_business_virtual_account(self):
        business_data = {
            "customer_identifier": "CCC",
            "business_name": "Techzilla-Joseph Okoye",
            "mobile_num": "08139011943",
            "bvn": config["BVN"],
            "beneficiary_account": "4920299492"
        }

        res = self.squad_client.virtual_accounts.create_business_virtual_account(business_data)
        # Assert the response from the API
        self.assertEqual(res["status"], 200)

    def test_create_customer_virtual_account(self):
        customer_data = {
            "customer_identifier": "CCC12efGi",
            "first_name": "SDK devs- Joseph",
            "last_name": "Folayan",
            "mobile_num": "08118997115",
            "email": "folayanjoey@gmail.com",
            "bvn": config["BVN"],
            "dob": "30/10/1990",
            "address": "22 Kota street, UK",
            "gender": "1",
            "beneficiary_account": "4920299492"
        }

        res = self.squad_client.virtual_accounts.create_customer_virtual_account(customer_data)
        # Assert the response from the API
        self.assertEqual(res["status"], 200)

    def test_query_merchant_transaction_with_filters(self):
        filter = {
            "transactionReference": "REFQVFJWNB75/1704003205952_1"

        }

        res = self.squad_client.virtual_accounts.query_merchant_transaction_with_filters(filter)
        # Assert the response from the API
        self.assertEqual(res["status"], 200)

    def test_get_customer_by_virtual_account_number(self):

        res = self.squad_client.virtual_accounts.get_customer_by_virtual_account_number('3456987768')
        # Assert the response from the API
        self.assertEqual(res["status"], 200)

    def test_get_customer_using_customer_identifier(self):

        res = self.squad_client.virtual_accounts.get_customer_using_customer_identifier('CCC12efGi')
        # Assert the response from the API
        self.assertEqual(res["status"], 200)

    def test_update_customer_bvn(self):
        customer_data = {
            "customer_bvn": bvn,
            "customer_identifier": "CCC12efGi",
            "phone_number": "08118997115"
        }
        res = self.squad_client.virtual_accounts.update_customer_bvn(customer_data)
        # Assert the response from the API
        self.assertIsNotNone(res)

    def test_query_all_merchant_virtual_account(self):
        res = self.squad_client.virtual_accounts.query_all_merchant_virtual_account()
        # Assert the response from the API
        self.assertEqual(res["status"], 200)

    def test_update_beneficiary_account(self):

        data = {
            "beneficiary_account": "1229706340",
            "virtual_account_number": "3998621828"
        }
    
        res = self.squad_client.virtual_accounts.update_beneficiary_account(data)
        # Assert the response from the API
        self.assertEqual(res["status"], 200)

    def test_simulate_payment(self):

        simulate =  {
            "virtual_account_number": "3998621828",
            "amount": "2000"
        }
    
        res = self.squad_client.virtual_accounts.simulate_payment(simulate)
        # Assert the response from the API
        self.assertEqual(res["status"], 200)

    def test_get_webhook_error_logs(self):

        simulate =  {
            "virtual_account_number": "3998621828",
            "amount": "2000"
        }
    
        res = self.squad_client.virtual_accounts.get_webhook_error_logs()
        # Assert the response from the API
        self.assertEqual(res["status"], 200)

    def test_query_customer_transaction_by_customer_identifier(self):
    
        res = self.squad_client.virtual_accounts.query_customer_transaction_by_customer_identifier("CCC")
        # Assert the response from the API
        self.assertEqual(res["status"], 200)

if __name__ == '__main__':
    unittest.main()