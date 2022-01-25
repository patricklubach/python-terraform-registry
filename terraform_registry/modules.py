from dataclasses import dataclass
from typing import Any

from . import helpers

# from requests import Response, request


@dataclass
class Modules:
    """Base class for a Terraform Registry Module service."""

    name: str = "modules.v1"

    def download(
        self, namespace: str, name: str, provider: str, version: str
    ) -> str:
        """Returns the download url for a single module."""

        endpoint = "download"
        response = helpers.call(
            self.name, namespace, name, provider, version, endpoint
        )
        return response.headers.get("x-terraform-get", "")

    def get(
        self, namespace: str, name: str, provider: str, version: str
    ) -> str:
        response = helpers.call(self.name, namespace, name, provider, version)
        return response.json()

    def latest(
        self, namespace: str, name: str, offset: int = 0
    ) -> dict[str, Any]:
        """Returns the latest version of a single module."""

        params: dict[str, Any] = {"offset": offset}
        response = helpers.call(self.name, namespace, name, params=params)
        return response.json()

    def latest_provider(
        self, namespace: str, name: str, provider: str
    ) -> dict[str, Any]:
        """
        Returns the latest versions of Terraform providers
        that are available for the module.
        """

        response = helpers.call(self.name, namespace, name, provider)
        return response.json()

    def list(
        self,
        namespace: str = "",
        offset: int = 0,
        provider: str = "",
        verified: bool = True,
    ) -> dict[str, Any]:
        """Returns list of modules according to criteria."""

        params: dict[str, Any] = {}
        params["offset"] = offset
        params["provider"] = provider
        params["verified"] = verified

        response = helpers.call(self.name, namespace, params=params)
        return response.json()

    def search(
        self,
        name: str,
        offset: int = 0,
        provider: None = None,
        namespace: str = "",
        verified: bool = True,
    ) -> dict[str, Any]:
        """Returns modules, that matches criteria."""

        endpoint = "search"

        params: dict[str, Any] = {}
        params["q"] = name
        params["namespace"] = namespace
        params["offset"] = offset
        params["provider"] = provider
        params["verified"] = verified

        response = helpers.call(self.name, endpoint, params=params)
        return response.json()

    def versions(
        self, namespace: str, name: str, provider: str
    ) -> dict[str, Any]:
        """Returns all available versions of a module."""
        endpoint = "versions"

        response = helpers.call(self.name, namespace, name, provider, endpoint)
        return response.json()
