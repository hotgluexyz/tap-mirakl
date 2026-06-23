"""Stream type classes for tap-mirakl."""

from hotglue_singer_sdk import typing as th

from tap_mirakl.client import MiraklStream

# Reused across standard_prices and discount_prices
_price_object = th.ObjectType(
    th.Property("amount", th.NumberType),
    th.Property("currency", th.StringType),
)

# Reused for titles and descriptions (both are locale+value arrays)
_localized_string_object = th.ObjectType(
    th.Property("locale", th.StringType),
    th.Property("value", th.StringType),
)

# Polymorphic: value type depends on the sibling `type` field (STRING/NUMERIC/BOOLEAN).
_any_type = th.CustomType({"type": ["string", "number", "boolean", "null"]})


class ProductsStream(MiraklStream):
    """Products stream - full catalog from Mirakl Connect."""

    name = "products"
    path = "/products"

    schema = th.PropertiesList(
        th.Property("id", th.StringType),
        th.Property("brand", th.StringType),
        th.Property(
            "gtins",
            th.ArrayType(th.ObjectType(th.Property("value", th.StringType))),
        ),
        th.Property("titles", th.ArrayType(_localized_string_object)),
        th.Property("descriptions", th.ArrayType(_localized_string_object)),
        th.Property(
            "images",
            th.ArrayType(th.ObjectType(th.Property("url", th.StringType))),
        ),
        th.Property(
            "standard_prices",
            th.ArrayType(
                th.ObjectType(
                    th.Property("scope", th.StringType),
                    th.Property("price", _price_object),
                )
            ),
        ),
        th.Property(
            "discount_prices",
            th.ArrayType(
                th.ObjectType(
                    th.Property("scope", th.StringType),
                    th.Property("price", _price_object),
                    th.Property("start_date", th.DateTimeType),
                    th.Property("end_date", th.DateTimeType),
                )
            ),
        ),
        th.Property(
            "quantities",
            th.ArrayType(
                th.ObjectType(
                    th.Property("available_quantity", th.IntegerType),
                    th.Property("warehouse_code", th.StringType),
                )
            ),
        ),
        th.Property(
            "partner_quantities",
            th.ArrayType(
                th.ObjectType(
                    th.Property("available_quantity", th.IntegerType),
                    th.Property("partner_id", th.StringType),
                )
            ),
        ),
        th.Property(
            "attributes",
            th.ArrayType(
                th.ObjectType(
                    th.Property("id", th.StringType),
                    th.Property("name", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("value", _any_type),
                )
            ),
        ),
        th.Property("category", th.ObjectType()),
    ).to_dict()
