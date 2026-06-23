"""Mirakl tap class."""

from typing import List

from hotglue_singer_sdk import Stream, Tap
from hotglue_singer_sdk import typing as th

from tap_mirakl.streams import ProductsStream

STREAM_TYPES = [
    ProductsStream,
]


class TapMirakl(Tap):
    """Mirakl tap class."""

    name = "tap-mirakl"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "client_id",
            th.StringType,
            required=True,
            description="OAuth2 client ID from Mirakl Connect.",
        ),
        th.Property(
            "client_secret",
            th.StringType,
            required=True,
            description="OAuth2 client secret from Mirakl Connect.",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync.",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]


if __name__ == "__main__":
    TapMirakl.cli()
