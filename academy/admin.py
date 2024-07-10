from django.contrib import admin
from .models import model

# Register your models here.

for i in model:
    admin.site.register(i)
