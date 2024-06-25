from django.http import JsonResponse
from django.views import View
import logging
from .services import FeatureFlagService

logger = logging.getLogger(__name__)

class FeatureFlagController(View):
    feature_flag_service = FeatureFlagService()

    def get(self, request):
        flag_name = request.GET.get('flag_name')

        if not flag_name:
            return JsonResponse({'error': 'flag_name parameter is required'}, status=400)

        logger.info("get() -- start")
        target_identifier = 'openidentifier'
        target_name = 'openfeature'
        flag_value = self.feature_flag_service.fetch_flag_values(flag_name, target_identifier, target_name)
        logger.info(f"flag_value: {flag_value}")
        logger.info("get() -- end")

        return JsonResponse({'flag_value': flag_value}, status=200)
