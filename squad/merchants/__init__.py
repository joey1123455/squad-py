from squad._squad import SquadClient


class SquadMerchant(SquadClient):
    """   
        Aggregator and Sub-merchants.
        This API allows you to be profiled as an aggregator and also create sub-merchants dynamically under your account.
        With this, you are able to initiate transactions from a central point for all businesses or sub merchants under you using the same API keys.
    """

    @classmethod
    def create_sub_users(cls, merchant_data: dict):
        """
        Create Sub-merchants.
        This API is used to create a sub-merchant, the sub-merchant will have its own ID and will automatically have its own view on the dashboard.
      
        Parameters:
            - `merchant_data` (dict): A dictionary containing merchant information.
                Required fields:
                    - `display_name` (str): Name of sub-merchant.
                    - `account_name` (str): Sub-merchant's settlement bank account name.
                    - `account_number` (str): Sub-merchant's settlement account number.
                    - `bank_code` (str): Sub-merchant's settlement bank code. e.g 058.
                    - `bank` (str): Name of sub-merchant's settlement bank e.g GTBank.
                   
                Returns:
                - JSONDict: The response data from the Squad API.
        """
        return cls().requests._send_request("/merchant/create-sub-users","post",data=merchant_data)
    
