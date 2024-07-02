from django.urls import path
from .views import FeatureFlagController ,StringFeatureFlagController

urlpatterns = [
    path('openfeature', FeatureFlagController.as_view(), name='openfeature'),
    path('<str:user_email>/', StringFeatureFlagController.as_view(), name='string_feature_flag'),
]
