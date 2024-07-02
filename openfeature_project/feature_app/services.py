import logging
from openfeature import api
from .providers import HarnessClient

logger = logging.getLogger(__name__)

class FeatureFlagService:
    def __init__(self):
        self.provider = HarnessClient(api_key='a3fa9722-ff5e-4096-a122-ab9a2a13d355') #api key for flag name openfeature_flag boolean variation.
        self.string_provider = HarnessClient(api_key='4ee6bfa5-8de0-4bca-bb6c-d0cc5f8e8ed5')  # API key for string variation
        
        api.set_provider(self.provider)
        #api.set_provider(self.string_provider)  # Setting string provider for string variation.

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
    
    def fetch_string_variation(self, flag_key, user_email):
        logger.info(f"fetch_string_variation() -- flag_key: {flag_key}, user_email: {user_email}")
        try:
            variation = self.string_provider.get_string_variation(flag_key, user_email, 'group', 'default')
            logger.info(f"Variation for {user_email}: {variation}")
            return variation
        except Exception as e:
            logger.error(f"Error fetching string variation: {e}")
            return 'default'
