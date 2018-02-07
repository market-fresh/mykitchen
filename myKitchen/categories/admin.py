from django.contrib import admin

# Register your models here.
from categories.models import Category, Categories_Defined

admin.site.register(Category)
admin.site.register(Categories_Defined)
