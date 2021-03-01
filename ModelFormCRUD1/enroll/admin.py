from django.contrib import admin

# Register your models here.
from .models import User

@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ("id","name",'lastname',"email","password")

