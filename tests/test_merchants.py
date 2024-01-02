import unittest
from dotenv import dotenv_values
from squad import Squad

config = dotenv_values(".env")
secret_key = config["SK2"]
bvn = config["BVN"]
a = Squad(secret_key=secret_key)

class TestSquadMerchant(unittest.TestCase):

    def setUp(self):
        self.squad_client = Squad(secret_key=secret_key)

    def test_create_sub_users(self):
        merchant = {
            "display_name": "joseph",
            "account_name": "Joseph Folayan",
            "account_number": "4920299492",
            "bank_code": "058",
            "bank": "GTBank",
        }
        res = self.squad_client.merchants.create_sub_users(merchant)
        self.assertEqual(res["status"], 200)