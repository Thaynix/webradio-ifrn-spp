from django.contrib.auth.models import User, Group 
from django.shortcuts import redirect

def is_orientador(func):
    def _wrapper_view(request, *args, **kwargs):
        if not request.user.groups.filter(name="Orientador").exists():
            return redirect("index")

        return func(request, *args, **kwargs)
    
    return _wrapper_view

def is_bolsista(func):
    def _wrapper_view(request, *args, **kwargs):
        bolsista = request.user.groups.filter(name="Bolsista").exists()
        orientador = request.user.groups.filter(name="Orientador").exists()

        if not bolsista and not orientador:
            return redirect("index")
        
        return func(request, *args, **kwargs)
    return _wrapper_view