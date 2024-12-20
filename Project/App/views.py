from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.
def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        
        '''try:
            user = User.objects.get(email=email)  
            if user.check_password(password):  
                auth.login(request, user) 
            user = authenticate(request, username=email, password=password)
                return redirect('blog/')  
            else:
                messages.info(request, 'Invalid Credentials')
                return redirect('login') 
        except User.DoesNotExist:
            messages.info(request, 'User does not exist')
            return redirect('login') 
    else:
        return render(request, 'login.html')'''
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  
            return redirect('blog/')  
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/')  
    else:
        return render(request, 'login.html')
        
    
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"email aready exist")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"username aready exist")
                return redirect("register")
            else:

                user=User.objects.create_user(password=password1,username=username,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.success(request,"user created")
                return redirect('/')
        else:
            messages.error(request,"password is not matching")
            return redirect('register')
    else:
        return render(request,'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

    
