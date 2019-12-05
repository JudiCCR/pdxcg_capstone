from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.safestring import mark_safe
from .models import Post, User, Comment
import json
import string
import random

def userhome(request):
    posts = request.user.posts.all()
    userlist = User.objects.all()
    context = {
        'posts':posts,
        'userlist':userlist,
    }
    return render(request, 'charapp/userhome.html', context)

def nu_post(request):
    user = request.user
    text = request.POST['nu_post_text']
    if text: 
        print(text)
    else: print('broke')
    title = request.POST['nu_post_title']

    post = Post.objects.create(user=user, text=text, title=title)
    post.save()

    return HttpResponseRedirect(reverse('charapp:userhome'))

def profile(request, username):
    context = {
        'profile': User.objects.get(username = username),
        'userlist': User.objects.all(),
    }
    return render(request, 'charapp/profile.html', context)

def comment(request, post_id):
    commenter = request.user
    post = Post.objects.get(id = post_id)
    text = request.POST['comment_text']
    author_name = request.POST['profile']

    comment = Comment.objects.create(user = commenter, post = post, text = text)
    comment.save()

    return HttpResponseRedirect(reverse('charapp:profile', args = [author_name]))

def post_table(request, post_id):
    post = Post.objects.get(id = post_id)
    user = request.user
    return render(request, 'charapp/post_table.html', {
        'user': user,
        'post': post,
    })

def quickstart(request, room_key):
    user = ''.join([random.choice(string.ascii_letters) for i in range(8)])
    context = {
        'user': user,
        'roomkey': room_key, 
    }
    return render(request, 'charapp/quickroom.html', context)
    
    