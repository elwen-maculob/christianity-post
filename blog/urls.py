from django.urls import path
from .views import HomeView, BlogListView, ReflectionListView, PostDetailView, AboutView
from blog.views import health_check
app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('reflection/', ReflectionListView.as_view(), name='reflection_list'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('health/', health_check, name='health_check'),
]