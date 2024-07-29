from django.urls import path
from .views import BooleanFeatureFlagController,  StringFeatureFlagController , FloatFeatureFlagController , IntegerFeatureFlagController , ObjectFeatureFlagController

urlpatterns = [
    path('boolean', BooleanFeatureFlagController.as_view(), name='openfeature'),
    path('string', StringFeatureFlagController.as_view(), name='string_feature_flag'),
    path('float', FloatFeatureFlagController.as_view(), name='float_feature_flag'),  # For testing float flags only
    path('integer', IntegerFeatureFlagController.as_view(), name='integer_feature_flag'),  # For testing integer flags only
    path('object', ObjectFeatureFlagController.as_view(), name='object_feature_flag'),  # For testing object flags only
]
