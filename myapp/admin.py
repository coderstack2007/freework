from django.contrib import admin
from .models import MyModel, MyModel2, MyModel3

admin.site.register(MyModel)
admin.site.register(MyModel2)
admin.site.register(MyModel3)
