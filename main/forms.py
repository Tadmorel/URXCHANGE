# main/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from . import models
from .models import Posts

class UserRegisterForm(UserCreationForm):
    USER_TYPE_CHOICES = (
        ('student', 'Estudiante'),
        ('collaborator', 'Colaborador'),
    )
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True)
    first_name = forms.CharField(max_length=30, required=True, label='Nombre')
    last_name = forms.CharField(max_length=30, required=True, label='Apellido')
    email = forms.EmailField(required=True, label='Email')
    country = forms.CharField(max_length=100, required=False, label='País')
    university = forms.CharField(max_length=200, required=False, label='Universidad')

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'user_type', 'country', 'university', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('user_type')

        if user_type == 'student':
            if not cleaned_data.get('country'):
                self.add_error('country', 'Este campo es requerido para estudiantes.')
            if not cleaned_data.get('university'):
                self.add_error('university', 'Este campo es requerido para estudiantes.')
        elif user_type == 'collaborator':
            # Para colaboradores, solo se requiere la universidad
            if not cleaned_data.get('university'):
                self.add_error('university', 'Este campo es requerido para colaboradores.')
        return cleaned_data
    
class PostForm(forms.ModelForm):
    class Meta:
        model = models.Posts
        fields=['title','description','university']




    
