import json
import httpx
from abc import abstractmethod
from squad.utils.exceptions import InvalidSecretKey,SquadError
from squad.utils.types import JSONDict
from squad.utils.logging import get_logger

_LOGGER = get_logger(__name__, class_name="SquadRequest")


class SquadClient:
    """represents a client for interacting with the Squad API"""

    def __init__(
        self,
        secret_key: str,
        base_url: str = "https://sandbox-api-d.squadco.com",
    ):
        if not secret_key:
            raise InvalidSecretKey("you must pass an authorization key (secret key)")

        self.secret_key = secret_key
        self.base_url = base_url

    async def _send_request(self, endpoint: str, method="get", params=None):
        """
        The function sends a request to an endpoint.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.secret_key}"}

        payload = await self._request_wrapper(
            url=url,
            method=method,
            request_data=params,
            headers=headers

        )
        response_data = self.parse_json_payload(payload)
        return response_data

    @abstractmethod
    async def _request_wrapper(self, url, method, request_data, headers):
        async with httpx.AsyncClient() as client:
            if method.lower() == "get":
                response = await client.get(url, json=request_data, headers=headers)
            elif method.lower() == "post":
                response = await client.post(url, json=request_data, headers=headers)

            response.raise_for_status()
            return response.text

    @staticmethod
    def parse_json_payload(payload: bytes) -> JSONDict:
        decoded_s = payload.decode("utf-8", "replace")
        try:
            return json.loads(decoded_s)
        except ValueError as exc:
            _LOGGER.error('Can not load invalid JSON data: "%s"', decoded_s)
            raise SquadError("Invalid server response") from exc
