"""REST client handling, including MiraklStream base class."""

from typing import Any, Dict, Optional

from hotglue_singer_sdk.streams import RESTStream
from memoization import cached

from tap_mirakl.auth import MiraklAuthenticator


class MiraklStream(RESTStream):
    """Mirakl stream class (base)."""

    url_base = "https://miraklconnect.com/api"
    primary_keys = ["id"]
    replication_key = None
    records_jsonpath = "$.data[*]"
    next_page_token_jsonpath = "$.next_page_token"
    limit = 100

    @property
    @cached
    def authenticator(self) -> MiraklAuthenticator:
        """Return a new authenticator object."""
        return MiraklAuthenticator.create_for_stream(self)

    def get_url_params(
        self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        if next_page_token:
            params["page_token"] = next_page_token
        if self.limit:
            params["limit"] = self.limit
        return params
