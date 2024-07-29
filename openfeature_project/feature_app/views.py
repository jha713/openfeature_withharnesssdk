from django.http import JsonResponse
from django.views import View
import os
from dotenv import load_dotenv
import logging
from .services import FeatureFlagService
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)
load_dotenv()

class FeatureFlagMixin:
    feature_flag_service = FeatureFlagService(api_key=os.getenv('HARNESS_API_KEY'))

class BooleanFeatureFlagController(APIView , FeatureFlagMixin):
    def get(self, request):
        flag_key = request.GET.get('flag_key')
        user_email = request.GET.get('user_email')
        if not flag_key or not user_email:
            return JsonResponse({'error': 'flag_key and user_email parameters are required'}, status=400)
        logger.info("get() -- start")
        flag_value = self.feature_flag_service.fetch_boolean_value(flag_key, user_email)
        logger.info("get() -- end")
        return JsonResponse({'flag_value': flag_value}, status=200)

class StringFeatureFlagController(APIView, FeatureFlagMixin):
    def get(self, request):

        flag_key = request.query_params.get('flag_key')
        user_email = request.query_params.get('user_email')
        if not flag_key or not user_email:
            return JsonResponse({'error': 'flag_key and user_email parameters are required'}, status=400)
        logger.info(f"Received request for flag_key: {flag_key}, user_email: {user_email}")
        logger.info("get() -- start")
        flag_value = self.feature_flag_service.fetch_string_variation(flag_key, user_email)
        logger.info("get() -- end")
        return JsonResponse({'variation': flag_value}, status=200)
    
class FloatFeatureFlagController(APIView, FeatureFlagMixin):

    def get(self, request):

        flag_key = request.GET.get('flag_key')
        user_email = request.GET.get('user_email')
        if not flag_key or not user_email:
            return JsonResponse({'error': 'flag_key and user_email parameters are required'}, status=400)
        logger.info(f"Received request for flag_name: {flag_key}")
        logger.info("get() -- start")
        flag_value = self.feature_flag_service.fetch_float_variation(flag_key, user_email)
        logger.info("get() -- end")
        return JsonResponse({'flag_value': flag_value}, status=200)
        


class IntegerFeatureFlagController(APIView , FeatureFlagMixin):

    def get(self, request):
        flag_key = request.GET.get('flag_key')
        user_email = request.GET.get('user_email')

        if not flag_key or not user_email:
            return JsonResponse({'error': 'flag_key and user_email parameters are required'}, status=400)

        logger.info(f"Received request for flag_name: {flag_key}")
        logger.info("get() -- start")
        flag_value = self.feature_flag_service.fetch_integer_variation(flag_key, user_email)
        logger.info("get() -- end")
        return JsonResponse({'flag_value': flag_value}, status=200)

class ObjectFeatureFlagController(APIView , FeatureFlagMixin):

    def get(self, request):
        flag_key = request.GET.get('flag_key')
        user_email = request.GET.get('user_email')
        if not flag_key or not user_email:
            return JsonResponse({'error': 'flag_key and user_email parameter is required'}, status=400)
        logger.info(f"Received request for flag_name: {flag_key}")
        logger.info("get() -- start")
        flag_value = self.feature_flag_service.fetch_object_variation(flag_key, user_email)
        logger.info("get() -- end")
        return Response({'flag_value': flag_value}, status=status.HTTP_200_OK)
