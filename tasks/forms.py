from django.forms import ModelForm
from .models import Task, regis

class regisForm(ModelForm):
    class Meta:
        model = regis
        db_table = 'regist'
        fields = ['ml', 'nombre_pc', 'nombre_user', 'cedula', 'centro_costos', 'departamento', 'sede']