from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    #IGNORE THE ERROR AT Post WORD BELOW.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #In above line lte means Less Then or Equal to.
    stuff_for_frontend = {'posts':posts}
    return render(request, 'blog/post_list.html', stuff_for_frontend)