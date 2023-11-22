from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect, HttpResponse  
from django.urls import reverse
from .models import Task, regis, User
from .forms import regisForm
from django.utils import timezone
import xlwt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from django.contrib.auth.decorators import user_passes_test
from collections import defaultdict




# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            return redirect('buscar')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})




@login_required
def signout(request):
    return redirect(request, 'singnin')

def logout(request):
    return redirect (request, 'singnin')



def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('buscar')  
        else:
            return render(request, 'signin.html', {'form': form, 'error': 'Username or password is incorrect.'})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})


registros_acumulados = []

def buscar(request):
    busqueda_actual = None
 


    if request.method == 'POST':
        query = request.POST.get('busqueda', '')
        busqueda_actual = {
            'query': query,
            'fecha_busqueda': datetime.now(),
        }
        
        if not query:
            messages.warning(request, 'Por favor, ingrese un término de búsqueda.')
        else:        
            resultados = regis.objects.filter(
                Q(ml__exact=query) | Q(nombre_pc__exact=query) | Q(nombre_user__exact=query) |
                Q(cedula__exact=query) | Q(centro_costos__exact=query) | Q(departamento__exact=query) |
                Q(sede__exact=query)
            )
        

            if not resultados:
                messages.info(request, 'No se encontraron resultados para la búsqueda.')
                return redirect('agregar_registro') 

            registros_acumulados.append({
                'query': query,
                'resultados': resultados,
                'fecha_busqueda': busqueda_actual['fecha_busqueda'],

            })

    # Ordenar los resultados acumulados por fecha de búsqueda (de más reciente a más antigua)
    registros_acumulados.sort(key=lambda x: x['fecha_busqueda'], reverse=True)

    # Renderizar la plantilla
    return render(request, 'buscar.html', {'registros_acumulados': registros_acumulados, 'busqueda_actual': busqueda_actual})


@login_required
def limpiar_registros(request):
    global registros_acumulados  # Accede a la lista en memoria
    registros_acumulados = []  # Limpia la lista en memoria
    return redirect('buscar')

def agregar_registro(request):
    if request.method == 'POST':
        form = regisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('buscar')
    else:
        form = regisForm() 
    return render(request, 'agregar_registro.html', {'form': form})

def modificar_registro(request, id):
    registro = regis.objects.get(id=id)
    if request.method == 'POST':
        form = regisForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('buscar')
    else:
        form = regisForm(instance=registro)
    
    return render(request, 'modificar_registro.html', {'form': form})




"""
@login_required
def buscar(request):
    registros = regis.objects.all()  
    query = request.GET.get('q')
    listado = []
    
    if query:
        registros = registros.filter(ml__icontains=query).all()
        for registro in registros:
            line = {'ml': registro.ml, 
                    'nombre_pc': registro.nombre_pc,
                    'nombre_user': registro.nombre_user, 
                    'cedula': registro.centro_costos,
                    'centro_costros':registro.centro_costos,
                    'sede': registro.sede,
                    'fecha': datetime.now()}
        print (list(registros))
    form = regisForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarea agregada exitosamente.')
            return redirect('buscar')

    if not registros:
        if query:
            return redirect('agregar')
        else:
            return HttpResponse("No hay datos para mostrar.")

    return render(request, 'buscar.html', {'registros': registros, 'query': query, 'form': form})

#@login_required
#def agregar(request):
 #   if request.method == 'POST':
  #      form = regisForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       messages.success(request, 'Tarea agregada exitosamente.')
      #      return redirect('buscar')
    #else:
     #   form = regisForm()
    
    #return render(request, 'agregar.html', {'form': form})

#def export_to_excel(request):
   # response = HttpResponse(content_type='application/ms-excel')
   # response['Content-Disposition'] = 'attachment; filename="datos.xlsx"'

    #wb = xlwt.Workbook(encoding='utf-8')
    #ws = wb.add_sheet('Datos')

    #row_num = 0
    #columns = ['ML', 'Nombre de PC', 'Nombre de Usuario', 'Cédula', 'Centro de Costos', 'Departamento', 'Sede', 'Fecha de Búsqueda']

    #for col_num, column_title in enumerate(columns):
        #ws.write(row_num, col_num, column_title)

    #registros = Task.objects.all()
    #for registro in registros:
        #row_num += 1
       # row = [registro.ml, registro.nombre_pc, registro.nombre_user, registro.cedula, registro.centro_costos, registro.departamento, registro.sede, registro.fecha_busqueda]
      #  for col_num, cell_value in enumerate(row):
     #       ws.write(row_num, col_num, cell_value)

    #wb.save(response)
    #return response

#def send_email_with_attachment(email, file_path):
    #from_email = 'tu_email@gmail.com'
    #to_email = email

    #msg = MIMEMultipart()
    #msg['From'] = from_email
    #msg['To'] = to_email
    #msg['Subject'] = 'Datos en formato Excel'

    #part = MIMEBase('application', 'octet-stream')
    #part.set_payload(open(file_path, 'rb').read())
    #encoders.encode_base64(part)
    #part.add_header('Content-Disposition', 'attachment; filename="datos.xlsx"')
    #msg.attach(part)

    #server = smtplib.SMTP('smtp.gmail.com', 587)
    #server.starttls()
    #server.login(from_email, 'tu_contraseña')
    #server.sendmail(from_email, to_email, msg.as_string())
    #server.quit()"""