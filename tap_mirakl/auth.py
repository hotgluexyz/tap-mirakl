"""Mirakl Authentication."""

from hotglue_singer_sdk.authenticators import OAuthAuthenticator, SingletonMeta


class MiraklAuthenticator(OAuthAuthenticator, metaclass=SingletonMeta):
    """Authenticator for Mirakl Connect OAuth2 client_credentials."""

    @property
    def oauth_request_body(self) -> dict:
        """Form body for token request."""
        return {
            "grant_type": "client_credentials",
            "client_id": self.config["client_id"],
            "client_secret": self.config["client_secret"],
        }

    @classmethod
    def create_for_stream(cls, stream) -> "MiraklAuthenticator":
        return cls(
            stream=stream,
            auth_endpoint="https://auth.mirakl.net/oauth/token",
        )
