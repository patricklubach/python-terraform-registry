from dataclasses import dataclass


@dataclass
class Providers:
    """Base class for a Terraform provider."""

    name: str = "providers.v1"
