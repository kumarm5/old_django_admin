from django.contrib import admin
from . import models

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_title', 'status', 'date_created')
    
admin.site.register(models.Blog_category, CategoryAdmin)
