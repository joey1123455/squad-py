from squad._squad import SquadClient

class SquadPOS(SquadClient):
    """ Squad POS Base"""

    @classmethod
    def get_all_transaction(cls, perPage:int, page:int, filter_dict: dict = {}):
        """
        Fetch all your Squad POS Transactions.

        Parameters
         - `filter_data` (dict): A dictionary containing filter information.
            ## Required:
                    - `page` (int): Page Number to Display.
                    - `perPage` (int): Number of records per Page.
            ## Optional:
                    - `date_from` (date): Format : YYYY-MM-DD Start Date
                    - `date_to`  (date): Format : YYYY-MM-DD End Date
                    - `sort_by` (str): Sorting Parameter. This can have a value of "createdAt".
                    - `sort_by_dir` (str): This arranges the transactions in ascending or descending order. possible values are "ASC" - ascending order "DESC" - descending order
        """
        return cls().requests._send_request(f"/softpos/transactions?perPage={perPage}&page={page}","get",data=filter_dict)
    
    @classmethod
    def create_terminal(cls, terminal_dict: dict = {}):
        """
        Create Terminal\n
        This API allows you to create multiple SquadPOS terminals which are associated to your squad account

        Parameters
         - `filter_data` (dict): A dictionary containing terminal information.
            ## Required:
                    - `email` (str): unique email to be associated to the terminal being created.
                    - `name` (str): Name to be associated to the terminal.
                    - `phone` (str): 11 digit phone number to be associated to the terminal.
                    - `location_id` (int): unique ID that identifies a particular location.
            
        """
        return cls().requests._send_request(f"/softpos/terminal","post",data=terminal_dict)
    
    @classmethod
    def get_all_terminals(cls, filter_dict: dict = {}):
        """
        see all  SquadPOS terminals created and associated to your account.

        Parameters
         - `filter_data` (dict): A dictionary containing filter information.
            ## Required:
                    - `page` (int): Page Number to Display.
                    - `perPage` (int): Number of records per Page.
            ## Optional:
                    - `location_id` (int): an ID that identifies a location
                    - `sort_by` (str): Sorting Parameter. This can have a value of "createdAt".
                    - `sort_by_dir` (str): This arranges the transactions in ascending or descending order. possible values are "ASC" - ascending order "DESC" - descending order
                    - `date_from` (date): Format : YYYY-MM-DD Start Date.
                    - `date_to`  (date): Format : YYYY-MM-DD End Date.
                    - `active` (bool): It takes a value of "True" or "False"

        """
        return cls().requests._send_request(f"/softpos/terminals","get",data=filter_dict)
    