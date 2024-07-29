from typing import Optional, Any, List , Union, Set
from openfeature.evaluation_context import EvaluationContext
from openfeature.flag_evaluation import FlagResolutionDetails
from openfeature.hook import Hook
from openfeature.provider import AbstractProvider, Metadata
import logging
from featureflags.client import CfClient
from featureflags.evaluations.auth_target import Target

# Initialize logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class HarnessClient(AbstractProvider):
    def __init__(self, api_key):
        try:
            logger.info("Initializing HarnessClient with provided API key...")
            self.cf_client = CfClient(api_key)
            logger.info("Harness client created, waiting for initialization...")
            self.cf_client.wait_for_initialization()
            if not self.cf_client.is_initialized():
                raise Exception("Harness client failed to initialize")
            logger.info("Harness client initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing Harness client: {e}")
            self.cf_client = None

    def get_metadata(self) -> Metadata:
        return Metadata(name="HarnessProvider")

    def get_provider_hooks(self) -> List[Hook]:
        return []

    def resolve_boolean_details(
        self,
        flag_key: str,
        default_value: bool,
        evaluation_context: Optional[EvaluationContext] = None,
    ) -> FlagResolutionDetails[bool]:
        logger.info(f"resolve_boolean_details() -- flag_key: {flag_key}")
        try:
            if self.cf_client is None:
                raise Exception("Harness client not initialized")
            
            if evaluation_context:
                target_identifier = evaluation_context.attributes.get("identifier", "default_identifier")
                target_name = evaluation_context.attributes.get("name", "default_name")
            else:
                target_identifier = "default_identifier"
                target_name = "default_name"
            target = Target(identifier=target_identifier, name=target_name)
            logger.info(f'target created : {target}')
            value = self.cf_client.bool_variation(flag_key, target, default_value)
            logger.info(f"Flag '{flag_key}' resolved with value: {value}")
        except Exception as e:
            logger.error(f"Error resolving flag '{flag_key}': {e}")
            value = default_value
        return FlagResolutionDetails(value=value, reason="DEFAULT", variant="variant", flag_metadata={}, error_code=None)

    def resolve_string_details(
        self,
        flag_key: str,
        default_value: str,
        evaluation_context: Optional[EvaluationContext] = None,
    ) -> FlagResolutionDetails[str]:
        logger.info(f"resolve_string_details() -- flag_key: {flag_key}")
        try:
            if self.cf_client is None:
                raise Exception("Harness client not initialized")
            
            if evaluation_context:
                target_identifier = evaluation_context.attributes.get("identifier", "default_identifier")
                target_name = evaluation_context.attributes.get("name", "default_name")
            else:
                target_identifier = "default_identifier"
                target_name = "default_name"
            
            target = Target(identifier=target_identifier, name=target_name)
            logger.info(f"Target created: {target}")
            
            value = self.cf_client.string_variation(flag_key, target, default_value)
            logger.info(f"Flag '{flag_key}' resolved with value: {value}")
        except Exception as e:
            logger.error(f"Error resolving flag '{flag_key}': {e}")
            value = default_value
        return FlagResolutionDetails(value=value, reason="DEFAULT", variant="variant", flag_metadata={}, error_code=None)
    
    def resolve_float_details(
        self,
        flag_key: str,
        default_value: float,
        evaluation_context: Optional[EvaluationContext] = None,
    ) -> FlagResolutionDetails[float]:
        logger.info(f"resolve_float_details() -- flag_key: {flag_key}")
        try:
            if self.cf_client is None:
                raise Exception("Harness client not initialized")
            
            if evaluation_context:
                target_identifier = evaluation_context.attributes.get("identifier", "default_identifier")
                target_name = evaluation_context.attributes.get("name", "default_name")

            else:
                target_identifier = "default_identifier"
                target_name = "default_name"
            target = Target(identifier=target_identifier, name=target_name)
            value = self.cf_client.float_variation(flag_key, target, 0.0)
            logger.info(f"Flag '{flag_key}' resolved with value: {value}")
        except Exception as e:
            logger.error(f"Error resolving flag '{flag_key}': {e}")
            value = 0.0
        return FlagResolutionDetails(value=value, reason="DEFAULT", variant="variant", flag_metadata={}, error_code=None)

    def resolve_integer_details(
        self,
        flag_key: str,
        default_value: int,
        evaluation_context: Optional[EvaluationContext] = None,
    ) -> FlagResolutionDetails[int]:
        logger.info(f"resolve_integer_details() -- flag_key: {flag_key}")
        try:
            if self.cf_client is None:
                raise Exception("Harness client not initialized")
            
            if evaluation_context:
                target_identifier = evaluation_context.attributes.get("identifier", "default_identifier")
                target_name = evaluation_context.attributes.get("name", "default_name")
            
            else:
                target_identifier = "default_identifier"
                target_name = "default_name"

            target = Target(identifier=target_identifier, name=target_name)
            logger.info(f"Target created: {target}")
            value = int(self.cf_client.number_variation(flag_key, target, 0))
            logger.info(f"Flag '{flag_key}' resolved with value: {value}")
        except Exception as e:
            logger.error(f"Error resolving flag '{flag_key}': {e}")
            value = 0
        return FlagResolutionDetails(value=value, reason="DEFAULT", variant="variant", flag_metadata={}, error_code=None)

    def resolve_object_details(
        self,
        flag_key: str,
        default_value: Any,
        evaluation_context: Optional[EvaluationContext] = None,
    ) -> FlagResolutionDetails[Union[dict, list]]:
        logger.info(f"resolve_object_details() -- flag_key: {flag_key}")
        try:
            if self.cf_client is None:
                raise Exception("Harness client not initialized")
            
            if evaluation_context:
                target_identifier = evaluation_context.attributes.get("identifier", "default_identifier")
                target_name = evaluation_context.attributes.get("name", "default_name")
            
            else:
                target_identifier = "default_identifier"
                target_name = "default_name"
            target = Target(identifier=target_identifier, name=target_name)
            value = self.cf_client.json_variation(flag_key, target, default_value)
            if not isinstance(value, (dict, list)):
                raise TypeError(f"Expected type (dict, list) but got {type(value)}")
            logger.info(f"Flag '{flag_key}' resolved with value: {value}")
        except Exception as e:
            logger.error(f"Error resolving flag '{flag_key}': {e}")
            value = {}
        return FlagResolutionDetails(value=value, reason="DEFAULT", variant="variant", flag_metadata={}, error_code=None)


    def shutdown(self):
        if self.cf_client:
            self.cf_client.close()
            self.cf_client = None
        logger.info("Provider shutdown complete")
