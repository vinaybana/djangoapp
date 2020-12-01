from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Userprofile, Comment,Category,Tag
from .forms import PostForm,ProfileForm, categoryForm,CommentForm
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PostSerializer
from rest_framework import generics
from django.contrib.auth.decorators import login_required

def category_list(request):
	categories=Category.objects.all()
	return render(request, 'blog/category_list.html', {'categories':categories})

def category_detail(request,slug):
	category = get_object_or_404(Category, slug=slug)
	print(category)
	posts= Post.objects.filter(category=category)
	print(posts)
	return render(request, 'blog/category_detail.html', {'posts': posts, 'category':category})

def category_edit(request, slug):
	category = get_object_or_404(Category, slug=slug)
	if request.method == "POST":
		form = CategoryForm(request.POST, instance=category)
		if form.is_valid():
			category = form.save(commit=False)
			category.created_date = timezone.now()
			category.save()
			return redirect('blog:category_detail', slug=category.slug)
	else:
		form = CategoryForm(instance=category)
	return render(request, 'blog/category_edit.html', {'form': form})

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	comments=Comment.objects.filter(post=post, parent=None)
	new_comment=None
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():	
			text= request.POST.get('text')
			name= request.POST.get('name')
			reply_id=request.POST.get('comment_id')
			comment_obj=None
			if reply_id:
				comment_obj=Comment.objects.get(id=reply_id)
			
			new_comment = Comment.objects.create(post=post, parent=comment_obj, text=text, name=name)
			new_comment.save()
			return redirect('blog:post_detail', slug=post.slug)

	else:
		form = CommentForm()
	return render(request, 'blog/post_details.html', {'form':form , 'post': post, 'comments':comments})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog:post_list')
		
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, slug):
	post = get_object_or_404(Post, slug=slug)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('blog:post_detail', slug=post.slug)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

def tag_list(request):
	tags= Tag.objects.all()
	print(tags)
	return render(request, 'blog/tag_list.html', {'tags':tags})


def tag_details(request, slug):
	tag = get_object_or_404(Tag, slug=slug)
	print(tag)
	posts=Post.objects.filter(tag__slug=tag)
	return render(request, 'blog/tag_details.html', {'tag':tag, 'posts': posts})


def cmnt(request, slug):
	post= get_object_or_404(Post, slug=slug)
	cmnt= Post.cmnt.filter(slug=post.slug)
	return cmnt



# def post_list(request):
# 	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
# 	return render(request, 'blog/post_list.html', {'posts':posts})

# def post_detail(request, pk):
# 	post = get_object_or_404(Post, pk=pk)
# 	return render(request, 'blog/post_details.html', {'post': post})

# def post_new(request):
# 	if request.method == "POST":
# 		form = PostForm(request.POST)
# 		if form.is_valid():
# 			post = form.save(commit=False)
# 			post.author = request.user
# 			post.published_date = timezone.now()
# 			post.save()
# 			return redirect('blog:post_detail', pk=post.pk)
# 	else:
# 		form = PostForm()
# 	return render(request, 'blog/post_edit.html', {'form': form})

# def post_edit(request, pk):
# 	post = get_object_or_404(Post, pk=pk)
# 	if request.method == "POST":
# 		form = PostForm(request.POST, instance=post)
# 		if form.is_valid():
# 			post = form.save(commit=False)
# 			post.author = request.user
# 			post.published_date = timezone.now()
# 			post.save()
# 			return redirect('blog:post_detail', pk=post.pk)
# 	else:
# 		form = PostForm(instance=post)
# 	return render(request, 'blog/post_edit.html', {'form': form})


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
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return render(request, 'blog/post_list.html')
	else:
		return render(request, 'blog/login.html')

def logout(request):
	logout(request)
	return render(request, 'blog/post_list.html')

@login_required
def userdetail(request, pk):
	user = User.objects.get(pk=pk)
	userimg=  Userprofile.objects.filter(user= request.user).first()
	return render(request, 'blog/userdetail.html',{'user':user, 'userimg':userimg})


def edit_profile(request, pk):
	user = User.objects.get(pk=pk)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES)

		if form.is_valid():
			is_exist = Userprofile.objects.filter(user=request.user).first()
			if is_exist:
				is_exist.user_image= form.cleaned_data.get('user_image')
				is_exist.user = request.user
				is_exist.save()
			else:
				userimg = form.save(commit=False)
				userimg.user = request.user
				userimg.save()
			return redirect('blog:userdetail',pk=user.pk)
	else:
		form = ProfileForm()
	return render(request,'blog/useredit.html', {'form':form})




# Redirect to a success page.

