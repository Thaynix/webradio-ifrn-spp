from django.shortcuts import render, redirect, get_object_or_404
from .models import Program, WarningCard
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ProgramForm, UserForm
from django.contrib.auth import authenticate, login


def index(request):
    cards = WarningCard.objects.all()
    return render(request, 'index.html', {'cards': cards})

# Listar os programas na tela de programação
def program_list(request):
    programs = Program.objects.all()
    return render(request, 'program/list.html', {'object_list': programs})

# Create
@login_required
def program_create(request):
    if request.method == "POST":
        form = ProgramForm(request.POST, request.FILES) # coisa a img
        if form.is_valid():
            form.save()
            return redirect('programacao')
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
            return redirect('programacao')
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
        return redirect('programacao')
    context = {
        'object': program,
        'title':f"Deletar o programa {program}",
        'message':f"Tem certeza que deseja deletar o programa {program}?"
    }
    return render(request,'form-delete.html', context)

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
