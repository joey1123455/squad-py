from squad.utils.exceptions import InvalidSecretKey


class SquadClient:
    """ represents a client for interacting with the Squad API  """

    def __init__(
        self,
        secret_key: str,
        base_url: str = "https://sandbox-api-d.squadco.com",
    ):
        if not secret_key:
            raise InvalidSecretKey("you must pass an authorization key (secret key)")

        self.secret_key = secret_key
        self.base_url = base_url
        print(secret_key,base_url)
