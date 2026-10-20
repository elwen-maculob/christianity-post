from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/featured_snippet.html')
def show_featured_posts():
    featured_posts = list(Post.objects.filter(is_featured=True).order_by('-created_on')[:3])
    
    if len(featured_posts) < 3:
        needed = 3 - len(featured_posts)
        existing_ids = [p.id for p in featured_posts]
        fallback_posts = Post.objects.exclude(id__in=existing_ids).order_by('-created_on')[:needed]
        featured_posts.extend(list(fallback_posts))
        
    return {'featured_posts': featured_posts}