from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UseradminAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'contact_no')
