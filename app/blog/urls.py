from django.urls import path
from app.blog import views

app_name = 'blog'

urlpatterns = [
	path('home/', views.home, name='home'),
	path('tutorials/', views.all_posts, name="all_posts"),
	path('tutorials/<slug:slug>/', views.detail, name='detail'),
	path('about/', views.about, name="about"),
	path('contact/',  views.contact, name="contact_me"),
]