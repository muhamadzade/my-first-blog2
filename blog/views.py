from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    postDict={'ps': posts}
    return render(request, 'blog/post_list.html', postDict)
    
