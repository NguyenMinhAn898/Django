from django.contrib import admin

# Register your models here.

from .models import Category, Place, Blog

# admin.site.register(User)
admin.site.register(Category)
admin.site.register(Place)
admin.site.register(Blog)