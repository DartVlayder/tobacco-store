from django.contrib import admin

from goods.models import Categories, Products

#admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'slug']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'quantity','price','discount']
    list_editable = ['price','discount']
    search_fields = ['name', 'description']
    list_filter = ['discount', 'description', 'category']
    fieldsets = [
        'name',
        'category',
        'slug',
        'description',
        'image',
        ('price', 'discount'),
        'quantity',
    ]