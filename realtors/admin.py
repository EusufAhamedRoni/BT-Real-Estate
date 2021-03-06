from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'hire_date')
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Realtor, RealtorAdmin)
