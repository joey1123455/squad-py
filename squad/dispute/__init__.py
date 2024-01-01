from squad._squad import SquadClient

class Dispute(SquadClient):
    """
    ## Disputes & Chargebacks
    This contains a list of APIs that allow you get all disputes raised on your transaction, reject the claim with an evidence or accept the claim and accept a charge back to be performed
    """
    @classmethod
    def get_dispute(cls):
        """
        GET ALL DISPUTES\n
        This API is used to get all disputes on your transactions raised by your customers.
        """
        return cls().requests._send_request(f"/dispute","get")