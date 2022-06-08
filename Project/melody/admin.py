from django.contrib import admin
from melody.models import Customer, Song
# Register your models here.

# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     list_display('id', 'firstname', 'lastname', 'address')
#     ordering('id')
#     search_fields('firstname', 'lastname')

admin.site.register(Customer)
admin.site.register(Song)