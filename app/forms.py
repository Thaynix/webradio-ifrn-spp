from django import forms
from .models import Program, ImageCarousel, WarningCard, AboutRadio, ProfileCard, Pedidos
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['image', 'name', 'description']


class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    class Meta:
        model = User
        fields  = ('username', 'email', 'password1', 'password2')

class ImageCarouselForm(forms.ModelForm):
    class Meta:
        model = ImageCarousel
        fields = ['title', 'image']

class WarningCardForm(forms.ModelForm):
    class Meta:
        model = WarningCard
        fields = ['title', 'description', 'author']

class AboutRadioForm(forms.ModelForm):
    class Meta:
        model = AboutRadio
        fields = ['text', 'image']

class ProfileCardForm(forms.ModelForm):
    class Meta:
        model = ProfileCard
        fields = ['image', 'position', 'name', 'description']

class PedidosForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ['description']
