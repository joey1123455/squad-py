import unittest
from dotenv import dotenv_values
from squad import Squad

config = dotenv_values(".env")
secret_key = config["SK2"]
bvn = config["BVN"]
a = Squad(secret_key=secret_key)

class TestPos(unittest.TestCase):

    def setUp(self):
        self.squad_client = Squad(secret_key=secret_key)

    def test_get_all_transaction(self):
        page = 1
        perPage = 10
        filter_data = {
            "sort_by_dir": "DESC",
            "date_to": "2023-10-30",
        }
        res = self.squad_client.pos.get_all_transaction(perPage, page, filter_data)
        self.assertEqual(res["status"], 200)

    def test_create_terminal(self):
        
        data = {
            "email": "folayanjoey@gmail.com",
            "name": "james doug",
            "phone": "08118997115",
            "location_id": 1
        }

        res = self.squad_client.pos.create_terminal(data)
        self.assertEqual(res["status"], 200)

    def test_get_all_terminals(self):

        filter_data = {
            "page": 1,
            "perPage": 10
        }

        res = self.squad_client.pos.get_all_terminals(filter_data)
        self.assertEqual(res["status"], 200)