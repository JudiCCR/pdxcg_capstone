from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, User, Comment
import string

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
    title = request.POST['nu_post_title']
    upload = request.FILES.get('nu_post_file', None)

    post = Post.objects.create(user=user, text=text, title=title, upload=upload)
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
    context = {'post':post}
    return render(request, 'charapp/post_table.html', context)