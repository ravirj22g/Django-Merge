# Create your views here.


from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from .forms import PostForm, LoginForm, SignUpForm, CommentForm, ProfileForm
from django.contrib import  messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate,logout
import csv
from django.http import HttpResponse





def post_list(request):
    print(request.user)
    posts = Post.objects.filter(published_date__lte=timezone.now()).all().order_by('-published_date')
    # posts = Post.objects.all()
    return render(request, 'unit/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'unit/post_detail.html', {'post': post})


def post_detail(request, pk):
    post = Post.objects.filter(pk=pk).last()
    comment = Comments.objects.filter(post=post).all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        new_comment = form.save(commit=False)
        new_comment.post=post
        new_comment.save()
        return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
        post = get_object_or_404(Post, pk=pk)
    return render(request, 'unit/post_detail.html', {'post': post, 'form': form, 'comments': comment})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        user = MyUser.objects.filter(id=request.user.id).last()
        if form.is_valid():
            post = form.save(commit=False)
            post.author = user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'unit/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'unit/post_edit.html', {'form': form})

def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("Validdd")
            user = form.save()
            auth_login(request, user)
            return redirect('post_list')
    else:
        form = SignUpForm()
    return render(request, 'unit/Signup.html', {'form': form})

def login(request):
    if request.user.is_authenticated:
        return redirect('post_list')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('post_list')
            else:
                print("Invalifddddddddddddddd")
                messages.error(request,'Invalid Credential')
                return redirect('login')
    form = LoginForm()
    return render(request, 'unit/login.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('post_list')

def category_detail(request, id):
    category = Category.objects.filter(id=id).last()
    print(category,'cccccccccccccc')
    posts = Post.objects.filter(category=category).all()
    return render(request, 'unit/post_list.html', {'posts': posts})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'unit/category_list.html', {'categories': categories})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'unit/tag_list.html', {'tags': tags})


def tag_detail(request, id):
    tag = Tag.objects.filter(id=id).last()
    posts = Post.objects.filter(tag__name=tag).all()
    return render(request, 'unit/tag_detail.html', {'posts': posts})


def user_profile(request):
    form = ProfileForm(None,instance=request.user)
    # print(MyUser.objects.get(request.user))
    return render(request,'unit/user_profile.html', {'form': form})    

def profile_update(request):
    form = ProfileForm(None,instance=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile Updated')
            return redirect('post_list')
    return render(request,'unit/profile_update.html', {'form': form}) 