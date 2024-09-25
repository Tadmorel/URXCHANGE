# main/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),  # Página principal con login
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('la_salle/',views.la_salle, name='la_salle'),
    path('anahuac/',views.anahuac, name='anahuac'),
    path('unam/',views.unam, name='unam'),
    path('ipn/',views.ipn, name='ipn'),
    path('tec/',views.tec, name='tec'),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='main/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='main/password_change_done.html'), name='password_change_done'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete_post'),  # Ruta para eliminar
]

