from django.contrib import admin

# Register your models here.
from .models import MyData


admin.site.register(MyData)