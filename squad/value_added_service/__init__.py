"""
Squad Services Client Package
============================

Module providing a Python client for interacting with the Squad API, offering functionalities related to Squad Value Added Services.

Package Structure:
------------------
- `squad.services.squad_services_client`: Module containing the `SquadServices_Client` class.

Classes:
--------
1. `SquadServices_Client(SquadClient)`: Represents a class providing functionalities related to Squad Services within the Squad API.
    - Methods:
        - `airtime(cls, airtime_data: dict) -> JSONDict`: Vend Airtime.
            - Parameters:
                - `airtime_data` (dict): Dictionary containing data to vend airtime.
                    - Required fields:
                        - `phone_number` (str): 11-digit phone number (e.g., "08139011943").
                        - `amount` (int): Amount in naira.

        - `get_data_bundles(cls, network: str) -> JSONDict`: Get Data Bundles Plan.
            - Parameters:
                - `network` (str): User Teleco ID (e.g., "MTN", "GLO", "AIRTEL", "MTN").

        - `data_bundles(cls, bundles_data: dict) -> JSONDict`: Vend Data.
            - Parameters:
                - `bundles_data` (dict): Dictionary containing data to vend data.
                    - Required fields:
                        - `phone_number` (str): 11-digit phone number (e.g., "08139011943").
                        - `amount` (int): Amount of the corresponding plan_code.
                        - `plan_code` (str): The plan code obtained from the `get_data_bundles` method (e.g., "1001").

        - `all_vending_transaction(cls, page: int, per_page: int, action: str) -> JSONDict`: Get All Vending Transactions.
            - Parameters:
                - `page` (int): The page of the transaction the merchant wants to view.
                - `per_page` (int): Number of transactions the merchant wants to view per page.
                - `action` (str): The type of transaction the merchant wants to see (e.g., "debit").

Example:
--------
```python
# Create an instance of SquadServices_Client
services_client_instance = SquadServices_Client()

# Vend Airtime
airtime_data = {
    'phone_number': '08139011943',
    'amount': 100
}
airtime_result = services_client_instance.airtime(airtime_data)

# Get Data Bundles Plan
network = 'MTN'
data_bundles_result = services_client_instance.get_data_bundles(network)

# Vend Data
bundles_data = {
    'phone_number': '08139011943',
    'amount': 500,
    'plan_code': '1001'
}
data_result = services_client_instance.data_bundles(bundles_data)

# Get All Vending Transactions
page = 1
per_page = 10
action = 'debit'
transactions_result = services_client_instance.all_vending_transaction(page, per_page, action)
```
"""

from squad._squad import SquadClient

class SquadServices_Client(SquadClient):
    """
    squad vending Base. 
    
    Equivalent value of all data and airtime vended will be charged from merchant SQUAD WALLET.
    """

    @classmethod
    def airtime(cls, airtime_data:dict):
        """
        This method is use to vend airtime.
        Minimum amount that can be vended is 50 naira

        Parameters:
        - `airtime_data` (dict): A dictionary containing data to vend airtime
            Required fields:
                - `phone_number` (str): 11 digit phone number. (format :: "08139011943")
                - `amount` (int): Amount in naira 

        returns:
        - JSONDict: The response data from thr squad API.                
        """
        endpoint = "/vending/purchase/airtime"
        return cls().requests._send_request(endpoint=endpoint,method="post",data=airtime_data)
    
    @classmethod
    def get_data_bundles(cls, network : str):
        """
        Data bundles plan for all telecos network.

        Parameters:
            Required fields:
                - `network` (str): user Teleco ID . (format :: MTN, GLO, AIRTEL, MTN)

        returns:
        - JSONDict: The response data from thr squad API.
        """
        cap_network = network.upper()
        endpoint = f"/vending/data-bundles?network={cap_network}"
        return cls().requests._send_request(
            endpoint=endpoint,
            method ="get"
        )

    @classmethod
    def data_bundles(cls, bundles_data:dict):
        """
        This method is use to vend data.

        Parameters:
         - `bundles_data` (dict): A dictionary containing data to vend data.
            Required fields:
                - `phone_number` (str): 11 digit phone number. (format :: "08139011943")
                - `amount` (int): Amount of the corresponding plan_code
                - `plan_code` (str): The plan code is gotten from the get_data_bundles method. (format:: "1001")

        returns:
        - JSONDict: The response data from thr squad API.

        """
        endpoint = "/vending/purchase/data"
        return cls().requests._send_request(
            endpoint=endpoint,
            method="post",
            data=bundles_data
        )
    
    
    @classmethod
    def all_vending_transaction(cls,page:int, perPge:int, action:str):
        """
        All transactions done by merchant.

        Parameters:
        Required fields:
              - `page` (int): The page of the transaction merchant want to view.
              - `perPage` (int): Number of transaction merchant want to view per page.
              - `action` (str): The type of transaction merchant want to see. (format :: "debit")

        returns:
        - JSONDict: The response data from thr squad API.
        """
        endpoint = f"/vending/transactions?page={page}&perPage={perPge}&action={action}"
        return cls().requests._send_request(
            endpoint=endpoint,
            method = "get"
        )