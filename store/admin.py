from django.contrib import admin

from .models import Category, Product , Banner


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price',
                    'in_stock', 'created', 'updated','is_active']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['baslik', 'slug']
    prepopulated_fields = {'slug': ('baslik',)}
    list_filter = ['is_active']