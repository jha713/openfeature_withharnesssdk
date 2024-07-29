import logging
from openfeature import api
from .providers import HarnessClient
from openfeature.evaluation_context import EvaluationContext

logger = logging.getLogger(__name__)


class FeatureFlagService:
    def __init__(self ,api_key):
        self.provider = HarnessClient(api_key)
        api.set_provider(self.provider)
        self.client = api.get_client()

    def fetch_boolean_value(self, flag_key, user_email):
        logger.info(f"fetch_flag_value() -- flag_name: {flag_key}")
        try:
            evaluation_context = EvaluationContext(
                targeting_key=user_email,
                attributes={"identifier": user_email, "name": user_email}
            )
            flag_value = self.provider.resolve_boolean_details(flag_key, False, evaluation_context).value
            logger.info(f"Fetched boolean value for '{flag_key}': {flag_value}")
        except Exception as e:
            logger.error(f"Error fetching flag value: {e}")
            flag_value = False
        return flag_value

    def fetch_string_variation(self, flag_key, user_email):
        logger.info(f"fetch_string_variation() -- flag_key: {flag_key}, user_email: {user_email}")
        try:
            evaluation_context = EvaluationContext(
                targeting_key=user_email,
                attributes={"identifier": user_email, "name": user_email}
            )
            logger.info(f"Created evaluation context: {evaluation_context}")
            variation = self.provider.resolve_string_details(flag_key, 'default', evaluation_context).value
            logger.info(f"Variation for {user_email}: {variation}")
            return variation
        except Exception as e:
            logger.error(f"Error fetching string variation: {e}")
            return 'default'
        
    def fetch_float_variation(self, flag_key, user_email):
        logger.info(f"fetch_float_variation() -- flag_name: {flag_key}")
        try:
            evaluation_context = EvaluationContext(
                targeting_key=user_email,
                attributes={"identifier": user_email, "name": user_email}
            )
            flag_value = self.provider.resolve_float_details(flag_key, 0.0, evaluation_context).value
            logger.info(f"Fetched float value for '{flag_key}': {flag_value}")
        except Exception as e:
            logger.error(f"Error fetching flag value: {e}")
            flag_value = 0.0
        return flag_value

    def fetch_integer_variation(self, flag_key, user_email):
        logger.info(f"fetch_integer_variation() -- flag_name: {flag_key}")
        try:
            evaluation_context = EvaluationContext(
                targeting_key=user_email,
                attributes={"identifier": user_email, "name": user_email}
            )
            flag_value = self.provider.resolve_integer_details(flag_key, 0, evaluation_context).value
            logger.info(f"Fetched integer value for '{flag_key}': {flag_value}")
        except Exception as e:
            logger.error(f"Error fetching flag value: {e}")
            flag_value = 0
        return flag_value

    def fetch_object_variation(self, flag_key, user_email):
        logger.info(f"fetch_object_variation() -- flag_name: {flag_key}")
        try:
            evaluation_context = EvaluationContext(
                targeting_key=user_email,
                attributes={"identifier": user_email, "name": user_email}
            )
            flag_value = self.provider.resolve_object_details(flag_key, {}, evaluation_context).value
            logger.info(f"Fetched object value for '{flag_key}': {flag_value}")
        except Exception as e:
            logger.error(f"Error fetching flag value: {e}")
            flag_value = {}
        return flag_value