from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post

def index(request):
    posts = request.user.posts.all()
    context = {
        'posts':posts,
    }
    return render(request, 'charapp/index.html', context)

def nu_post(request):
    user = request.user
    text = request.POST['nu_post_text']

    post = Post.objects.create(user=user, text=text)
    post.save()

    return HttpResponseRedirect(reverse('charapp:index'))