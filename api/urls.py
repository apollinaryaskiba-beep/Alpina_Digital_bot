from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GPTBotViewSet, ScenarioViewSet, StepViewSet

router = DefaultRouter()
router.register(r'bots', GPTBotViewSet)
router.register(r'scenarios', ScenarioViewSet)
router.register(r'steps', StepViewSet)

urlpatterns = [
    path('', include(router.urls)),
]