from requests import request

BASE_URL: str = "https://registry.terraform.io"
DISCOVERY_PATH = "/.well-known/terraform.json"
DISCOVERY_URI: str = f"{BASE_URL}{DISCOVERY_PATH}"


def list() -> dict[str, str]:
    """Returns all the currently registered services."""

    response = request("GET", DISCOVERY_URI)
    return response.json()
