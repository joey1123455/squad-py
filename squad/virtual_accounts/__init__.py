"""
VirtualAccounts Module
=====================

Subclass of SquadClient representing the Squad Virtual Accounts API.

Squad Virtual Accounts API allows you to create and reserve bank account numbers for receiving payments from your customers.
Please note that there is a new compliance rule put in place to mitigate against fraud. As a result, all virtual accounts must carry a slug as a prefix to the name.
The slug must be a portion of your business name or abbreviations of your business name as one word. Please note that slash (/) is not allowed and only hyphen can be used.
Please be informed that all accounts without the prefix will be flagged by our compliance and fraud team and might ultimately be closed.

Methods
-------
create_customer_virtual_account(customer_data: dict) -> JSONDict:
    
    Creating Virtual Accounts for Customers.

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
            - `customer_identifier` (str): unique customer identifier as given by the merchant.
        Optional fields:
            - `beneficiary_account` (str): Beneficiary Account is the 10 Digit Bank Account Number (GTBank) provided by the Merchant 
              where money sent to this Virtual account is paid into. 
              Please note that when the beneficiary account is not provided, money paid into this virtual account go into your wallet 
              and will be paid out/settled in T+1 settlement time.

    Returns:
    - JSONDict: The response data from the Squad API.

    Example:
    ```python
    customer_data = {
        "first_name": "John",
        "last_name": "Doe",
        "middle_name": "M",
        "mobile_num": "08012345678",
        "dob": "01/01/1990",
        "email": "john.doe@example.com",
        "bvn": "12345678901",
        "gender": "1",
        "address": "123 Main Street",
        "customer_identifier": "ABC123",
        "beneficiary_account": "1234567890"
    }
    response = VirtualAccounts.create_customer_virtual_account(customer_data)
    print(response)
    ```

create_business_virtual_account(business_data: dict) -> JSONDict:
    
    Creating Virtual Accounts for Business.

    Parameters:
    - `business_data` (dict): A dictionary containing customer information.
        Required fields:
            - `bvn` (str): Bank Verification Number.
            - `business_name` (str): Name of Business/Customer.
            - `customer_identifier` (str): An alphanumeric string used to identify a customer/business in your system 
              which will be tied to the virtual account being created.
            - `mobile_num` (str): 08012345678 (doesn't take more than 11 digits).
        Optional fields:
            - `beneficiary_account` (str): Beneficiary Account is the 10 Digit Bank Account Number (GTBank) provided by the Merchant 
              where money sent to this Virtual account is paid into. 
              Please note that when the beneficiary account is not provided, money paid into this virtual account go into your wallet 
              and will be paid out/settled in T+1 settlement time.

    Returns:
    - JSONDict: The response data from the Squad API.

    Example:
    ```python
    business_data = {
        "bvn": "12345678901",
        "business_name": "ABC Corporation",
        "customer_identifier": "ABC123",
        "mobile_num": "08012345678",
        "beneficiary_account": "1234567890"
    }
    response = VirtualAccounts.create_business_virtual_account(business_data)
    print(response)
    ```
    

query_merchant_transactions() -> JSONDict:
    
    Query All Merchant's Transactions.

    Returns:
    - JSONDict: The response data from the Squad API.

    Example:
    ```python
    response = VirtualAccounts.query_merchant_transactions()
    print(response)
    ```
    

query_merchant_transaction_with_filters(filter_data: dict = {}) -> JSONDict:
    
    Query All Merchant Transactions with Multiple Filters.

    Parameters:
    - `filter_data` (dict): A dictionary containing filter information.
        Optional:
            - `page` (int): Page Number to Display.
            - `perPage` (int): Number of records per Page.
            - `virtualAccount` (int): a unique 10-digit virtual account number.
            - `customerIdentifier` (str): Unique Identifier used to create/identify a customer's virtual account.
            - `startDate` (date): MM-DD-YYYY E.G: 09-19-2022.
            - `endDate` (date): MM-DD-YYYY E.G: 09-19-2022.
            - `transactionReference` (str): Unique Identifier of a transaction.
            - `session_id` (str): Unique ID that identifies all NIP transactions.
            - `dir` (str): Takes two possible values: "DESC" and "ASC". "DESC" - descending order "ASC" - ascending order.

    Returns:
    - JSONDict: The response data from the Squad API.

    Example:
    ```python
    filter_data = {"page": 1, "perPage": 10, "dir": "ASC"}
    response = VirtualAccounts.query_merchant_transaction_with_filters(filter_data)
    print(response)
    ```
    

get_customer_by_virtual_account_number(virtual_account_number: str) -> JSONDict:
    
    Get Customer Details by Virtual Account Number.

    Parameters:
    - `virtual_account_number` (str): The Virtual Account Number.

    Returns:
    - JSONDict: The response data from the Squad API.

    Example:
    ```python
    virtual_account_number = "1234567890"
    response = VirtualAccounts.get_customer_by_virtual_account_number(virtual_account_number)
    print(response)
    ```
    

get_customer_using_customer_identifier(customer_identifier: str) -> JSONDict:
    
    Get Customer Details Using Customer Identifier.

    Parameters:
    - `customer_identifier` (str): The Customer Identifier.

    Returns:
    - JSONDict: The response data from the Squad API.

    Example:
    ```python
    customer_identifier = "ABC123"
    response = VirtualAccounts.get_customer_using_customer_identifier(customer_identifier)
    print(response)
    ```
    

update_customer_bvn(customer_data: dict = {}) -> JSONDict:
    
    Update Customer's BVN and Unfreeze Transaction.

    Parameters:
    - `customer_data` (dict): A dictionary containing customer information.
        Optional:
            - `customer_bvn` (str): Bank Verification Number of Customer.
            - `customer_identifier` (str): Unique number given to the customer by the merchant.
            - `phone

_number` (str): customer's phone number.

    Returns:
    - JSONDict: The response data from the Squad API.

    Example:
    ```python
    customer_data = {"customer_bvn": "12345678901", "customer_identifier": "ABC123", "phone_number": "08012345678"}
    response = VirtualAccounts.update_customer_bvn(customer_data)
    print(response)
    ```
    

query_all_merchant_virtual_account(filter_data: dict = {}) -> JSONDict:
    
    Query All Merchant's Virtual Accounts.

    Parameters:
    - `filter_data` (dict): A dictionary containing filter information.
        Optional:
            - `page` (int): Page Number to Display.
            - `perPage` (int): Number of records per Page.
            - `startDate` (date): MM-DD-YYYY E.G: 09-19-2022.
            - `endDate` (date): MM-DD-YYYY E.G: 09-19-2022.

    Returns:
    - JSONDict: The response data from the Squad API.

    Example:
    ```python
    filter_data = {"page": 1, "perPage": 10, "startDate": "09-19-2022", "endDate": "09-19-2022"}
    response = VirtualAccounts.query_all_merchant_virtual_account(filter_data)
    print(response)
    ```
    

update_beneficiary_account(beneficiary_data: dict) -> JSONDict:
    
    Update Beneficiary Account.

    Parameters:
    - `beneficiary_data` (dict): A dictionary containing beneficiary information.
        Required:
            - `beneficiary_account` (str): 10 digit valid NUBAN account number.
            - `virtual_account_number` (str): The Virtual account number whose beneficiary account is to be updated.

    Returns:
    - JSONDict: The response data from the Squad API.

    Example:
    ```python
    beneficiary_data = {"beneficiary_account": "1234567890", "virtual_account_number": "1234567890"}
    response = VirtualAccounts.update_beneficiary_account(beneficiary_data)
    print(response)
    ```
    

simulate_payment(payment_data: dict) -> JSONDict:
    
    Simulate Payment.

    Parameters:
    - `payment_data` (dict): A dictionary containing beneficiary information.
        Required:
            - `virtual_account_number` (str): The Virtual account number whose beneficiary account is to be updated.
        Optional:
            - `amount` (str): Simulated Amount.

    Returns:
    - JSONDict: The response data from the Squad API.

    Example:
    ```python
    payment_data = {"virtual_account_number": "1234567890", "amount": "50000"}
    response = VirtualAccounts.simulate_payment(payment_data)
    print(response)
    ```
    

get_webhook_error_logs(filter_data: dict = {}) -> JSONDict:
    
    Get Webhook Error Log.

    Parameters:
    - `filter_data` (dict): A dictionary containing filter information.
        Optional:
            - `page` (int): Page Number to Display.
            - `perPage` (int): Number of records per Page.

    Returns:
    - JSONDict: The response data from the Squad API.

    Example:
    ```python
    filter_data = {"page": 1, "perPage": 10}
    response = VirtualAccounts.get_webhook_error_logs(filter_data)
    print(response)
    ```
    

delete_webhook_error_logs(transaction_ref: str) -> JSONDict:
    
    Delete Webhook Error Log.

    Parameters:
    - `transaction_ref` (str): Unique Transaction Ref that identifies each virtual account 
      and is obtained from the retrieved webhook error log.

    Returns:
    - JSONDict: The response data from the Squad API.

    Example:
    ```python
    transaction_ref = "ABC123"
    response = VirtualAccounts.delete_webhook_error_logs(transaction_ref)
    print(response)
    ```
    

query_customer_transaction_by_customer_identifier(customer_identifier: str) -> JSONDict:
    
    Query Customer Transaction by Customer Identifier.

    Parameters:
    - `customer_identifier` (str): Unique Customer Identifier that identifies each virtual account.

    Returns:
    - JSONDict: The response data from the Squad API.

    Example:
    ```python
    customer_identifier = "ABC123"
    response = VirtualAccounts.query_customer_transaction_by_customer_identifier(customer_identifier)
    print(response)
    ```
    

Attributes
----------
Inherited from SquadClient.
"""



from squad._squad import SquadClient


class VirtualAccounts(SquadClient):
    """
    Squad Virtual Accounts API allows you to create and reserve bank account numbers for receiving payments from your customers.\n
    Please note that there is a new compliance rule put in place to mitigate against fraud. As a result, all virtual accounts must carry a slug as a prefix to the name.\n The slug must be a portion of your business name or abbreviations of your business name as one word. Please note that slash (/) is not allowed and only hyphen can be used.\n
    Please be informed that all accounts without the prefix will be flagged by our compliance and fraud team and might ultimately be closed.
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
        return cls().requests._send_request("/virtual-account","post",data=customer_data)

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
        return cls().requests._send_request("/virtual-account/business","post",data=business_data)

    @classmethod
    def query_merchant_transactions(cls):
      """ Query All Merchant's Transactions.\n
          This is an endpoint to query all the merchant transactions over a period of time.


        Parameters:
            - None

        Returns:
                - JSONDict: The response data from the Squad API.
      """
      return cls().requests._send_request(f"/virtual-account/merchant/transactions","get")
    
    @classmethod
    def query_merchant_transaction_with_filters(cls,filter_data:dict ={}):
        """Query All Merchant Transactions with Multiple Filters.\n
        This endpoint allows you query all transactions and filter using multiple parameters like virtual account number, start and end dates, customer Identifier etc


        Parameters
         - `filter_data` (dict): A dictionary containing filter information.
              Optional:
                - `page` (int): Page Number to Display.
                - `perPage` (int): Number of records per Page.
                - `virtualAccount` (int): a unique 10-digit virtual account number.
                - `customerIdentifier` (str): Unique Identifier used to create/identify a customer's virtual account.
                - `startDate` (date): MM-DD-YYYY E.G: 09-19-2022.
                - `endDate` (date): MM-DD-YYYY E.G: 09-19-2022.
                - `transactionReference` (str): Unique Identifier of a transaction.
                - `session_id` (str): Unique ID that identifies all NIP transactions.
                - `dir` (str): Takes two possible values: "DESC" and "ASC". "DESC" - descending order "ASC" - ascending order.
            
          
        """
        return cls().requests._send_request(f"/virtual-account/merchant/transactions/all","get",data=filter_data)
    
    @classmethod
    def get_customer_by_virtual_account_number(cls,virtual_account_number: str):
        """
        Get Customer Details by Virtual Account Number\n
        This is an endpoint to retrieve the details of a customer using the Virtual Account Number
        """
        return cls().requests._send_request(f"/virtual-account/customer/{virtual_account_number}","get")
    
    @classmethod
    def get_customer_using_customer_identifier(cls,customer_identifier: str):
        """
        Get Customer Details Using Customer Identifier\n
        This is an endpoint to retrieve the details of a customer's virtual account using the Customer Identifier
        """
        return cls().requests._send_request(f"/virtual-account/{customer_identifier}","get")
    
    @classmethod
    def update_customer_bvn(cls, customer_data: dict ={}):
        """
        Update Customer's BVN and Unfreeze Transaction


        Parameters
         - `customer_data` (dict): A dictionary containing customer  information.
              Optional:
                - `customer_bvn` (str): Bank Verification Number of Customer.
                - `customer_identifier` (str): Unique number given to customer by merchant.
                - `phone_number` (str): customer's phone number.
        """
        return cls().requests._send_request(f"/virtual-account/update/bvn","patch",data=customer_data)
    
    @classmethod
    def query_all_merchant_virtual_account(cls, filter_data: dict = {}):
        """ Query All Merchant's Virtual Accounts.\n
            This is an endpoint to look-up the virtual account numbers related to a merchant.

        Parameters
         - `filter_data` (dict): A dictionary containing filter information.
              Optional:
                - `page` (int): Page Number to Display.
                - `perPage` (int): Number of records per Page.
                - `startDate` (date): MM-DD-YYYY E.G: 09-19-2022.
                - `endDate` (date): MM-DD-YYYY E.G: 09-19-2022.
        """

        return cls().requests._send_request(f"/virtual-account/merchant/accounts","get",data=filter_data)
    
    @classmethod
    def update_beneficiary_account(cls, beneficiary_data: dict):
        """
        Update Beneficiary Account
        
        Parameters
            - `beneficiary_data` (dict): A dictionary containing beneficiary information.
                ## Required:
                    - `beneficiary_account` (str): 10 digit valid NUBAN account number.
                    - `virtual_account_number` (str): The Virtual account number whose beneficiary account is to be updated.
        """

        return cls().requests._send_request("/virtual-account/update/beneficiary/account","patch",data=beneficiary_data)
    
    @classmethod
    def simulate_payment(cls, payment_data:dict):
        """ 
        Simulate Payment.\n
        This is an endpoint to simulate payments 


        Parameters
            - `payment_data` (dict): A dictionary containing beneficiary information.
                ## Required:
                    - `virtual_account_number` (str): The Virtual account number whose beneficiary account is to be updated.
                   Optional:
                    - `amount` (str): Simulated Amount.
        """
        return cls().requests._send_request("/virtual-account/simulate/payment","post",data=payment_data)
    
    @classmethod
    def get_webhook_error_logs(cls, filter_data:dict = {}):
        """ 
        Get Webhook Error Log

        Parameters
         - `filter_data` (dict): A dictionary containing filter information.
              Optional:
                - `page` (int): Page Number to Display.
                - `perPage` (int): Number of records per Page.
        """
        return cls().requests._send_request(f"/virtual-account/webhook/logs","get",data=filter_data)
    
    @classmethod
    def delete_webhook_error_logs(cls, transaction_ref: str):
        """ 
        Delete Webhook Error Log

        Parameters
        ## Required:
            - `transaction_ref` (str): Unique Transaction Ref that identifies each virtual account and gotten from the retrieved webhook error log.
        """
        return cls().requests._send_request(f"/virtual-account/webhook/logs/{transaction_ref}","delete")
    
    @classmethod
    def query_customer_transaction_by_customer_identifier(cls, customer_identifier: str):
        """ 
        Query Customer Transaction by Customer Identifier.\n
        This is an endpoint to query the transactions a customer has made. This is done using the customer's identifier which was passed when creating the virtual account.


        Parameters
        ## Required:
            - `customer_identifier` (str):  Unique Customer Identifier that identifies each virtual account
        """
        return cls().requests._send_request(f"/virtual-account/customer/transactions/{customer_identifier}","get")