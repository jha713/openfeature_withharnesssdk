from django.urls import path
from .views import BooleanFeatureFlagController,  StringFeatureFlagController , IntegerFeatureFlagController , ObjectFeatureFlagController

urlpatterns = [
    path('boolean', BooleanFeatureFlagController.as_view(), name='openfeature'),
    path('string', StringFeatureFlagController.as_view(), name='string_feature_flag'),
    path('integer', IntegerFeatureFlagController.as_view(), name='integer_feature_flag'),  # For testing integer flags only
    path('object', ObjectFeatureFlagController.as_view(), name='object_feature_flag'),  # For testing object flags only
]
