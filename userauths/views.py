from django.urls import reverse
from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings
from userauths.models import User

# User = settings.AUTH_USER_MODEL


# Create your views here.
def register_view(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hey {username}, your account was created successfully")
            new_user = authenticate(username=form.cleaned_data['email'],
                                    password=form.cleaned_data['password1']
            )
            login(request, new_user)
            app_name = 'shop'
            url_name = 'index'
            url = reverse(f'{app_name}:{url_name}')
            return redirect(url)
    else:
        form =UserRegisterForm()
    
    context ={
        'form':form,
    }
    return render(request, 'registration/signup.html', context)

def login_view(request):
    if request.user.is_authenticated:
        messages.warning(request, f"Hey, you are already logged In")
        return redirect('shop:index')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'You are logged in successfuly')
                return redirect('shop:index')
            else:
                messages.warning(request, 'User Does Not Exist, Sign Up')
        except:
            messages.warning(request, f"User with {email} does not exist")
        
        
    return render(request, 'registration/signin.html')
        
        
def logout_view(request):
    logout(request)
    messages.success(request, "You logged out.")
    return redirect('userauths:signin')