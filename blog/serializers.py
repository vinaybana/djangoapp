from .models import Post,Category,Tag,Comment
from rest_framework import serializers
import json

class PostSerializer(serializers.ModelSerializer):
	comments = serializers.SerializerMethodField()

	def get_comments(self,obj):
		comments = Comment.objects.filter(post = obj.id).all()
		data = []
		for cmnt in comments:
			data.append(
				{
					'post':obj.id,
					'name':cmnt.name,
					'text': cmnt.text,
					'created':cmnt.created,
					'updated':cmnt.updated,
					'active':cmnt.active,
					'parent': cmnt.parent
				})
			# sent = json.dumps(data)
		return data

	class Meta:
		model = Post
		fields = ['id','title', 'text', 'author', 'created_date', 'published_date','comments']


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['id','title', 'text', 'parent', 'created_date']

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = ['id','title', 'text','created_date']

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ['post','name', 'text','created','updated','active','parent']