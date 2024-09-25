from django.shortcuts import render

# Create your views here.


# main/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Posts, CustomUser


def home(request):
    return render(request, 'main/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu cuenta ha sido creada. Puedes iniciar sesión ahora.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Credenciales inválidas')
    return render(request, 'main/login.html')

@login_required
def dashboard(request):
    user=request.user
    post_form = PostForm()
    rol = user.user_type
    data_context = {'user': request.user,'post_form':post_form}
    print(rol)
    if rol == 'collaborator':
        data_context['collab'] = True
        if request.method == 'POST':
           post_form = PostForm(request.POST)
           if post_form.is_valid():
               post = post_form.save(commit=False)
               post.user = user
               post.save()
            
    return render(request, 'main/dashboard.html',data_context)

def user_logout(request):
    logout(request)
    return redirect('login')

def la_salle(request):
    posts = Posts.objects.filter(university="ulsa")
    data_context = {"Posts":posts}
    return render(request, 'la_salle.html',data_context)


def anahuac(request):
    posts = Posts.objects.filter(university="ana")
    data_context = {"Posts":posts}
    return render(request, 'anahuac.html',data_context)


def unam(request):
    posts = Posts.objects.filter(university="unam")
    data_context = {"Posts":posts}
    return render(request, 'unam.html',data_context)

def tec(request):
    posts = Posts.objects.filter(university="tec")
    data_context = {"Posts":posts}
    return render(request, 'tec.html',data_context)

def ipn(request):
    posts = Posts.objects.filter(university="ipn")
    data_context = {"Posts":posts}
    return render(request, 'ipn.html',data_context)




def edit_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)  # Obtener el post por su ID o lanzar 404 si no existe

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)  # Pre-rellenar el formulario con los datos actuales
        if form.is_valid():
            form.save()  # Guardar los cambios en la base de datos
            messages.success(request, 'Publicación actualizada con éxito.')
            return redirect('dashboard')  # Redirigir a la página que prefieras después de editar
    else:
        form = PostForm(instance=post)  # Mostrar el formulario con los datos existentes

    return render(request, 'edit_post.html', {'form': form, 'post': post})



def delete_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)


   
    if request.method == 'POST':
        post.delete()  # Eliminar el post de la base de datos
        messages.success(request, 'Publicación eliminada con éxito.')  # Mensaje de confirmación
        return redirect('dashboard')  # Redirigir a la página después de eliminar

    return render(request, 'delete_post.html', {'post': post})  # Mostrar confirmación antes de eliminar

