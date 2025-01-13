from django import forms
from .models import Program, ImageCarousel, WarningCard, AboutRadio, ProfileCard, Pedidos, ProgramEp, Calendar
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm


class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['image', 'name', 'description', 'color']
        widgets = {
            'color': forms.Select(attrs={'class': 'form-select'}),
        }


class UserForm(UserCreationForm):
    # email = forms.EmailField(max_length=100)
    group =  forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label="Grupo de Permissão")
    class Meta:
        model = User
        fields  = ('username', 'first_name', 'password1', 'password2', 'group')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            group = self.cleaned_data['group']
            user.groups.add(group)
        return user


class UserUpdateForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True, label="Grupo de Permissão")
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'group')
    
    def __init__(self, *args, **kwargs):
        user = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if user and user.groups.exists():
            self.fields['group'].initial = user.groups.first() 

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            group = self.cleaned_data['group']
            user.groups.add(group)
        return user

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
        fields = ['date', 'program']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
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
    
