from django.http import JsonResponse
from django.views import View
import logging
from .services import FeatureFlagService
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

class FeatureFlagController(View):
    feature_flag_service = FeatureFlagService()

    def get(self, request):
        flag_name = request.GET.get('flag_name')
        if not flag_name:
            return JsonResponse({'error': 'flag_name parameter is required'}, status=400)
        logger.info("get() -- start")
        flag_value = self.feature_flag_service.fetch_flag_value(flag_name)
        logger.info("get() -- end")
        return JsonResponse({'flag_value': flag_value}, status=200)

class StringFeatureFlagController(APIView):
    feature_flag_service = FeatureFlagService()

    def get(self, request, user_email):
        if not user_email:
            return JsonResponse({'error': 'user_email parameter is required'}, status=400)
        logger.info(f"Received request for user_email: {user_email}")
        flag_key = 'multivariant'
        logger.info("get() -- start")
        flag_value = self.feature_flag_service.fetch_string_variation(flag_key, user_email)
        logger.info("get() -- end")
        return JsonResponse({'variation': flag_value}, status=200)

class IntegerFeatureFlagController(View):
    feature_flag_service = FeatureFlagService()

    def get(self, request):
        flag_name = request.GET.get('flag_name')
        if not flag_name:
            return JsonResponse({'error': 'flag_name parameter is required'}, status=400)

        logger.info(f"Received request for flag_name: {flag_name}")
        logger.info("get() -- start")
        flag_value = self.feature_flag_service.fetch_integer_variation(flag_name)
        logger.info("get() -- end")
        return JsonResponse({'flag_value': flag_value}, status=200)

class ObjectFeatureFlagController(APIView):
    feature_flag_service = FeatureFlagService()

    def get(self, request):
        flag_name = request.GET.get('flag_name')
        if not flag_name:
            return JsonResponse({'error': 'flag_name parameter is required'}, status=400)
        logger.info(f"Received request for flag_name: {flag_name}")
        logger.info("get() -- start")
        flag_value = self.feature_flag_service.fetch_object_variation(flag_name)
        logger.info("get() -- end")
        return Response(flag_value, status=status.HTTP_200_OK)
