from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import Product, ProductsPage


class ProductInline(admin.TabularInline):
    model = Product


class ProductsPageAdmin(PageAdmin):
    inlines = (ProductInline,)


admin.site.register(ProductsPage, ProductsPageAdmin)