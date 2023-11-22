"""
URL configuration for projectpru project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signin, name='signin'),
    #path('home/', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    #path('lista/', views.lista, name='lista'),
    #path('agregar/', views.agregar, name='agregar'),
    #path('tasks/', views.tasks, name='tasks'),
    path('logout/', views.signout, name='logout'),
    path('buscar/', views.buscar, name='buscar'),
    path('agregar/', views.agregar_registro, name='agregar_registro'),
    path('modificar/<int:id>/', views.modificar_registro, name='modificar_registro'),
    path('limpiar_registros/', views.limpiar_registros, name='limpiar_registros'),  # Agrega esta línea
    #path('limpiar/', views.limpiar_registros, name='limpiar_registros'),
    #path('create_task/', views.create_task, name='create_task'),
    #path('tasks/<int:task_id>', views.task_detail, name='task_detail'),
    #path('taks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    #path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    #path('finalizar-busqueda/', views.finalizar_busqueda, name='finalizar_busqueda'),


]
