from django.shortcuts import render, redirect
from .models import Program
from .forms import ProgramForm

def index(request):
    return render(request, 'index.html')

def programacao(request):
    return render(request, 'programacao.html')

# Listar os programas na tela de programação
def programacao(request):
    programs = Program.objects.all()
    return render(request, 'programacao.html', {'object_list': programs})

# Create
def program_create(request):
    if request.method == "POST":
        form = ProgramForm(request.POST)
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