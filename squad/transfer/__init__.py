from squad._squad import SquadClient


class SquadTransfer(SquadClient):
    """
    ## Transfer API
    These are suites of API that allows you move funds from your Squad Wallet to a bank Account.
    """

    @classmethod
    def account_lookup(cls, bank_data: dict):
        """
        This API allows you lookup/confirm the account name of the recipient you intend to credit. This should be done before initiating the transfer.

        Parameters

        ## Required:
                - `bank_code` (str): Unique NIP code that identifies a bank..
                - `account_number` (str): Account number you want to transfer to.
        """
        return cls().requests._send_request(
            f"/payout/account/lookup", "post", data=bank_data
        )

    @classmethod
    def fund_transfer(cls, transfer_data: dict):
        """
        ## Fund Transfer
        This API allows you to transfer funds from your Squad Wallet to the account you have looked up.
        Please be informed that we will not be held liable for mistake in transferring to a wrong account or an account that wasn't looked up.

        ## Transaction Reference:
        Transaction Reference used to initiate a transfer must be unique per transfer. Kindly ensure that you append your merchant ID to the transaction Reference you are creating. This is compulsory as it will throw an error if you don't append it.

        ## For instance:
        If my Squad Merchant ID is SBABCKDY and i want to create a transaction ref for my transfer, then I will have something like:
            - "transaction_reference":"SBABCKDY_12345".

        ## Parameters

        ## Required:
                - `transaction_reference` (str): Unique Transaction Reference used to initiate a transfer. Please ensure that you append your merchant ID to the transaction Reference you are creating. This is compulsory as it will throw an error if you don't append it.
                - `amount` (str): Amount to be transferred. Value is in Kobo.
                - `bank_code`(str): Unique NIP Code that identifies a bank.
                - `account_number` (str): 10-digit NUBAN account number to be transferred to. Must be an account that has been looked up and vetted to be transferred to.
                - `account_name` (str): The account name tied to the account number you are transferring to which you have looked up using our look up API.
                - `currency_id`  (str): Takes only the value "NGN".
                - `remark` (str): A unique remark that will be sent with the transfer.
        """
        return cls().requests._send_request(
            f"/payout/transfer", "post", data=transfer_data
        )

    @classmethod
    def re_query(cls, transaction_reference: str):
        """
        ## Re-query Transfer
        This API allows you re-query the status of a transfer made to know if it was successful, failed, reversed or pending.

        Parameters
        ## Required:
                - `transaction_reference` (str): Unique Transaction Reference used to initiate a transfer. Please ensure that you append your merchant ID to the transaction Reference you are creating. This is compulsory as it will throw an error if you don't append it.
        """
        return cls().requests._send_request(
            f"/payout/requery",
            "post",
            data={"transaction_reference": transaction_reference},
        )

    @classmethod
    def get_all_transfer(cls, filter_data: dict = {}):
        """
        ## Get All Transfers
        This API Allows you retrieve the details of all transfers you have done from your Squad Wallet using this transfer solution.

        Parameters
         - `filter_data` (dict): A dictionary containing filter information.
            Optional:
                - `page` (int): Page Number to Display.
                - `perPage` (int): Number of records per Page.
                - `dir` (str): Allows you sort the records in either ascending or descending order. It takes the value "ASC" or "DESC"
        """
        return cls().requests._send_request(f"/payout/list","get",data=filter_data)
