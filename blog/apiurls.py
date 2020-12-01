from rest_framework import renderers
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import api, views


router = DefaultRouter()
router.register('post', api.PostViewSet)
router.register('category', api.CategoryViewSet)
router.register('tag', api.TagViewSet)
router.register('comment', api.CommentViewSet)

urlpatterns = [
	
	path('', include(router.urls)),
]