from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import login, authenticate, logout #add thi
from django.contrib.auth.decorators import login_required
# Create your views here.


from .forms import *
 
# Create your views here.
 
 
def hotel_image_view(request):
 
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
 
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = HotelForm()
    return render(request, 'hotel_image_form.html', {'form': form})
 
 
def success(request):
    return HttpResponse('successfully uploaded')

# Python program to view
# for displaying images


def display_hotel_images(request):

	if request.method == 'GET':

		# getting all the objects of hotel.

		Hotels = Hotel.objects.all()
		return render(request, 'display_hotel_images.html',
					{'hotel_images': Hotels})


def register(request):


    if request.method == 'POST':
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        username = request.POST["username"]
        password1 = request.POST["psw"]
        password2 = request.POST["psw-repeat"]
        email = request.POST["email"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "UserName Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username = username,first_name=first_name,last_name=last_name, email=email, password= password1 )
                user.save()
        else:
            messages.info(request, "Password not matching")
            return redirect('register')
        return redirect("image_upload")
    
    else:
        return  render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        print("here ooo")
        username = request.POST['username']
        password = request.POST['password']


        user = auth.authenticate(username=username, password=password)

        if user is not None:
            print("not none")
            auth.login(request, user)
            return redirect('feeds')
        else:
            print(" none")
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    else:
        return render(request, "login.html")

def home(request):
    return  render(request, 'register.html')

@login_required
def feeds(request):  
    import random
    latest_posts = Post.objects.order_by('-created_at')[:100]

    # Shuffle the posts randomly
    random_posts = random.sample(list(latest_posts), len(latest_posts))
    print(type(random_posts))
    Hotels = Hotel.objects.all()
    p = Post.objects.order_by('-created_at')[:100]
    post = Comments.objects.order_by('-id')[:100]
    for i in Post.objects.all():
                post.title = i.author
    return render(request, 'index.html', {'hotel_images': Hotels, 'p': random_posts,"post": post})


from .models import Post
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.comment =  "Comment"
            post.save()
            for obj in Post.objects.all():
                print(obj.title)
            return redirect('feeds')
        
                



    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def create_comment(request):
    if request.method == 'POST':
        comment = Post.objects.all().values_list('comment', flat=True).order_by('-created_at')[:100]
        ##comment_id = Comments.objects.get(title='Testing Comments and Post linkage').id

        print(comment)
        try:
            product = Post.objects.get(title='comment').title
            print(product)
        except Post.DoesNotExist:
            print('Post not found')


        # Print the names of the matching comment
        form = CommentForm(request.POST)
        
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            for i in Post.objects.all():
                post.title = i.author
            for j in Post.objects.all():
                post.title2= j.title
            print(post.title2)
            post.save()
            print(f"{post.author} commented {post.content}  on {post.title}'s post")  
            return redirect("feeds")
        
                



    else:
        form = CommentForm()
        for obj in Post.objects.all():
            #if obj.title == 
            print(obj.id)
    return render(request, 'comment.html', {'form': form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("login")