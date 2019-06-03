from modeltranslation.translator import register, TranslationOptions
from products.models import Product, ProductsPage


@register(ProductsPage)
class ProductsPageTranslationOptions(TranslationOptions):
    fields = ('content', )

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'season')

