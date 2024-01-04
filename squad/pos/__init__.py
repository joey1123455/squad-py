"""
Squad POS Python Client.

This module provides a Python client for interacting with the Squad POS API. Squad POS offers functionalities related to Point of Sale (POS) operations, including managing transactions, creating terminals, and retrieving information about terminals associated with your Squad account.

Usage:
- Import the `SquadPOS` class from this module.
- Instantiate the `SquadPOS` class with the required parameters, including the secret key obtained from the Squad Dashboard.
- Use the various methods of the `SquadPOS` class to perform specific POS-related API operations.

Example:
```python
# Import the SquadPOS class
from squad import SquadPOS

# Create an instance of SquadPOS
pos_instance = SquadPOS(secret_key='your_secret_key')

# Get all Squad POS transactions
transactions_data = {
    'perPage': 10,
    'page': 1,
    'date_from': '2022-01-01',
    'date_to': '2022-02-01',
    'sort_by': 'createdAt',
    'sort_by_dir': 'ASC'
}
all_transactions = pos_instance.get_all_transaction(**transactions_data)

# Create a SquadPOS terminal
terminal_data = {
    'email': 'terminal@example.com',
    'name': 'Terminal Name',
    'phone': '12345678901',
    'location_id': 123
}
created_terminal = pos_instance.create_terminal(terminal_dict=terminal_data)

# Get all SquadPOS terminals
terminals_data = {
    'page': 1,
    'perPage': 10,
    'location_id': 456,
    'sort_by': 'createdAt',
    'sort_by_dir': 'DESC',
    'date_from': '2022-01-01',
    'date_to': '2022-02-01',
    'active': True
}
all_terminals = pos_instance.get_all_terminals(filter_dict=terminals_data)
```
"""

from squad._squad import SquadClient

class SquadPOS(SquadClient):
    """ Squad POS Base"""

    @classmethod
    def get_all_transaction(cls, perPage:int, page:int, filter_dict: dict = {}):
        """
        Fetch all your Squad POS Transactions.

        Parameters
        ----------
        per_page : int
            Number of records per page.
        page : int
            Page number to display.
        filter_dict : dict, optional
            A dictionary containing filter information.
            
            Required:
            - `page` (int): Page number to display.
            - `per_page` (int): Number of records per page.
            
            Optional:
            - `date_from` (date): Format: YYYY-MM-DD. Start date for filtering.
            - `date_to` (date): Format: YYYY-MM-DD. End date for filtering.
            - `sort_by` (str): Sorting parameter. Can have a value of "createdAt".
            - `sort_by_dir` (str): Arranges the transactions in ascending or descending order.
              Possible values are "ASC" for ascending order, "DESC" for descending order.
              
        Returns
        -------
        dict
            JSON response containing Squad POS transactions.

        Example
        -------
        >>> SquadPOS.get_all_transactions(per_page=10, page=1, filter_dict={"sort_by": "createdAt"})
        """
        return cls().requests._send_request(f"/softpos/transactions?perPage={perPage}&page={page}","get",data=filter_dict)
    
    @classmethod
    def create_terminal(cls, terminal_dict: dict = {}):
        """
        Create Terminal.

        This API allows you to create multiple SquadPOS terminals associated with your Squad account.

        Parameters
        ----------
        terminal_dict : dict, required
            A dictionary containing terminal information.
            
            Required:
            - `email` (str): Unique email to be associated with the terminal being created.
            - `name` (str): Name to be associated with the terminal.
            - `phone` (str): 11-digit phone number to be associated with the terminal.
            - `location_id` (int): Unique ID that identifies a particular location.

        Returns
        -------
        dict
            JSON response containing information about the created terminal.

        Example
        -------
        >>> terminal_info = {"email": "example@example.com", "name": "Terminal1", "phone": "12345678901", "location_id": 1}
        >>> SquadPOS.create_terminal(terminal_info)
        """
        return cls().requests._send_request(f"/softpos/terminal","post",data=terminal_dict)
    
    @classmethod
    def get_all_terminals(cls, filter_dict: dict = {}):
        """
        See all SquadPOS terminals created and associated with your account.

        Parameters
        ----------
        filter_dict : dict, optional
            A dictionary containing filter information.
            
            Required:
            - `page` (int): Page number to display.
            - `per_page` (int): Number of records per page.
            
            Optional:
            - `location_id` (int): ID that identifies a location.
            - `sort_by` (str): Sorting parameter. Can have a value of "createdAt".
            - `sort_by_dir` (str): Arranges the transactions in ascending or descending order.
              Possible values are "ASC" for ascending order, "DESC" for descending order.
            - `date_from` (date): Format: YYYY-MM-DD. Start date for filtering.
            - `date_to` (date): Format: YYYY-MM-DD. End date for filtering.
            - `active` (bool): Takes a value of "True" or "False".

        Returns
        -------
        dict
            JSON response containing information about SquadPOS terminals.

        Example
        -------
        >>> SquadPOS.get_all_terminals(filter_dict={"sort_by": "createdAt", "sort_by_dir": "ASC"})
        """
        return cls().requests._send_request(f"/softpos/terminals","get",data=filter_dict)
    