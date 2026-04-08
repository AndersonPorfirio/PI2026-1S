from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views # Importe as views de autenticação

urlpatterns = [
    path('admin/', admin.site.urls),
    # Esta linha abaixo ativa o login em templates/registration/login.html
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', include('catalog.urls')),
]