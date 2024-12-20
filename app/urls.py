from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path('', index, name='index'),
    path('programacao/', program_list, name='program_list'),
    path('sistema/', admin_system, name='admin_system'),

    # CRUD INICIO - CARROSEL
    path('sistema/carrosel/', home_list_system, name='home_list_system'),
    path('cadastrar/carrosel', img_carousel_create, name='img_carousel_create'),
    path('cadastrar/carrosel', img_carousel_create, name='img_carousel'),
    path("<int:pk>/atualizar/carrosel", img_carousel_update, name="img_carousel_update"),
    path('<int:pk>/deletar/carrosel', img_carousel_delete, name='img_carousel_delete'),
    
    # CRUD INICIO - WARNING
    path('sistema/avisos/', warning_list_system, name="warning_list_system"),
    path('cadastrar/avisos/', warning_create, name='warning_create'),
    path('<int:pk>/atualizar/avisos', warning_update, name='warning_update'),
    path('<int:pk>/deletar/avisos', warning_delete, name='warning_delete'),

    # CRUD INICIO - SOBRE
    path('sistema/sobre/', about_list_system, name="about_list_system"),
    # path('cadastrar/avisos/', warning_create, name='warning_create'),
    path('<int:pk>/atualizar/sobre', about_update, name='about_update'),
    
    # CRUD INICIO - MEMBROS DA RADIO
    path('sistema/equipe/', profile_list_system, name="profile_list_system"),
    path('cadastrar/equipe/', profile_create, name='profile_create'),
    path('<int:pk>/atualizar/equipe', profile_update, name='profile_update'),
    path('<int:pk>/deletar/equipe', profile_delete, name='profile_delete'),

    # CRUD PROGRAMAS
    path('sistema/programas/', program_list_system, name='program_list_system'),
    path('cadastrar/programas/', program_create, name='program_create'),
    path('<int:pk>/atualizar/programas', program_update, name='program_update'),
    path('<int:pk>/deletar/programas', program_delete, name='program_delete'),
    # EP PROGRA'MAS
    path('programas/<int:pk>/', program_detail, name='program_detail'),
    path('cadastrar/programas/<int:pk>/episodios', programep_create, name='programep_create'),
    # path('<int:pk>/atualizar/episodios', programep_update, name='programep_update'),


    # CRUD PEDIDOS
    path('pedidos', pedidos_list, name='pedidos_list'),
    
    # AUTH
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cadastro/', register, name='register'),
    

]