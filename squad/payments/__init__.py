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
    
    @classmethod
    def generate_payment_link(cls, payment_data: dict):
        """ Creating Payment Link 

        Parameters
            - `payment_data` (dict): A dictionary containing payment link information.
                ## Required:
                    - `name` (str): Title/Name of the Payment Link.
                    - `hash` (str): Unique string that identifies each payment Link (cannot exceed 255 characters).
                    - `link_status` (int): Value can be 0 or 1. 1 - Active, 0 - Inactive.
                    - `expire_by` (str): sample: 2021-04-26T11:22:08.587Z.
                    - `amount` (int): Amount must be in the lowest currency. (kobo for Naira transactions and cent for Dollar transaction) i.e 40000 = 400NGN.
                    - `currency_id` (str): USD or NGN (USD - US Dollars & NGN - Nigerian Naira).
                    - `description` (str): This describes what the payment link does.
                   Optional:
                    - `redirect_link` (str): URL to be redirected to after payment. When this is not provided, the default redirect URL set on your dashboard will be used.
                    - `return_message` (str): Message to be displayed to the customer after payment via the link.
        """
        return cls().requests._send_request(f"/payment_link/otp","post",data=payment_data)
    
    @classmethod
    def refund(cls, data: dict):
        """ Initiate refund process on a successful transaction.

        Parameters
            - `payment_data` (dict): A dictionary containing payment link information.
                ## Required:
                    - `gateway_transaction_ref` (str): Unique reference that uniquely identifies the medium of payment and can be obtained from  the webhook notification sent to you.
                    - `transaction_ref` (str): unique reference that identifies a transaction. Can be obtained from the dashboard or the webhook notification sent to you.
                    - `refund_type` (str): The value of this parameter is either "Full" or "Partial".
                    - `reason_for_refund` (str): Reason for initiating the refund.
                
                   Optional:
                    - `refund_amount` (str): Refund amount is in kobo or cent. This is only required for "Partial" refunds.
        """
        return cls().requests._send_request(f"/transaction/refund","post",data=data)
    
  
    
  