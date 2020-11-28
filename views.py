from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from .models import Register
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout

def regi(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('home')
            except:
                pass
        else:
            print(form.errors)
    else:
        form = RegisterForm()
    context={'form':form}
    return render(request, 'register.html', context)

def log(request):
    if request.session.__contains__('is_logged'):
        return redirect('home')
    if request.method == 'POST':
        name1 = request.POST['name']
        password1 = request.POST['password']

        count = Register.objects.filter(name=name1, password=password1).count()
        if count > 0:
            request.session['is_logged'] = True
            return redirect('home')
        else:
            # messages.error(request, "Invalid credentials")
            return render(request, 'login.html', {'alert_flag': True})
    return render(request, 'login.html')

def logout(request):
    request.session.__delitem__('is_logged')
    return redirect('login')

def home(request):
    if request.session.__contains__('is_logged'):
        return render(request, 'home.html')
    return redirect('login')

def ind(request):
    return render(request, 'index.html')

def pros(request):
    return render(request, 'products.html')

def pro_det(request):
    return render(request, 'product-details.html')

def cart(request):
    return render(request, 'cart.html')

def account(request):
    return render(request, 'account.html')