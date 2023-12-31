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

        Returns:
        - JSONDict: The response data from the Squad API.
        """
        return cls().requests._send_request("/transaction/initiate","post",data=payment_data)