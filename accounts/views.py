from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contacts

# Create your views here.

def register(request):
    if request.method == 'POST':
        # messages.error(request, 'Hello World Testing Error msgs')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if both passwords match
        # if password != password2:
        #     messages.error(request, 'Passwords do not match')
        #     return redirect('register')
        # else:
        #     flag1 = True

            # Check if username is unique
        if User.objects.filter(username = username).exists():
            messages.error(request , 'Someone has that Username, try another')
            return redirect('register')
        else:
            flag2 = True
                # Check if email is unique
        if User.objects.filter(email = email).exists():
            messages.error(request , 'That email is already used!')
            return redirect('register')
        else:
            flag3 = True

        # No error, all good
        if flag2 & flag3:
            user = User.objects.create_user(username = username,email = email,password= password, first_name= first_name, last_name= last_name)
            user.save()
            messages.success(request, 'User registration successfull! Now you can login with your credentials')
            return redirect('login')
        # else:
        #     messages.error(request, 'Passwords do not match')
        #     return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Login Successfull!')
            return redirect('dashboard')
        else:
            messages.error(request , 'Invalid Username/Password')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.info(request, "You're logged out!")
        return redirect('index')

def dashboard(request):

    all_inquiries = Contacts.objects.order_by('-contact_date').filter( user_id = request.user.id)

    context = {
        'contacts': all_inquiries,
    }
    return render(request, 'accounts/dashboard.html', context)