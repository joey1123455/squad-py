import unittest
from dotenv import dotenv_values
from squad import Squad

config = dotenv_values(".env")
secret_key = config["SK2"]
bvn = config["BVN"]
a = Squad(secret_key=secret_key)

class TestSquadTransfer(unittest.TestCase):

    def setUp(self):
        self.squad_client = Squad(secret_key=secret_key)

    def test_account_lookup(self):
        data = {
            "bank_code": "000017",
            "account_number": "0248130510",
        } 
        res = self.squad_client.transfer.account_lookup(data) 
        # print(res) 
        # self.assertEqual(res["status"], 200)
        self.assertIsNotNone(res)

    def test_fund_transfer(self):
        data = {
           "remark": "for test transfer to my customer",
            "bank_code":"000013",
            "currency_id": "NGN",
            "amount": "100",
            "account_number":"0123456789",
            "transaction_reference":"SBABCKDY_12345",
            "account_name":"BOLUS PAUL"
        }    
        res = self.squad_client.transfer.fund_transfer(data) 
        self.assertIsNotNone(res)

    def test_re_query(self):
        data = {
            "transaction_reference": "47484093994949"
        }

        res = self.squad_client.transfer.re_query(data)
        self.assertIsNotNone(res)

    def test_get_all_transfer(self):
        res = self.squad_client.transfer.get_all_transfer()
        self.assertIsNotNone(res)

    