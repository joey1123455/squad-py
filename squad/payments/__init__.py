from squad._squad import SquadClient

class PaymentTransaction(SquadClient):
    """ Squad Payments Base """

    @classmethod
    def initiate_transaction(cls, payment_data: dict):
        """
        Initiate a transaction.

        Parameters:
          - `payment_data` (dict): A dictionary containing payment information.
              Required fields:
                - `email` (str): Recipient's email address.
                - `amount` (integer): The amount of the payment.
                - `initiate_type` (str): Type of initiation (default is "inline").
                - `currency` (str): Currency code for the payment (Allowed value is either "USD" or "NGN").
              Optional fields:
                - `transaction_ref` (str): An alphanumeric string that uniquely identifies a transaction.
                - `customer_name` (str): Name of Customer carrying out the transaction.
                - `callback_url` (str): Sample: http://squadco.com.
                - `payments_channels` (list): An array of payment channels to control what channels you want to make available for the user to make a payment with. Available channels include; ['card', 'bank' , 'ussd','transfer'].
                - `metadata` (dict): Object that contains any additional information that you want to record with the transaction. The custom fields in the object will be returned via webhook and the payment verification endpoint..
                - `pass_charge` (bool): the charges is being paid by the customer (default is False).
                - `sub_merchant_id` (str): This is the ID of a merchant that was created by an aggregator which allows the aggregator initiate a transaction on behalf of the submerchant.

                - `is_recurring` (bool): This allows you charge a card without collecting the card information each time

        Returns:
        - JSONDict: The response data from the Squad API.
        """
        return cls().requests._send_request("/transaction/initiate","post",data=payment_data)

    @classmethod
    def charge_card(cls, payment_data: dict):
        """
        Charge Card.
        This allows you charge a card using the token generated during the initial transaction which was sent via webhook

        Parameters:
         - `payment_data` (dict): A dictionary containing payment information.
              Required fields:
                - `amount` (int): Recipient's email address.
                - `token_id` (str): A unique tokenization code for each card transaction and it is returned via the webhook for first charge on the card.
              Optional fields:
                - `transaction_ref` (str): Unique case-sensitive transaction reference. If you do not pass this parameter, Squad will generate a unique reference for you.

        Returns:
        - JSONDict: The response data from the Squad API.
        """
        return cls().requests._send_request("/transaction/charge_card","post",data=payment_data)
    
    @classmethod
    def verify_transaction(cls, transaction_ref: str):
        """
        Verify Transaction.
        This is an endpoint that allows you to query the status of a particular transaction using the unique transaction reference attached to the transaction.
        Parameters:
          Required fields:
            - `transaction_ref` (str): Unique transaction reference that identifies each transaction
              
        Returns:
        - JSONDict: The response data from the Squad API.
        """
        return cls().requests._send_request(f"/transaction/verify/{transaction_ref}","get")
    
  