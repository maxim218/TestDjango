from django.contrib import admin
from .models import MyFirstModel
from .models import MyModelForSum

admin.site.register(MyFirstModel)
admin.site.register(MyModelForSum)
