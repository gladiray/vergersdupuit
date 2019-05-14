from django.db import models
from mezzanine.pages.models import Page, RichText
from django.utils.translation import ugettext_lazy as _


class ProductsPage(Page, RichText):
    pass


class Product(models.Model):
    container_page = models.ForeignKey(ProductsPage)
    name = models.CharField(_("Name"), max_length=500)
    description = models.CharField(_("Description"), max_length=1000, blank=True, null=True)
    season = models.CharField(_("Season"), max_length=200, blank=True, null=True)
    photo = models.ImageField(_("Products photo"), upload_to="upload/")
