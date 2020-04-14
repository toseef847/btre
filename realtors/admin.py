from django.contrib import admin
from .models import Realtor

# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('name','is_mvp','email','phone','hire_date')
    search_fields = ('name',)
admin.site.register(Realtor, RealtorAdmin)