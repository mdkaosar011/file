from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import *
from . forms import *

# Create your views here.
@login_required
def home(req):
    posts = Post.objects.all().order_by('-created_at')
    profiles = Profile.objects.all()
    context = {
        'posts': posts,
        'profiles':profiles,
    }
    return render(req, 'home.html',context)


@login_required
def create_post(req):
    if req.method == 'POST':
        form = CreatePostForm(req.POST, req.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.author = req.user
            data.save()
            messages.success(req, "Post created successfully!")
            return redirect('my_post')
    else:
        form = CreatePostForm()

    return render(req, 'create_post.html', {'form': form})
        

@login_required
def my_post(req):
    posts = Post.objects.filter(author= req.user).order_by('-created_at')
    profiles = Profile.objects.all()
    context = {
        'posts': posts,
        'profiles':profiles,
    }
    return render(req, 'my_post.html',context)


@login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, author=request.user, id=post_id)

    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES, instance=post)  
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect('my_post') 

    else:
        form = CreatePostForm(instance=post)

    return render(request, 'create_post.html', {'form': form, 'post': post})



@login_required
def delete_post(req, id):
    post = get_object_or_404(Post, id = id, author=req.user)
    if req.method == 'POST':
        post.delete()
        messages.success(req, "The post has been successfully deleted.")
        return redirect('my_post')
    


@login_required
def profile_view(request):
    # Fetch or create profile
    profile, created = Profile.objects.get_or_create(author=request.user)  

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home') 

    else:
        form = ProfileForm(instance=profile) 

    return render(request, 'profile.html', {'form': form})



@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return JsonResponse({
                'success': True,
                'author': comment.author.username,
                'content': comment.content,
                'profile_pic': comment.author.profile.profile_pic.url if comment.author.profile.profile_pic else '/static/default_profile.png'  
            })
    
    return JsonResponse({'success': False, 'error': 'Invalid form'}, status=400)