from django.forms import ModelForm
from .models import MyModel
from .models import MyModel2
from .models import MyModel3

from django import forms



class MyForm(ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'
        

     
        
class MyForm2(ModelForm):
    class Meta:
        model = MyModel2
        fields = '__all__'

class MyForm3(ModelForm):
    class Meta: 
        model = MyModel3
        fields = '__all__'

