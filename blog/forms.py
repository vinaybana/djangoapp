from django import forms
from .models import Post, Userprofile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text',)

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Userprofile
		fields = ('user_image',)

# class UserForm(forms.ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ('username', 'first_name', 'last_name', 'email')

