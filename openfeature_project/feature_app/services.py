import logging
from openfeature import api
from .providers import HarnessClient

logger = logging.getLogger(__name__)

class FeatureFlagService:
    def __init__(self):
        self.provider = HarnessClient(api_key='a3fa9722-ff5e-4096-a122-ab9a2a13d355')
        api.set_provider(self.provider)

    def fetch_flag_value(self, flag_name):
        logger.info("fetch_flag_value() -- start")
        try:
            client = api.get_client()
            flag_value = client.get_boolean_value(flag_name, False)
        except Exception as e:
            logger.error(f"Error fetching flag value: {e}")
            flag_value = False
        logger.info("fetch_flag_value() -- end")
        return flag_value
