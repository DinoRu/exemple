from django import template
from app.blog.models import Post


register = template.Library()

@register.inclusion_tag('pages/recent_posts.html')
def show_recent_posts(count=6):
	recent_posts = Post.objects.order_by('publish')[:count]
	return {'recent_posts': recent_posts}
