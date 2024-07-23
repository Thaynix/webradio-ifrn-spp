from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', index, name='index'),
    path('programacao', program_list, name='program_list'),
    path('sistema/', admin_system, name='admin_system'),

    # CRUD
    path('programacao/cadastrar/', program_create, name='program_create'),
    path('programacao/<int:pk>/atualizar/', program_update, name='program_update'),
    path('programacao/<int:pk>/deletar/', program_delete, name='program_delete'),
    
    # AUTH
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cadastro/', register, name='register'),
    

]