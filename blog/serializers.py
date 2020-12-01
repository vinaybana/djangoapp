from .models import Post,Category,Tag,Comment
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ['title', 'text', 'author', 'created_date', 'published_date']


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['title', 'text', 'parent', 'created_date']

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ['title', 'text','created_date']

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['post','name', 'text','created','updated','active','parent']