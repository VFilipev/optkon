from django.contrib import admin
from catalog import models

class PhotosInline(admin.TabularInline):
    model=models.Photos
    extra = 10

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines=[PhotosInline]

admin.site.register(models.Category)
