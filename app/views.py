from django.shortcuts import render, redirect, get_object_or_404
from .models import Program, WarningCard, ProfileCard, ImageCarousel, AboutRadio, ProgramEp, Pedidos
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ProgramForm, UserForm, ImageCarouselForm, WarningCardForm, AboutRadioForm, ProfileCardForm, PedidosForm, ProgramEpForm
from django.contrib.auth import authenticate, login

def index(request):
    cards = WarningCard.objects.all()
    profilecards = ProfileCard.objects.all()
    carousel = ImageCarousel.objects.all()
    about = AboutRadio.objects.all()
    form = ImageCarouselForm()
    return render(request, 'index.html', {'cards': cards, 'profilecards': profilecards, 'carousel': carousel, 'about': about, 'carouselform': form})

@login_required
def admin_system(request):
    profilecards = ProfileCard.objects.all()
    return render(request, 'system/index.html', {'profilecards': profilecards})

# ========== CRUD INICIO ==========
# ===== CARROSEL =====
# List 
def home_list_system(request):
    img_carousel = ImageCarousel.objects.all() 
    return render(request,'system/home/home-list.html', {'img_carousel': img_carousel})

# Create das imagens do carrosel
def img_carousel_create(request):
    if request.method == "POST":
        form = ImageCarouselForm(request.POST, request. FILES)
        if form.is_valid():
            form.save()
            return redirect('home_list_system') 
    else:
        form = ImageCarouselForm()
    context = {
        'form': form,
        'title':'Criar uma nova imagem para o carrosel'
    }
    return render(request, 'system/home/form.html', context)

# Update
def img_carousel_update(request, pk):
    img_carousel = get_object_or_404(ImageCarousel, pk=pk)
    if request.method == "POST":
        form = ImageCarouselForm(request.POST, request.FILES, instance=img_carousel)
        if form.is_valid():
            form.save()
            return redirect('home_list_system')
    else:
        form = ImageCarouselForm(instance=img_carousel)
    context = {
        'form': form,
        'title':  f"Editar o programa {img_carousel}"
    }
    return render(request, 'form.html', context)

# Delete
def img_carousel_delete(request, pk):
    img_carousel = get_object_or_404(ImageCarousel, pk=pk)
    if request.method== 'POST':
        img_carousel.delete()
        return redirect('home_list_system')
    context = {
        'object': img_carousel,
        'title':f"Deletar a imagem {img_carousel}",
        'message':f"Tem certeza que deseja deletar a imagem {img_carousel}?"
    }
    return render(request,'form-delete.html', context)

# ===== AVISOS =====
# List
def warning_list_system(request):
    cards = WarningCard.objects.all()
    return render(request,'system/home/warning-list.html', {'cards': cards})

# Create
def warning_create(request):
    if request.method == "POST":
        form = WarningCardForm(request.POST, request. FILES)
        if form.is_valid():
            form.save()
            return redirect('warning_list_system') 
    else:
        form = WarningCardForm()
    context = {
        'form': form,
        'title':'Criar um novo card de avisos'
    }
    return render(request, 'system/home/form.html', context)

# Update
def warning_update(request, pk):
    cards = get_object_or_404(WarningCard, pk=pk)
    if request.method == "POST":
        form = WarningCardForm(request.POST, request.FILES, instance=cards)
        if form.is_valid():
            form.save()
            return redirect('warning_list_system')
    else:
        form = WarningCardForm(instance=cards)
    context = {
        'form': form,
        'title':  f"Editar o card de aviso {cards}"
    }
    return render(request, 'form.html', context)

# Delete
def warning_delete(request, pk):
    cards = get_object_or_404(WarningCard, pk=pk)
    if request.method== 'POST':
        cards.delete()
        return redirect('warning_list_system')
    context = {
        'object': cards,
        'title':f"Deletar a imagem {cards}",
        'message':f"Tem certeza que deseja deletar a imagem {cards}?"
    }
    return render(request,'form-delete.html', context)

# ===== SOBRE =====
# List
def about_list_system(request):
    about = AboutRadio.objects.all()
    return render(request,'system/home/about-list.html', {'about': about})

# update
def about_update(request, pk):
    about = get_object_or_404(AboutRadio, pk=pk)
    if request.method == "POST":
        form = AboutRadioForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('warning_list_system')
    else:
        form = AboutRadioForm(instance=about)
    context = {
        'form': form,
        'title':  f"Editar texto {about}"
    }
    return render(request, 'form.html', context)

# ===== CARDS DE PERFIL DOS MEMBROS DA RADIO =====
# List
def profile_list_system(request):
    profile_cards = ProfileCard.objects.all()
    return render(request,'system/home/profile-card-list.html', {'profile_cards': profile_cards})

# Create
def profile_create(request):
    if request.method == "POST":
        form = ProfileCardForm(request.POST, request. FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list_system') 
    else:
        form = ProfileCardForm()
    context = {
        'form': form,
        'title':'Criar um novo card para membro da equipe'
    }
    return render(request, 'system/home/form.html', context)

# Update
def profile_update(request, pk):
    profile_cards = get_object_or_404(ProfileCard, pk=pk)
    if request.method == "POST":
        form = ProfileCardForm(request.POST, request.FILES, instance=profile_cards)
        if form.is_valid():
            form.save()
            return redirect('profile_list_system')
    else:
        form = ProfileCardForm(instance=profile_cards)
    context = {
        'form': form,
        'title':  f"Editar o card do membro {profile_cards}"
    }
    return render(request, 'form.html', context)

# Delete
def profile_delete(request, pk):
    profile_cards = get_object_or_404(ProfileCard, pk=pk)
    if request.method== 'POST':
        profile_cards.delete()
        return redirect('profile_list_system')
    context = {
        'object': profile_cards,
        'title':f"Deletar a imagem {profile_cards}",
        'message':f"Tem certeza que deseja deletar a imagem {profile_cards}?"
    }
    return render(request,'form-delete.html', context)

# ===== CRUD PROGRAMAS ======
def program_list_system(request):
    programs = Program.objects.all()
    return render(request, 'system/programs/programs-list.html', {'programs': programs})

# List
def program_list(request):
    programs = Program.objects.all()
    return render(request, 'program/list.html', {'programs': programs})

# Create
@login_required
def program_create(request):
    if request.method == "POST":
        form = ProgramForm(request.POST, request.FILES) # coisa a img
        if form.is_valid():
            form.save()
            return redirect('program_list_system')
    else:
        form = ProgramForm()
    context = {
        'form': form,
        'title':'Criar um novo programa'
    }
    return render(request, 'form.html', context)

# Update
@login_required
def program_update(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method == "POST":
        form = ProgramForm(request.POST, request.FILES, instance=program)
        if form.is_valid():
            form.save()
            return redirect('program_list_system')
    else:
        form = ProgramForm(instance=program)
    context = {
        'form': form,
        'title':  f"Editar o programa {program}"
    }
    return render(request, 'form.html', context)

# Delete
@login_required
def program_delete(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method== 'POST':
        program.delete()
        return redirect('program_list_system')
    context = {
        'object': program,
        'title':f"Deletar o programa {program}",
        'message':f"Tem certeza que deseja deletar o programa {program}?"
    }
    return render(request,'form-delete.html', context)

# EP PROGRAMAS
@login_required
def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    eps = ProgramEp.objects.filter(program=program).order_by("timestamp")
    return render(request, 'program/detail.html', {'program': program, 'eps': eps})

@login_required
def programep_create(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method == "POST":
        form = ProgramEpForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.program = program
            form.save()
            return redirect('program_detail', pk=program.pk)
    else:
        form = ProgramEpForm()
    context = {
        'form': form,
        'title':'Criar um novo episodio'
    }
    return render(request, 'form.html', context)



# CRUD PEDIDOS DE MUSICAS

# List e Create
@login_required
def pedidos_list(request):
    musiclist = Pedidos.objects.all()

    if request.method == "POST":
        form = PedidosForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('pedidos_list') 
    else:
        form = PedidosForm()

    context = {
        'form': form,
        'musiclist': musiclist,
    }
    return render(request, 'music-requests/music-request-list.html', context)



# ===== AUTH =====
# Register
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']
            password  = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  
                return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

