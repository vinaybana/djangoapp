from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['title', 'text', 'author', 'created_date', 'published_date']


