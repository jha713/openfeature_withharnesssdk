import unittest
from django.test import TestCase
from rest_framework.test import APIClient
from unittest.mock import patch
from django.urls import reverse

class TestFeatureFlagViews(TestCase):
    def setUp(self):
        self.client = APIClient()

    @patch('feature_app.views.FeatureFlagService')
    def test_boolean_feature_flag_controller(self, MockFeatureFlagService):
        mock_service = MockFeatureFlagService.return_value
        mock_service.fetch_boolean_value.return_value = False
        url=reverse("openfeature")
        response = self.client.get(url, {'flag_key': 'test_key', 'user_email': 'user@test.com'})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'flag_value': False})

    # Similar tests for StringFeatureFlagController
    @patch('feature_app.views.FeatureFlagService')
    def test_string_feature_flag_controller(self, MockFeatureFlagService):
        mock_service = MockFeatureFlagService.return_value
        mock_service.fetch_string_variation.return_value = 'default'
        url=reverse("string_feature_flag")
        response = self.client.get(url, {'flag_key': 'test_key', 'user_email': 'user@test.com'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'variation': 'default'})

    # Similar tests for IntegerFeatureFlagController
    @patch('feature_app.views.FeatureFlagService')
    def test_integer_feature_flag_controller(self, MockFeatureFlagService):
        mock_service = MockFeatureFlagService.return_value
        mock_service.fetch_integer_variation.return_value = 0
        url = reverse("integer_feature_flag")
        response = self.client.get(url, {'flag_key': 'test_key', 'user_email': 'user@test.com'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'flag_value': 0})

    # Similar tests for FloatFeatureFlagController
    @patch('feature_app.views.FeatureFlagService')
    def test_float_feature_flag_controller(self, MockFeatureFlagService):
        mock_service = MockFeatureFlagService.return_value
        mock_service.fetch_float_variation.return_value = 0.0
        url = reverse("float_feature_flag")

        response = self.client.get(url, {'flag_key': 'test_key', 'user_email': 'user@test.com'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'flag_value': 0.0})

    # Similar tests for ObjectFeatureFlagController
    @patch('feature_app.views.FeatureFlagService')
    def test_object_feature_flag_controller(self, MockFeatureFlagService):
        mock_service = MockFeatureFlagService.return_value
        mock_service.fetch_object_variation.return_value = {'flag_value': {}}
        url = reverse('object_feature_flag')
        response = self.client.get(url, {'flag_key': 'test_key', 'user_email': 'user@test.com'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'flag_value': {}})


if __name__ == '__main__':
    unittest.main()
