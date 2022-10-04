from django.shortcuts import render
from.models import Post 
# Create your views here. display posts on blog
def list(request):
    Data = {'Posts':  Post.objects.all().order_by("-date")} #conductive into template, #key Posts
    return render(request, 'blog/blog.html', Data)