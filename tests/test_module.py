import unittest

from terraform_registry import Module

NAMESPACE: str = "terraform-modules-google"
NAME: str = "network"
PROVIDER: str = "google"
VERSION: str = "v4.0.1"


class TestModule(unittest.TestCase):
    def test_module(self):
        """Tests the instance creation of type Module."""
        service = Module()
        self.assertIsInstance(service, Module)

    def test_download(self):
        """Tests the retrieval of a single module."""
        service = Module()
        self.assertIs(
            type(service.download(NAMESPACE, NAME, PROVIDER, VERSION)), str
        )
        self.assertEqual(
            service.download(NAMESPACE, NAME, PROVIDER, VERSION), ""
        )

    def test_get(self):
        """Tests retrieval of single module info."""
        service = Module()
        self.assertIs(
            type(service.get(NAMESPACE, NAME, PROVIDER, VERSION)), dict
        )
