from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Program, WarningCard, ProfileCard, ImageCarousel, AboutRadio, ProgramEp, Pedidos, Calendar
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ProgramForm, UserForm, ImageCarouselForm, WarningCardForm, AboutRadioForm, ProfileCardForm, PedidosForm, ProgramEpForm, CalendarForm, UserUpdateForm
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .decorators import is_orientador, is_bolsista

def paginate(request, coisas, num_page):
    paginator = Paginator(coisas, num_page)
    page_number = request.GET.get('page')
    page_objects = paginator.get_page(page_number)
    
    return page_objects

def index(request):
    cards = WarningCard.objects.all()
    profilecards = ProfileCard.objects.all()
    carousel = ImageCarousel.objects.all()
    about = AboutRadio.objects.all()
    form = ImageCarouselForm()
    context = {
        'cards': cards, 
        'profilecards': profilecards, 
        'carousel': carousel, 
        'about': about, 
        'carouselform': form
    }
    
    return render(request, 'index.html', context)

@login_required
@is_bolsista
def admin_system(request):
    profilecards = ProfileCard.objects.all()
    return render(request, 'system/index.html', {'profilecards': profilecards})


# ========== CRUD INICIO ==========
# ===== CARROSEL =====
# LIST IMG CAROUSEL
@login_required
@is_bolsista
def home_list_system(request):
    img_carousel = ImageCarousel.objects.all()
    page = paginate(request, img_carousel, 6)
    context = {
        'page': page,
        'img_carousel': img_carousel
    }
    
    return render(request,'system/home/home-list.html', context)

# CREATE IMG CAROUSEL
@login_required
@is_bolsista
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

# UPDATE IMG CAROUSEL 
@login_required
@is_bolsista
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

# DELETE IMG CAROUSEL
@login_required
@is_bolsista
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
# LIST CARDS WARNING
@login_required
@is_bolsista
def warning_list_system(request):
    cards = WarningCard.objects.all()
    page = paginate(request, cards, 6)
    
    context = {
        'page': page,
        'cards': cards,
    }
    return render(request,'system/home/warning-list.html', context)

# CREATE CARD WARNING
@login_required
@is_bolsista
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

# UPDATE CARD WARNING
@login_required
@is_bolsista
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

# DELETE CARD WARNING
@login_required
@is_bolsista
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
# LIST ABOUT
@login_required
@is_bolsista
def about_list_system(request):
    about = AboutRadio.objects.all()
    return render(request,'system/home/about-list.html', {'about': about})

# UPDATE ABOUT
@login_required
@is_bolsista
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
# LIST CARDS PROFILE
@login_required
@is_bolsista
def profile_list_system(request):
    profile_cards = ProfileCard.objects.all()
    page = paginate(request, profile_cards, 6)
    context = {
        'page': page,
        'profile_cards': profile_cards
    }
    
    return render(request,'system/home/profile-card-list.html', context)

# CREATE CARD PROFILE
@login_required
@is_bolsista
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

# UPDATE CARD PROFILE
@login_required
@is_bolsista
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

# DELETE CARD PROFILE
@login_required
@is_bolsista
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



# ========== SISTEMA ADMIN ==========
# ===== CRUD PROGRAMAS =====
@login_required
@is_bolsista
def program_list_system(request):
    programs = Program.objects.all()
    page = paginate(request, programs, 6)
    context = {
        'page': page,
    }
    return render(request, 'system/programs/programs-list.html', context)

# List
def program_list(request):
    programs = Program.objects.all()
    return render(request, 'program/list.html', {'programs': programs})

# Create
@login_required
@is_bolsista
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
@is_bolsista
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
@is_bolsista
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

# ===== CRUD EPISODIOS =====
# EPISODIOS PROGRAMAS
# LIST EPISODIOS
@login_required
@is_bolsista
def programep_list(request, pk):
    program = get_object_or_404(Program, pk=pk)
    programep = ProgramEp.objects.filter(program=program) 
    page = paginate(request, programep, 5)
    context = {
        'page': page,
        'program':program
    }
    return render(request, 'system/programs/episodes-list.html', context)

# DETAIL/LIST EPISODIOS
def program_detail(request, pk):
    program = get_object_or_404(Program, pk=pk)
    eps = ProgramEp.objects.filter(program=program).order_by("timestamp")
    page = paginate(request, eps, 5)
    
    context = {
        'page': page,
        'program':program,
        'eps':eps,
        
    }
    return render(request, 'program/detail.html', context)


# CREATE EPISODIOS
@login_required
@is_bolsista
def programep_create(request, pk):
    program = get_object_or_404(Program, pk=pk)
    if request.method == "POST":
        form = ProgramEpForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.program = program
            form.save()
            return redirect('programep_list', pk=program.pk)
    else:
        form = ProgramEpForm()
    context = {
        'form': form,
        'program': program,
        'title':f'Criar um novo episodio para {program.name}'
    }
    return render(request, 'form.html', context)

# UPDATE
@login_required
@is_bolsista
def programep_update(request, pk):
    programep = get_object_or_404(ProgramEp, pk=pk)
    if request.method == "POST":
        form = ProgramEpForm(request.POST, request.FILES, instance=programep)
        if form.is_valid():
            form.save()
            return redirect('programep_list', pk=programep.program.pk)
    else:
        form = ProgramEpForm(instance=programep)
    context = {
        'form': form,
        'title':  f"Editar o episodio {programep}"
    }
    return render(request, 'form.html', context)

# DELETE 
@login_required
@is_bolsista
def programep_delete(request, pk):
    programep = get_object_or_404(ProgramEp, pk=pk)
    program = programep.program.pk

    if request.method == 'POST':
        programep.delete()
        return redirect('programep_list', pk=program)
    context = {
        'object': programep,
        'program': program,
        'title':f"Deletar o episodio {programep}",
        'message':f"Tem certeza que deseja deletar o episodio {programep}?"
    }
    return render(request,'form-delete.html', context)

# CRUD PEDIDOS DE MUSICAS
# PEDIDOS INICIO
def pedidos_create(request):
    if request.method == "POST":
        form = PedidosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pedidos_create')
    else:
        form = PedidosForm()

    context = {
        'form': form,
        'title':'PEÇA UMA MUSICA'
    }
    return render(request, 'music-requests/form.html', context)
@login_required
@is_bolsista
def pedido_aceito(request, pk):
    pedido = get_object_or_404(Pedidos, pk=pk)    
    if request.method == 'POST':
        pedido.status = 'aprovado'
        pedido.save()
    return redirect('pedidos_list_system')

@login_required
@is_bolsista
def pedido_negado(request, pk):    
    pedido = get_object_or_404(Pedidos, pk=pk)
    if request.method == 'POST':
        pedido.status = 'negado'
        pedido.save()
    return redirect ('pedidos_list_system')

@login_required
@is_bolsista
def pedidos_list_system(request):
    musiclist = Pedidos.objects.all()
    page = paginate(request, musiclist, 5)
    context = {
        'page': page,
        'musiclist': musiclist
    }
    return render(request, 'system/music-request/music-request-list.html', context)

@login_required
@is_bolsista
def pedidos_delete(request, pk):
    music = get_object_or_404(Pedidos, pk=pk)
    if request.method == 'POST':
        music.delete()
        return redirect('pedidos_list_system')
    context = {
        'object': music,
        'title':f"Deletar o pedido {music}",
        'message':f"Tem certeza que deseja deletar o pedido {music}?"
    }
    return render(request,'form-delete.html', context)

# CALENDARIO
@login_required
@is_bolsista
def calendar_create(request):
    if request.method == "POST":
        form = CalendarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_list')
    else:
        form = CalendarForm()

    context = {
        'form': form,
        'title':'CRIAR EVENTO'
    }
    return render(request, 'form.html', context)

def calendar(request):
    context = {}
    events = Calendar.objects.all()
    context['events'] = events
    programs = Program.objects.all()
    context['programs'] = programs

    return render(request, 'calendar/calendar.html', context)

@login_required
@is_bolsista
def calendar_update(request, pk):
    event = get_object_or_404(Calendar, pk=pk)
    if request.method == "POST":
        form = CalendarForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('calendar_list')
    else:
        form = CalendarForm(instance=event)
    context = {
        'form': form,
        'title':  f"Editar o evento {event}"
    }
    return render(request, 'form.html', context)

#LIST
@login_required
@is_bolsista
def calendar_list(request):
    calendar = Calendar.objects.all()
    # program = get_object_or_404(Program)
    page = paginate(request, calendar, 6)    
    
    if request.method == "POST":
        form = CalendarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar_list')
    else:
        form = CalendarForm()

    context = {
        'page': page,
        'form': form,
        'calendar': calendar,
        # 'program': program,
    }
    return render(request, 'system/calendar/calendar-list.html', context)

@login_required
@is_bolsista
def calendar_delete(request, pk):
    calendar = get_object_or_404(Calendar, pk=pk)
    if request.method == 'POST':
        calendar.delete()
        return redirect('calendar_list')
    context = {
        'object': calendar,
        'title':f"Deletar o evento {calendar}",
        'message':f"Tem certeza que deseja deletar o evento {calendar}?"
    }
    return render(request,'form-delete.html', context)

# ===== USUÁRIOS =====
# CRUD de usuário
@login_required
@is_orientador
def user_list(request):
    users = User.objects.all()
    page = paginate(request, users, 6)
    context = {
        'page': page,
    }
    return render(request, 'registration/user-list.html', context )

@login_required
@is_orientador
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()

    context = {
        'form': form,
        'title': 'CRIAR USUARIO'
    }
    return render(request, 'form.html', context)

@login_required
@is_orientador
def user_update(request, pk):
    user_update = get_object_or_404(User,pk=pk)
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=user_update)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserUpdateForm(instance=user_update)
    
    context = {
        'form': form,
        'title':  f"Editar o usuario {user_update}"
    }
    return render(request, 'form.html', context)

@login_required
@is_orientador
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    context = {
        'object': user,
        'title': f"deletar o usuario {user}"
    }
    return render(request, 'form-delete.html', context )

@login_required
@is_orientador
def user_update_password(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = SetPasswordForm(data=request.POST, user=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = SetPasswordForm(user=user)
    context = {
        'form' : form,
        'title': f"Alterar a senha do usuario {user}"
    }
    return render(request, 'form.html', context)


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

