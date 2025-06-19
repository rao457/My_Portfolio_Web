from django.contrib import admin
from .models import ContactModel
# Register your models here.

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'timestamp', 'replied')
    search_fields = ('name', 'email', 'message')