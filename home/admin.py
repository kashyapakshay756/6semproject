from django.contrib import admin
from home.models import form
from home.models import serviceform
from home.models import need
from .models import *

# Register your models here.


class helo(admin.ModelAdmin):
    list_display = ('name', 'email', 'mobile')
    list_editable = ('email', 'mobile')
    search_fields = ('mobile', 'name')
    ordering = ['name']


admin.site.register(form, helo)


class service(admin.ModelAdmin):
    list_display = ('name', 'email', 'services', 'adderess', 'message')
    search_fields = ('name', 'email', ' services')


admin.site.register(serviceform, service)


admin.site.register(need)

admin.site.register(Donate)
