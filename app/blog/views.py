from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from app.blog.models import Post, Category, SubscribeUsers
from app.blog.forms import SubscribeForm


def home(request):
	return render(request, 'pages/index.html', {})


def all_posts(request):
	
	categories = Category.objects.all()
	q = request.GET.get('q') if request.GET.get('q') !=None else ''
	posts = Post.objects.filter(Q(category__name__icontains=q) |
								Q(title__icontains=q) |
								Q(description__icontains=q))
	context = {
		'posts': posts,
		'categories': categories,
	}
	return render(request, 'pages/all_posts.html', context)


def detail(request, slug):
	post = list(filter(lambda post: post.slug==slug, Post.objects.all()))[0]
	if request.method == 'POST':
		form = SubscribeForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			subscribe_user = SubscribeUsers.objects.filter(email=email).first()
			if subscribe_user:
				messages.error(request, f"{email} email address is already subscriber.")
				return redirect('blog:detail', post.slug)
			try:
				validate_email(email)
			except ValidationError as e:
				messages.error(request, e.messages[0])
				return redirect('blog:detail', post.slug)
			subsciber = SubscribeUsers()
			subsciber.email = email
			subsciber.save()
			messages.success(request, f'{email} email was successfully subscribed to our newsletter!')
			return redirect('blog:detail', post.slug)
	else:
		form = SubscribeForm
	context = {
		'post': post,
		'form': form
	}
	return render(request, 'pages/post_detail.html', context)


def about(request):
	return render(request, 'pages/about.html', {})


def contact(request):
	return render(request, 'pages/contact_me.html', {})


