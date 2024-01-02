import random
import unittest
import uuid
from dotenv import dotenv_values
from squad import Squad

config = dotenv_values(".env")
secret_key = config["SK2"]
a = Squad(secret_key=secret_key)

class TestDispute(unittest.TestCase):

    def setUp(self):
        self.squad_client = Squad(secret_key=secret_key)

    def test_get_dispute(self):
        res = self.squad_client.dispute.get_dispute()
        self.assertEqual(res["status"], 200)

    def test_get_dispute_upload_url(self):
        ticket = str(uuid.uuid4())
        digit = random.randint(1, 10000)
        file = "img.jpg"
        res = self.squad_client.dispute.get_dispute_upload_url(ticket, file)
        # print(res)
        self.assertIsNotNone(res)

    def test_resolve_dispute(self):
        ticket = str(uuid.uuid4())
        digit = random.randint(1, 10000)
        file = "img{digit}.jpg"
        res = self.squad_client.dispute.resolve_dispute(ticket, digit)
        self.assertIsNotNone(res)


if __name__ == '__main__':
    unittest.main()