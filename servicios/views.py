from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ServiciosForm
from .models import Servicios
from django.contrib.auth.decorators import login_required #proteger/esconderxd(?)


# Create your views here.
def home(request):
    return render(request, 'home.html',)

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('servicios')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'User already exist'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Password do not match'
        })
        

@login_required
def servicios(request):
    servicios = Servicios.objects.filter(user=request.user)  #fts? solo el actual 1.38
    return render(request, 'servicios.html', {'servicios': servicios})


@login_required
def add_servicios(request):
    
    if request.method == 'GET':
        return render(request, 'add_servicios.html', {
            'form': ServiciosForm
        })
    else:
        try:
            form = ServiciosForm(request.POST, request.FILES)
            new_servicio = form.save(commit=False)
            new_servicio.user = request.user
            new_servicio.save() #se guarda xd
            return redirect('servicios')
        except ValueError:
            return render(request, 'add_servicios.html', {
                'form': ServiciosForm,
                'error': 'please provide valid data'
            })
            


@login_required
def servicio_detail(request, servicio_id):
    if request.method == 'GET':
        servicio = get_object_or_404(Servicios, pk=servicio_id, user=request.user)
        form = ServiciosForm(instance=servicio)
        return render(request, 'servicio_detail.html', {'servicio': servicio, 'form':form})
    else:
        try:
            servicio = get_object_or_404(Servicios, pk=servicio_id, user=request.user)
            form = ServiciosForm(request.POST, request.FILES, instance=servicio)
            form.save()
            return redirect('servicios')
        except ValueError:
            return render(request, 'servicio_detail.html', {'servicio': servicio, 'form':form, 'error': "Error updating task"})


@login_required
def delete_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicios, pk=servicio_id, user=request.user)
    if request.method == 'POST':
        servicio.delete()
        return redirect('servicios')


@login_required
def cerrarsesion(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
            })
        else:
            login(request, user)
            return redirect('servicios')