from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', index, name='index'),
    path('programacao', program_list, name='program_list'),
    path('sistema/', admin_system, name='admin_system'),

    # CRUD
    path('sistema/programas/', program_list_system, name='program_list_system'),
    path('cadastrar/', program_create, name='program_create'),
    path('<int:pk>/atualizar/', program_update, name='program_update'),
    path('<int:pk>/deletar/', program_delete, name='program_delete'),
    
    # AUTH
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cadastro/', register, name='register'),
    

]