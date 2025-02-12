from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages 
from .models import Users

# Create your views here.
def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            encrypted_password = make_password(password)
            new_user = Users(user_name = user_name, email=email, password = encrypted_password)
            new_user.save()
            return redirect('login')
        except Exception as e:
            messages.error(request, f'Ocurrió un error: {e}')
            return redirect('register')
        
    return render(request, 'register.html')

def login (request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        try:
            #Bucar usuario en la base de datos
            user = Users.objects.get(user_name = user_name)
            if check_password(password, user.password):
                messages.success(request, 'Inicio de sesión exitoso')
                request.session['user_name'] = user_name
                return redirect('what_home')
            else:
                messages.error(request, 'Contraseña incorrecta')
                return redirect('login')
        except Users.DoesNotExist:
            #Para cuando el usuario no se encuntra
            messages.error(request, 'El usuario no existe.')
            return redirect('login')
    else:
        return render(request, 'login.html')