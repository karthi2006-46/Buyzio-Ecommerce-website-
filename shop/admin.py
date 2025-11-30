from django.contrib import admin
from .models import *

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'image', 'description')  # corrected spelling
# admin.site.register(category,CategoryAdmin)

admin.site.register(category)
admin.site.register(Products)
