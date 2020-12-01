from rest_framework import serializers, viewsets, status as status_code, generics, mixins
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import pagination

class PostViewSet(viewsets.ModelViewSet	):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-published_date')
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated] 
    http_method_names = ['get','post','put','patch','delete']

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	http_method_names = ['get','post','put','patch','delete']

class TagViewSet(viewsets.ModelViewSet):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer
	http_method_names = ['get','post','put','patch','delete']

class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	http_method_names = ['get','post','put','patch','delete']