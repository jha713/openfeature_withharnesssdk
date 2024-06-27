import unittest
from unittest.mock import MagicMock, patch
from openfeature.flag_evaluation import FlagResolutionDetails
from feature_app.providers import HarnessClient

class TestHarnessClient(unittest.TestCase):

    @patch('feature_app.providers.CfClient')  # Mock the CfClient class in the feature_app.providers module
    def setUp(self, MockCfClient):
        self.mock_cf_client = MockCfClient.return_value
        self.mock_cf_client.wait_for_initialization.return_value = None
        self.api_key = 'a3fa9722-ff5e-4096-a122-ab9a2a13d355'
        self.harness_client = HarnessClient(self.api_key)

    def test_resolve_boolean_details_success(self):
        # Setup
        flag_key = 'test-flag'
        default_value = False
        expected_value = True
        self.mock_cf_client.bool_variation.return_value = expected_value

        # Exercise
        result = self.harness_client.resolve_boolean_details(flag_key, default_value)

        # Verify
        self.mock_cf_client.bool_variation.assert_called_once_with(flag_key, self.harness_client.target, default_value)
        self.assertIsInstance(result, FlagResolutionDetails)
        self.assertEqual(result.value, expected_value)
        self.assertEqual(result.reason, "DEFAULT")
        self.assertEqual(result.variant, "variant")
        self.assertEqual(result.flag_metadata, {})
        self.assertIsNone(result.error_code)

    def test_resolve_boolean_details_exception(self):
        # Setup
        flag_key = 'test-flag'
        default_value = False
        self.mock_cf_client.bool_variation.side_effect = Exception("Test exception")

        # Exercise
        result = self.harness_client.resolve_boolean_details(flag_key, default_value)

        # Verify
        self.mock_cf_client.bool_variation.assert_called_once_with(flag_key, self.harness_client.target, default_value)
        self.assertIsInstance(result, FlagResolutionDetails)
        self.assertEqual(result.value, default_value)
        self.assertEqual(result.reason, "DEFAULT")
        self.assertEqual(result.variant, "variant")
        self.assertEqual(result.flag_metadata, {})
        self.assertIsNone(result.error_code)

if __name__ == '__main__':
    unittest.main()
