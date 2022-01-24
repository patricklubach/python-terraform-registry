from typing import Any

from requests import Response, request

from . import utils


def endpoint(service_name: str) -> str:
    """Returns the endpoint path of the given service."""

    services = utils.list()
    return services.get(service_name, "")


def uri(service_name: str):
    """Returns the full uri of the service."""

    return "/".join([utils.BASE_URL, endpoint(service_name)])


def url(*args: str) -> str:
    return "/".join(args)


def call(service_name: str, *args: str, **kwargs: Any) -> Response:
    """
    Calls the Terraform Registry API with specified parameter
    and returns requests.Response object.
    """

    path: str = "/".join([arg for arg in args])
    callable_url: str = url(uri(service_name), path)
    params: dict[str, Any] = {}

    if not kwargs:
        for key, value in kwargs:
            params[key] = value

    return request("GET", callable_url, params=params)
