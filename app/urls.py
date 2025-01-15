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
    # EP PROGRAMAS
    path('programas/<int:pk>/', program_detail, name='program_detail'),
    path('sistema/programas/<int:pk>/episodios/', programep_list, name='programep_list'),
    path('sistema/programas/<int:pk>/episodios/cadastrar', programep_create, name='programep_create'),
    path('<int:pk>/atualizar/episodios', programep_update, name='programep_update'),
    path('<int:pk>/deletar/episodios', programep_delete, name='programep_delete'),

    # CRUD PEDIDOS
    path('pedidos/', pedidos_create, name='pedidos_create'),
    path('sistema/pedidos/', pedidos_list_system, name='pedidos_list_system'),
    path('<int:pk>/deletar/pedidos/', pedidos_delete, name='pedidos_delete'),
    # path('<int:pk>/aceitar/pedidos/', pedido_aceito, name='pedido_aceito'),
    # path('<int:pk>/negar/pedidos/', pedido_negado, name='pedido_negado'),
    
    # CRUD CALENDARIO
    path('calendario/', calendar, name='calendar'),
    path('cadastrar/calendario/', calendar_create, name='calendar_create'),
    path("sistema/calendario/", calendar_list, name="calendar_list"),
    path('<int:pk>/atualizar/calendario', calendar_update, name='calendar_update'),
    path('<int:pk>/deletar/calendario', calendar_delete, name='calendar_delete'),
    
    # CRUD USUARIOS
    path('usuario/', user_create, name='user_create'),
    path('sistema/usuarios/', user_list, name='user_list'),
    path('<int:pk>/atualizar/usuarios', user_update, name='user_update'),
    path('<int:pk>/deletar/usuarios', user_delete, name='user_delete'),
    path('<int:pk>/atualizar-senha/usuarios', user_update_password, name='user_update_password'),
    
    # AUTH
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('cadastro/', register, name='register'),
    

]