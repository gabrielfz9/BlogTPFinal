from apps.posts.models import Post
from django.views.generic import TemplateView, ListView

class Base(ListView):
	queryset = Post.objects.all().order_by('-fecha_publicacion')
	model = Post
	template_name = 'base.html'
