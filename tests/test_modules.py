import unittest

from terraform_registry import Modules

NAMESPACE: str = "terraform-Moduless-google"
NAME: str = "network"
PROVIDER: str = "google"
VERSION: str = "v4.0.1"


class TestModules(unittest.TestCase):
    def test_Modules(self):
        """Tests the instance creation of type module"""
        service = Modules()
        self.assertIsInstance(service, Modules)

    def test_download(self):
        """Tests the retrieval of a single module"""
        service = Modules()
        self.assertIs(
            type(service.download(NAMESPACE, NAME, PROVIDER, VERSION)), str
        )
        self.assertEqual(
            service.download(NAMESPACE, NAME, PROVIDER, VERSION), ""
        )

    def test_get(self):
        """Tests retrieval of single Modules info."""
        service = Modules()
        self.assertIs(
            type(service.get(NAMESPACE, NAME, PROVIDER, VERSION)), dict
        )

    def test_latest(self):
        """Tests retrieval of the latest version of a single module"""
        service = Modules()
        self.assertIs(type(service.latest(NAMESPACE, NAME)), dict)

    def test_latest_provider(self):
        """
        Tests retrieval of the latest versions of Terraform providers
        that are available for the module
        """
        service = Modules()
        self.assertIs(
            type(service.latest_provider(NAMESPACE, NAME, PROVIDER)), dict
        )

    def test_list(self):
        """Tests retrieval of the latest version of a single module"""
        service = Modules()
        self.assertIs(type(service.list(NAMESPACE, provider=PROVIDER)), dict)

    def test_search(self):
        """Tests retrieval of the latest version of a single module"""
        service = Modules()
        self.assertIs(type(service.list(NAME, provider=PROVIDER)), dict)
