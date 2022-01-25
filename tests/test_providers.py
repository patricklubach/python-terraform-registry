import unittest

from terraform_registry import Providers

ARCH: str = "amd64"
NAMESPACE: str = "terraform-Moduless-google"
OS: str = "linux"
TYPE: str = "google"
VERSION: str = "v4.0.1"


class TestModules(unittest.TestCase):
    def test_Providers(self):
        """Tests the instance creation of type provider"""
        service = Providers()
        self.assertIsInstance(service, Providers)

    def test_list(self):
        """Tests retrieval of the latest version of a single pproviders"""
        service = Providers()
        self.assertIs(type(service.list(NAMESPACE, TYPE)), dict)

    def test_find(self):
        """Tests retrieval of the latest version of a single pproviders"""
        service = Providers()
        self.assertIs(
            type(service.find(NAMESPACE, TYPE, VERSION, OS, ARCH)), dict
        )
