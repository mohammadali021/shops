from django.contrib import admin

from shops.models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_sale', 'sale_price', 'is_available', 'slug')
    list_editable = ('price', 'category', 'is_sale', 'sale_price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    # prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
admin.site.register(Category , CategoryAdmin)
admin.site.register(Order)
admin.site.register(Customer)
