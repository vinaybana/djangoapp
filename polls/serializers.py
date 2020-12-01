from .models import Question,Choice
from rest_framework import serializers

class QuestionSerializer(serializers.ModelSerializer):
	choices = serializers.SerializerMethodField()

	def get_choices(self, obj):
		choices = Choice.objects.filter(question = obj.id).all()
		data = []
		for opt in choices:
			data.append(
				{
					'id': opt.id,
					'choice_text': opt.choice_text,
					'score': opt.votes
				})
		return data
	class Meta:
		model = Question
		fields = ['question_text', 'pub_date','choices']

class ChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = ['question', 'choice_text', 'votes']

