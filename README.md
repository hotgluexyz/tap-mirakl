# tap-mirakl

`tap-mirakl` is a Singer tap for [Mirakl Connect](https://www.mirakl.com), the commerce platform for marketplace and dropship operations.

Built with the [Hotglue Singer SDK](https://github.com/hotgluexyz/HotglueSingerSDK) for Singer Taps.

## Installation

```bash
pip install tap-mirakl
```

Or install directly from the repo:

```bash
pip install git+https://github.com/hotgluexyz/tap-mirakl.git
```

## Configuration

### Config fields

| Field | Required | Description |
|---|---|---|
| `client_id` | Yes | OAuth2 client ID from Mirakl Connect |
| `client_secret` | Yes | OAuth2 client secret from Mirakl Connect |
| `start_date` | No | Earliest record date to sync (ISO 8601, e.g. `2024-01-01T00:00:00Z`) |

### Example `config.json`

```json
{
  "client_id": "<your-client-id>",
  "client_secret": "<your-client-secret>",
  "start_date": "2024-01-01T00:00:00Z"
}
```

Run `tap-mirakl --about` to see all supported settings.

## Source Authentication and Authorization

This tap uses the **OAuth 2.0 client credentials** flow. Credentials are obtained from the [Mirakl Connect](https://miraklconnect.com) dashboard under your integration settings. The token endpoint is `https://auth.mirakl.net/oauth/token` and tokens are refreshed automatically.

## Supported Streams

| Stream | Replication | Primary Key | Description |
|---|---|---|---|
| `products` | Full Table | `id` | Full product catalog from the Mirakl Connect seller account |

## Usage

```bash
# Show version
tap-mirakl --version

# Show help
tap-mirakl --help

# Discover available streams
tap-mirakl --config config.json --discover > catalog.json

# Run a full sync
tap-mirakl --config config.json --catalog catalog.json
```

## Developer Resources

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install the tap in editable mode with dev dependencies
pip install -e .
pip install ruff pytest

# Run linting
ruff check .

# Run tests (requires .secrets/config.json)
pytest tap_mirakl/tests/
```
