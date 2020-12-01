from rest_framework import renderers
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import api, views

router = DefaultRouter()
router.register('question', api.QuestionViewSet),
router.register('choice', api.ChoiceViewSet),

urlpatterns = [
	path('', include(router.urls)),
]