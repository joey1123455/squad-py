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
    
    @classmethod
    def get_dispute_upload_url(cls, ticket_id: str, file_name: str):
        """ 
        Get Upload URL\n
        This API is used to get a unique URL to upload an evidence(file) which is a proof or reason to reject a dispute. This is only necessary when we want to reject a dispute.
        

        Parameters
            
        ## Required:
                - `ticket_id` (str)
                - `file_name` (str)
        """
        return cls().requests._send_request(f"/dispute/upload-url/{ticket_id}/{file_name}","get")
    
    @classmethod
    def resolve_dispute(cls, ticket_id: str, dispute_data: dict):
        """ 
        Get Upload URL\n
        This API is used to get a unique URL to upload an evidence(file) which is a proof or reason to reject a dispute. This is only necessary when we want to reject a dispute.
        

        Parameters
            
        ## Required:
                - `ticket_id` (str)
                - `action` (str):  This is the action you want to be taken on the raised dispute. The value of this action can be either "rejected" or "accepted"
        ##   Optional:
                - `file_name` (str): The name of the file uploaded.
        """
        return cls().requests._send_request(f"/dispute/{ticket_id}/resolve","get",data=dispute_data)