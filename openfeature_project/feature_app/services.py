import logging
from .providers import HarnessClient

logger = logging.getLogger(__name__)

class FeatureFlagService:
    def __init__(self):
        self.harness_client = HarnessClient(api_key='a3fa9722-ff5e-4096-a122-ab9a2a13d355')

    def fetch_flag_values(self, flag_name, target_identifier, target_name):
        logger.info("fetch_flag_values() -- start")

        try:
            flag_value = self.harness_client.is_feature_enabled(flag_name, target_identifier, target_name, False)
            logger.info(f"Flag '{flag_name}' resolved with value: {flag_value}")
        except Exception as e:
            logger.error(f"Error fetching flag value: {e}")
            flag_value = False

        logger.info("fetch_flag_values() -- end")
        return flag_value
