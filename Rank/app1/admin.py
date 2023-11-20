from django.contrib import admin
from .models import CustomUser, Rank

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Rank)