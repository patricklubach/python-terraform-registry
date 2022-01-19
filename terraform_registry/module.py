from dataclasses import dataclass
from typing import Any

from requests import Response, request

from . import utils


@dataclass
class Module:
    """Base class for a Terraform Registry Module service."""

    name: str = "modules.v1"

    def _endpoint(self) -> str:
        """Returns the endpoint path of the given service."""

        services = utils.list()
        return services.get(self.name, "")

    def _uri(self):
        """Returns the full uri of the service."""

        return "/".join([utils.BASE_URL, self._endpoint()])

    def _url(self, *args: str) -> str:
        return "/".join(args)

    def _call(self, *args: str, **kwargs: Any) -> Response:
        """
        Calls the Terraform Registry API with specified parameter
        and returns requests.Response object.
        """

        path = "/".join([arg for arg in args])
        url = self._url(self._uri(), path)
        params: dict[str, Any] = {}

        for key, value in kwargs:
            params[key] = value

        return request("GET", url, params=params)

    def download(
        self, namespace: str, name: str, provider: str, version: str
    ) -> str:
        """Returns the download url for a single module."""

        endpoint = "download"
        response = self._call(namespace, name, provider, version, endpoint)
        return response.headers.get("x-terraform-get", "")

    def get(
        self, namespace: str, name: str, provider: str, version: str
    ) -> str:
        response = self._call(namespace, name, provider, version)
        return response.json()

    def latest(
        self, namespace: str, name: str, offset: int = 0
    ) -> dict[str, Any]:
        """Returns the latest version of a single module."""

        params: dict[str, Any] = {"offset": offset}
        response = self._call(namespace, name, params=params)
        return response.json()

    def latest_provider(
        self, namespace: str, name: str, provider: str
    ) -> dict[str, Any]:
        """
        Returns the latest versions of Terraform providers
        that are available for the module.
        """

        response = self._call(namespace, name, provider)
        return response.json()

    def list(
        self,
        namespace: str = "",
        offset: int = 0,
        provider: None = None,
        verified: bool = True,
    ):
        """Returns list of modules according to criteria."""
        params: dict[str, Any] = {}
        params["offset"] = offset
        params["provider"] = provider
        params["verified"] = verified

        response = self._call(namespace, params=params)
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

        params: dict[str, Any] = {
            "name": name,
            "namespace": namespace,
            "offset": offset,
            "provider": provider,
        }

        response = request(
            "GET", f"{utils.BASE_URL}/{endpoint}", params=params
        )
        return response.json()

    def versions(
        self, namespace: str, name: str, provider: str
    ) -> dict[str, Any]:
        """Returns all available versions of a module."""
        endpoint = "versions"
        url = f"{utils.BASE_URL}/{namespace}/{name}/{provider}/{endpoint}"
        response = request("GET", url)
        return response.json()
