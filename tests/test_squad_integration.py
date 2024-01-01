import unittest
import uuid
from dotenv import dotenv_values
from squad import Squad

config = dotenv_values(".env")
secret_key = config["SK2"]
a = Squad(secret_key=secret_key)

class TestSquadPayments(unittest.TestCase):

    def setUp(self):
        random_uuid = uuid.uuid4()
        self.squad_client = Squad(secret_key=secret_key)
        self.transaction_ref = str(random_uuid)

    
    def test_initiate_transaction(self):
        transaction_data = {
            "email": "recipient@example.com",
            "amount": 1000,
            "initiate_type": "inline",
            "currency": "USD",
            "transaction_ref": self.transaction_ref,
        }
        
        res = self.squad_client.transactions.initiate_transaction(transaction_data)
        print(res)
        self.assertEqual(res["status"], 200)

    def test_verify_transaction(self):
        res = self.squad_client.transactions.verify_transaction("1ae16cde-a46f-4cfb-a6c1-c44a659debbc")

        # # Assert the response from the API
        self.assertEqual(res["status"], 200)
        # print("ref",self.transaction_ref)

if __name__ == '__main__':
    unittest.main()
