import logging
from openfeature import api
from .providers import HarnessClient
from featureflags.evaluations.auth_target import Target
from openfeature.evaluation_context import EvaluationContext

logger = logging.getLogger(__name__)

class FeatureFlagService:
    def __init__(self):
        self.provider = HarnessClient(api_key='4ee6bfa5-8de0-4bca-bb6c-d0cc5f8e8ed5')
        api.set_provider(self.provider)

    def fetch_flag_value(self, flag_name):
        logger.info(f"fetch_flag_value() -- flag_name: {flag_name}")
        try:
            client = api.get_client()
            flag_value = client.get_boolean_value(flag_name, False)
            logger.info(f"Fetched boolean value for '{flag_name}': {flag_value}")
        except Exception as e:
            logger.error(f"Error fetching flag value: {e}")
            flag_value = False
        return flag_value

    def fetch_string_variation(self, flag_key, user_email):
        logger.info(f"fetch_string_variation() -- flag_key: {flag_key}, user_email: {user_email}")
        try:
            # Create an EvaluationContext from the Target
            evaluation_context = EvaluationContext(
                targeting_key=user_email,
                attributes={"identifier": user_email, "name": user_email}
            )
            logger.info(f"Created evaluation context: {evaluation_context}")

            client = api.get_client()
            variation = client.get_string_value(flag_key, 'default', evaluation_context=evaluation_context)
            logger.info(f"Variation for {user_email}: {variation}")
            return variation
        except Exception as e:
            logger.error(f"Error fetching string variation: {e}")
            return 'default'

    def fetch_integer_variation(self, flag_name):
        logger.info(f"fetch_integer_variation() -- flag_name: {flag_name}")
        try:
            client = api.get_client()
            flag_value = client.get_integer_value(flag_name, 0)
            logger.info(f"Fetched integer value for '{flag_name}': {flag_value}")
        except Exception as e:
            logger.error(f"Error fetching flag value: {e}")
            flag_value = 0
        return flag_value

    def fetch_object_variation(self, flag_name):
        logger.info(f"fetch_object_variation() -- flag_name: {flag_name}")
        try:
            client = api.get_client()
            flag_value = client.get_object_value(flag_name, {})
            logger.info(f"Fetched object value for '{flag_name}': {flag_value}")
        except Exception as e:
            logger.error(f"Error fetching flag value: {e}")
            flag_value = {}
        return flag_value
