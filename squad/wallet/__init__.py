from squad._squad import SquadClient

class Wallet(SquadClient):
    """ Squad Wallet Base"""

    @classmethod
    def balance(cls, currency_id: str ="NGN"):
        """
        This endpoint allows you get your Squad Wallet Balance.\n
        Please be informed that the wallet balance is in KOBO. (Please note that you can't get wallet balance for Dollar transactions)

        Parameters
            
        ## Required:
                - `currency_id` (str): It only takes the value "NGN". (Please note that you can't get wallet balance for Dollar transactions)
        """
        return cls().requests._send_request(f"/merchant/balance","get",data={"currency_id": currency_id})