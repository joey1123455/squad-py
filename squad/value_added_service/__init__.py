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