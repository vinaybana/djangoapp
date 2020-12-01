from rest_framework import serializers, viewsets, status as status_code, generics, mixins
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework.response import Response

class QuestionViewSet(viewsets.ModelViewSet):
	serializer_class = QuestionSerializer
	queryset = Question.objects.all()
	http_method_names = ['get','post','put','patch']

class ChoiceViewSet(viewsets.ModelViewSet):
	serializer_class = ChoiceSerializer
	queryset = Choice.objects.all()
	http_method_names = ['get','post','put','patch']