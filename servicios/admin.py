from django.contrib import admin
from .models import Servicios

class ServiciosAdmin(admin.ModelAdmin):
    readonly_fields = ("created", ) #solo lectura

# Register your models here.
admin.site.register(Servicios, ServiciosAdmin)