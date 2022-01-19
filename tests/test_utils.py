import re
import unittest

import terraform_registry


class TestUtils(unittest.TestCase):
    def test_base_url(self):
        self.assertIs(type(terraform_registry.BASE_URL), str)
        expression = re.compile("^https://[a-z.]+$")
        self.assertTrue(expression.match(terraform_registry.BASE_URL))

    def test_list(self):
        self.assertIs(type(terraform_registry.list()), dict)
