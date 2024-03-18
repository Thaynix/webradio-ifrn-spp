from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import *

urlpatterns = [
    path('', index, name='index'),
    path('programacao', programacao, name= 'programacao'),
    # CRUD
    path('programacao/cadastrar/', program_create, name='program_create'),
    path('programacao/<int:pk>/atualizar/', program_update, name='program-update'),
    path('programacao/<int:pk>/deletar/', program_delete, name='program-delete'),
    # AUTH
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)