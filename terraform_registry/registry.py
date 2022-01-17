import copy
from dataclasses import dataclass
from typing import Any

from requests import request


@dataclass
class Service:
    """Base class for a Terraform module."""

    base_url: str = "https://registry.terraform.io"

    def endpoint(self, service_name: str) -> str:
        services = self.list()
        return services.get(service_name, "")

    def list(self) -> dict[str, str]:
        """Returns all the currently registered services."""

        discovery_path = "/.well-known/terraform.json"
        response = request("GET", f"{self.base_url}{discovery_path}")
        return response.json()

    def url(self, service_name: str):
        return f"{self.base_url}{self.endpoint(service_name)}"


@dataclass
class Module:
    """Base class for a Terraform module."""

    base_url: str

    def _call(self, *args: list[str], **kwargs: dict[str, Any]):
        path: list[str] = [arg for arg in args]
        base_url = self.base_url.rstrip("/")
        url = "/".join(path.insert(0, base_url))

        params: dict[str, Any] = {}

        for k, v in kwargs:
            params[k] = v

        return request("GET", url, params=params)

    def download(
        self, namespace: str, name: str, provider: str, version: str
    ) -> str:
        endpoint = "download"
        response = response = request(
            "GET",
            f"{self.base_url}/{namespace}/{name}/{provider}/{version}/{endpoint}",
        )
        return response.headers.get("x-terraform-get")

    def get(
        self, namespace: str, name: str, provider: str, version: str
    ) -> str:
        url = f"{self.base_url}/{namespace}/{name}/{provider}/{version}"
        print("calling", url)
        response = response = request("GET", url)
        return response.json()

    def latest(
        self, namespace: str, name: str, offset: int = 0
    ) -> dict[str, Any]:

        params: dict[str, Any] = {"offset": offset}
        response = request(
            "GET", f"{self.base_url}/{namespace}/{name}", params=params
        )
        return response.json()

    def latest_provider(
        self, namespace: str, name: str, provider: str
    ) -> dict[str, Any]:
        response = request(
            "GET", f"{self.base_url}/{namespace}/{name}/{provider}"
        )
        return response.json()

    def list(
        self,
        namespace: str = "",
        offset: int = 0,
        provider: None = None,
        verified: bool = True,
    ):

        params: dict[str, Any] = {}
        params["offset"] = offset
        params["provider"] = provider
        params["verified"] = verified

        url = f"{self.base_url}/{namespace}"
        response = request("GET", url, params=params)

        return response.json()

    def search(
        self,
        name: str,
        offset: int = 0,
        provider: None = None,
        namespace: str = "",
        verified: bool = True,
    ) -> dict[str, Any]:
        endpoint = "search"

        params: dict[str, Any] = {
            "name": name,
            "namespace": namespace,
            "offset": offset,
            "provider": provider,
        }

        response = request("GET", f"{self.base_url}/{endpoint}", params=params)
        return response.json()

    def versions(
        self, namespace: str, name: str, provider: str
    ) -> dict[str, Any]:
        endpoint = "versions"
        url = f"{self.base_url}/{namespace}/{name}/{provider}/{endpoint}"
        response = request("GET", url)
        return response.json()


@dataclass
class Provider:
    """Base class for a Terraform provider."""

    pass
