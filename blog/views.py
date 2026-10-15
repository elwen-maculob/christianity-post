from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
#1. For homepage
class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'featured_posts'
    def get_queryset(self):
        return Post.objects.filter(is_featured=True).order_by('-created_on')[:3]
#2. For 2000 word blog posts  
class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog_list.html'
    context_object_name = 'blog_list'
    def get_queryset(self):
        return Post.objects.filter(category__name='Blog', status=1).order_by('-created_on')
#3. For 600 words reflection posts
class ReflectionListView(ListView):
    model = Post
    template_name="blog/reflection_list.html"
    context_object_name="reflections"
    def get_queryset(self):
        return Post.objects.filter(category__name="Reflection", status=1).order_by("-created_on")
#4. Post detail view
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
#5. About page view
class AboutView(DetailView):
    template_name = 'blog/about.html' 
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)