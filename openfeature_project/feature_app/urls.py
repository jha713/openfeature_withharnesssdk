from django.urls import path
from .views import FeatureFlagController

urlpatterns = [
    path('openfeature', FeatureFlagController.as_view(), name='openfeature'),
]
