import unittest
from unittest.mock import MagicMock
from dotenv import dotenv_values
from squad import Squad

config = dotenv_values(".env")
secret_key = config["SK2"]
a = Squad(secret_key=secret_key)

class TestSquadAPI(unittest.TestCase):

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
            "customer_identifier": "CCC",
            "first_name": "Techzilla- Joesph",
            "last_name": "Okoye",
            "mobile_num": "08139011943",
            "email": "ayo@gmail.com",
            "bvn": config["BVN"],
            "dob": "30/10/1990",
            "address": "22 Kota street, UK",
            "gender": "1",
            "beneficiary_account": "4920299492"
        }

        res = self.squad_client.virtual_accounts.create_customer_virtual_account(customer_data)
        # Assert the response from the API
        self.assertEqual(res["status"], 200)

    def test_filter_merchant_transaction(self):
        filter = {
            "transactionReference": "REFQVFJWNB75/1704003205952_1"

        }

        res = self.squad_client.virtual_accounts.filter_merchant_transaction(filter)
        # Assert the response from the API
        self.assertEqual(res["status"], 200)

    def test_get_customer_by_virtual_account_number(self):

        res = self.squad_client.virtual_accounts.get_customer_by_virtual_account_number('3456987768')
        # Assert the response from the API
        self.assertEqual(res["status"], 200)

    def test_get_customer_using_customer_identifier(self):

        res = self.squad_client.virtual_accounts.get_customer_using_customer_identifier('hex11rthyuirjahdu')
        # Assert the response from the API
        self.assertEqual(res["status"], 200)

if __name__ == '__main__':
    unittest.main()