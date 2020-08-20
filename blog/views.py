from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PostSerializer
from rest_framework import generics

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_details.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog:post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog:post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})


def sign_up(request):
	context = {}
	form = UserCreationForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			user = form.save()
			auth.login(request, user)
			return render(request,'blog/post_list.html')
	context['form']=form
	return render(request,'blog/sign_up.html',context)

def login(request):

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		print(username)
		print(password)
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return render(request, 'blog/post_list.html')
	else:
		return render(request, 'blog/login.html')

def logout(request):
	logout(request)
	return render(request, 'blog/post_list.html')

class PostViewSet(viewsets.ModelViewSet	):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all().order_by('-published_date')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]



# Redirect to a success page.

