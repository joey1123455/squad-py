from squad._squad import SquadClient


class VirtualAccounts(SquadClient):
    """
    ### Squad Virtual Accounts API allows you to create and reserve bank account numbers for receiving payments from your customers.
    ##### Please note that there is a new compliance rule put in place to mitigate against fraud. As a result, all virtual accounts must carry a slug as a prefix to the name. The slug must be a portion of your business name or abbreviations of your business name as one word. Please note that slash (/) is not allowed and only hyphen can be used.
    ##### Please be informed that all accounts without the prefix will be flagged by our compliance and fraud team and might ultimately be closed.
    """

    @classmethod
    def create_customer_virtual_account(cls, customer_data: dict):
        """
            Creating Virtual Accounts for Customers
         Parameters:
          - `customer_data` (dict): A dictionary containing customer information.
              Required fields:
                - `first_name` (str): customer first name.
                - `last_name` (integer): customer last name.
                - `middle_name` (str): customer middle name.
                - `mobile_num` (str): 08012345678 (doesn't take more than 11 digits).
                - `dob` (date): mm/dd/yyyy.
                - `email` (str): customer email.
                - `bvn` (str): BNV is compulsory.
                - `gender` (str): "1" - Male, "2" -Female.
                - `address` (str): customer address.
                - `customer_identifier` (str): unique customer identifier as given by merchant.
                
            Optional fields:
                - `beneficiary_account` (str): Beneficiary Account is the 10 Digit Bank Account Number (GTBank) provided by the Merchant where money sent to this Virtual account is paid into. Please note that when beneficiary account is not provided, money paid into this virtual account go into your wallet and will be paid out/settled in T+1 settlement time..

        Returns:
        - JSONDict: The response data from the Squad API.
        """
        cls().requests._send_request("/virtual-account","post",data=customer_data)

    @classmethod
    def create_business_virtual_account(cls, business_data: dict):
        """
            Creating Virtual Accounts for Business
         Parameters:
          - `business_data` (dict): A dictionary containing customer information.
              Required fields:
                - `bvn` (str): Bank Verification Number.
                - `business_name` (str): Name of Business/Customer.
                - `customer_identifier` (str): An alphanumeric string used to identify a customer/business in your system which will be tied to the virtual account being created.
                - `mobile_num` (str): 08012345678 (doesn't take more than 11 digits).
            
            Optional fields:
                - `beneficiary_account` (str): Beneficiary Account is the 10 Digit Bank Account Number (GTBank) provided by the Merchant where money sent to this Virtual account is paid into. Please note that when beneficiary account is not provided, money paid into this virtual account go into your wallet and will be paid out/settled in T+1 settlement time..

        Returns:
        - JSONDict: The response data from the Squad API.
        """
        cls().requests._send_request("/virtual-account/business","post",data=business_data)
