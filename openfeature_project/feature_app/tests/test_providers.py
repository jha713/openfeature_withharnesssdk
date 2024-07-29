import unittest
from unittest.mock import patch, MagicMock
from feature_app.providers import HarnessClient
from featureflags.evaluations.auth_target import Target


class TestHarnessClient(unittest.TestCase):
    @patch('feature_app.providers.CfClient')
    def setUp(self, MockCfClient):
        self.mock_cf_client = MockCfClient.return_value
        self.mock_cf_client.is_initialized.return_value = True
        self.harness_client = HarnessClient("test_api_key")

    def test_initialize_success(self):
        self.mock_cf_client.is_initialized.assert_called_once()
        self.assertIsNotNone(self.harness_client.cf_client)

    def test_initialize_failure(self):
        with patch('feature_app.providers.CfClient') as MockCfClient:
            MockCfClient.return_value.is_initialized.return_value = False
            with self.assertRaises(Exception) as context:
                    HarnessClient("test_api_key")
                    self.assertEqual(str(context.exception), "Harness client not initialized")
                    
    def test_resolve_boolean_details(self):
        self.mock_cf_client.bool_variation.return_value = True
        target = Target(identifier="default_identifier", name="default_name")
        result = self.harness_client.resolve_boolean_details("test_flag", False)
        self.assertEqual(result.value, True)
        self.mock_cf_client.bool_variation.assert_called_with("test_flag", target, False)
        
    def test_resolve_string_details(self):
        self.mock_cf_client.string_variation.return_value = "test_value"
        target = Target(identifier="default_identifier", name="default_name")
        result = self.harness_client.resolve_string_details("test_flag", "default_value")
        self.assertEqual(result.value, "test_value")
        self.mock_cf_client.string_variation.assert_called_with("test_flag", target, "default_value")

    def test_resolve_integer_details(self):
        self.mock_cf_client.number_variation.return_value = 0
        target = Target(identifier="default_identifier", name="default_name")
        result = self.harness_client.resolve_integer_details("test_flag", 0)
        self.assertEqual(result.value, 0)
        self.mock_cf_client.number_variation.assert_called_with("test_flag", target, 0)

    def test_resolve_float_details(self):
        self.mock_cf_client.float_variation.return_value = 0.0
        target = Target(identifier="default_identifier", name="default_name")
        result = self.harness_client.resolve_float_details("test_flag", 0.0)
        self.assertEqual(result.value, 0.0)
        self.mock_cf_client.float_variation.assert_called_with("test_flag", target, 0.0)
    def test_resolve_object_details(self):
        self.mock_cf_client.json_variation.return_value = {"key": "value"}
        target = Target(identifier="default_identifier", name="default_name")
        result = self.harness_client.resolve_object_details("test_flag", {})
        self.assertEqual(result.value, {"key": "value"})
        self.mock_cf_client.json_variation.assert_called_with("test_flag", target, {})

if __name__ == '__main__':
    unittest.main()
