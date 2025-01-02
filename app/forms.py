from django import forms
from .models import Program, ImageCarousel, WarningCard, AboutRadio, ProfileCard, Pedidos, ProgramEp, Calendar
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
        fields = ['description', 'singer', 'author']

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calendar
        fields = ['date','color', 'program']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-select'}),
            'program': forms.Select(attrs={'class': 'form-select'}),
        }
        

def check_audio_extension(filename):
    """
    Checa se o arquivo tem uma extensão de áudio
    """
    audio_extensions = [".mp3", ".wav", ".ogg", ".oga", ".m4a"]
    for ext in audio_extensions:
        if filename.endswith(ext):
            return True
    return False

class ProgramEpForm(forms.ModelForm):
    class Meta:
        model = ProgramEp
        fields = ['audio', 'title', 'description']

    def clean(self):
        cleaned_data = super().clean()

        audio = cleaned_data.get("audio")
        is_audio =  check_audio_extension(str(audio))
        if is_audio == False:
            self.add_error("audio", "É necessário cadastrar com um arquivo de áudio.")
        
        return cleaned_data
    
