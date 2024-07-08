from django.urls import path
from .views import FeatureFlagController,  StringFeatureFlagController , IntegerFeatureFlagController , ObjectFeatureFlagController

urlpatterns = [
    path('openfeature', FeatureFlagController.as_view(), name='openfeature'),
    path('<str:user_email>/', StringFeatureFlagController.as_view(), name='string_feature_flag'),
    path('integer', IntegerFeatureFlagController.as_view(), name='integer_feature_flag'),  # For testing integer flags only
    path('object', ObjectFeatureFlagController.as_view(), name='object_feature_flag'),  # For testing object flags only
]
