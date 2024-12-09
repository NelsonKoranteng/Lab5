from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm


# Login view
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the homepage after login
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

@login_required
def add_comment(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('view_post', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'post': post})
    
# Homepage view
def homepage(request):
    # Get all blog posts, ordered by creation date
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'homepage.html', {'posts': posts})
from django.shortcuts import render, get_object_or_404
from .models import BlogPost  # Replace with your model name if different

# View for displaying a single blog post
def view_post(request, id):
    post = get_object_or_404(BlogPost, id=id)  # Fetch the post by its ID
    return render(request, 'view_post.html', {'post': post})

# View for creating a new blog post
#@login_required
def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            # Create a post but don't save it to the database yet
            post = form.save(commit=False)
            # Assign the current user as the author
            post.author = request.user
            # Now save the post
            post.save()
            return redirect('home')  # Redirect to the homepage or desired URL
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})

    # View for updating an existing blog post
def update_post(request, id):
    post = get_object_or_404(BlogPost, id=id)  # Fetch the blog post by ID or return 404
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)  # Bind the form with existing post data
        if form.is_valid():
            form.save()  # Save changes to the database
            return redirect('view_post', id=post.id)  # Redirect to the updated post's detail page
    else:
        form = BlogPostForm(instance=post)  # Initialize the form with the post data
    return render(request, 'update_post.html', {'form': form, 'post': post})

    # View for deleting a blog post
def delete_post(request, id):
    post = get_object_or_404(BlogPost, id=id)  # Fetch the blog post by ID or return 404
    if request.method == 'POST':
        post.delete()  # Delete the post from the database
        return redirect('home')  # Redirect to the homepage or any other page
    return render(request, 'delete_post.html', {'post': post})

    # View for user registration
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to the homepage or another page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

    # View for user logout
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to the homepage after logout

    # View for user profile
@login_required
def profile(request):
    return render(request, 'blog/profile.html')  # Ensure 'profile.html' exists in your templates
