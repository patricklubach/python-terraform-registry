from dataclasses import dataclass
from typing import Any

from . import helpers


@dataclass
class Providers:
    """Base class for a Terraform provider."""

    name: str = "providers.v1"

    def list(self, namespace: str, type: str) -> dict[str, Any]:
        """
        Returns list of versions that are currently available for
        a particular provider.
        """

        response = helpers.call(self.name, namespace, type)
        return response.json()

    def find(
        self, namespace: str, type: str, version: str, os: str, arch: str
    ) -> dict[str, Any]:
        """
        Returns list of versions that are currently available for
        a particular provider.
        """

        response = helpers.call(
            self.name, namespace, type, version, "download", os, arch
        )
        return response.json()
