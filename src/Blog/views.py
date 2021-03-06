from apps.posts.models import Post
from django.views.generic import TemplateView, ListView

class Base(ListView):
	model = Post
	template_name = 'base.html'
