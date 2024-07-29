import unittest
import os
from dotenv import load_dotenv
from unittest.mock import patch, MagicMock
from feature_app.services import FeatureFlagService

load_dotenv()

class TestFeatureFlagService(unittest.TestCase):
    @patch('feature_app.services.HarnessClient')
    def setUp(self, MockHarnessClient):
        self.mock_harness_client = MockHarnessClient.return_value
        self.service = FeatureFlagService(api_key=os.getenv('HARNESS_API_KEY'))

    def test_fetch_boolean_value(self):
        self.mock_harness_client.resolve_boolean_details.return_value.value = True
        result = self.service.fetch_boolean_value('test_key', 'user@test.com')
        self.assertTrue(result)


    def test_fetch_string_value(self):
        self.mock_harness_client.resolve_string_details.return_value.value = 'test_value'
        result = self.service.fetch_string_variation('test_key', 'user@test.com')
        self.assertEqual(result, 'test_value')

    def test_fetch_integer_value(self):
        self.mock_harness_client.resolve_integer_details.return_value.value = 0
        result = self.service.fetch_integer_variation('test_key', 'user@test.com')
        self.assertEqual(result, 0)

    def test_fetch_float_value(self):
        self.mock_harness_client.resolve_float_details.return_value.value = 0.0
        result = self.service.fetch_float_variation('test_key', 'user@test.com')
        self.assertEqual(result, 0.0)

    def test_fetch_object_value(self):
        self.mock_harness_client.resolve_object_details.return_value.value = {'key': 'value'}
        result = self.service.fetch_object_variation('test_key', 'user@test.com')
        self.assertEqual(result, {'key': 'value'})


if __name__ == '__main__':
    unittest.main()
