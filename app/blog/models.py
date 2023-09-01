from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
	name = models.CharField(max_length=100, verbose_name='category')

	def __str__(self):
		return self.name


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	category = models.ForeignKey(Category, related_name='post', on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=500)
	content = RichTextUploadingField()
	publish = models.DateTimeField(auto_now_add=True)
	created = models.DateField(auto_now_add=True)

	class Meta:
		ordering = ['-publish', '-created']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog:detail', kwargs={'slug':  self.slug})

	@property
	def slug(self):
		return slugify(self.title)

class SubscribeUsers(models.Model):
	email = models.EmailField(unique=True, max_length=100)
	created = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.email

	
	



