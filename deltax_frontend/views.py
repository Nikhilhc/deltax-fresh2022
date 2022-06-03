from django.shortcuts import  render, redirect
from .forms import RegistrationForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib import messages

def homepage(request):
    return render(request,'HomePage.html')

def register_request(request):
    form = RegistrationForm(request.POST or None)
    print(form.errors)
    if form.is_valid():
        username = form.cleaned_data['username']
        password1 = form.cleaned_data['password1']
        password2 = form.cleaned_data['password2']
        new_user = form.save(commit=False)
        new_user.save()
        messages.success(request,'Successfully Registered.')
        return redirect("deltax_frontend:home")
    context = {
        'form':form
    }
    return render(request,'register.html',context)

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        try:
            user = User.objects.get(username=username)
        except:
            user=None
            messages.error(request,f"Are you sure you are registered? We cannot find this user.")
        if user is not None and not user.check_password(password):
            if password is None:
                messages.error(request, f'Field is required')
            messages.error(request,f"Invalid Passsword")
        elif user is None:
            pass
        else:
            user = authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,'Successfully Logged In. Welcome!!')
            #user.emailconfirmed.active_user_email()
            return redirect("deltax_frontend:home")
    else:
        form = LoginForm()
    context = {'form':form}
    return render(request,'Login.html',context)

def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully Logged Out. Feel free to login again')
    return redirect('deltax_frontend:login')