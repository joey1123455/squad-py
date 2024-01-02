import unittest
from dotenv import dotenv_values
from squad import Squad

config = dotenv_values(".env")
secret_key = config["SK2"]
bvn = config["BVN"]
a = Squad(secret_key=secret_key)

class TestSquadWallet(unittest.TestCase):

    def setUp(self):
        self.squad_client = Squad(secret_key=secret_key)

    def test_balance(self):
        res = self.squad_client.wallet.balance("NGN")
        self.assertEqual(res["status"], 200)