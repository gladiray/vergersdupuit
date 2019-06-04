from django.db import models
from mezzanine.core.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page, RichText, Orderable

# Create your models here.


class HomePage(models.Model):
    extra_css_for_page = models.CharField(_("CSS to add to page"), blank=True, null=True, max_length=2000, help_text="for exemple: .green-room {background-color: #9D090E;color: white;}")


    @classmethod
    def get_homepage_info(cls):
        return cls.objects.all()[0]


class HomePageSection(Orderable):
    page = models.ForeignKey(HomePage)
    text = RichTextField(_("Text content"), blank=True, null=True)
    photo1 = models.ImageField(_("Photo 1"), upload_to="upload/", blank=True, null=True)
    alt_photo1 = models.CharField(_("Alternative text for photo1"), blank=True, null=True, max_length=200)
    photo2 = models.ImageField(_("Photo 2"), upload_to="upload/", blank=True, null=True)
    alt_photo2 = models.CharField(_("Alternative text for photo2"), blank=True, null=True, max_length=200)
    extra_css_for_section = models.CharField(_("CSS to add to section"), blank=True, null=True, max_length=2000, help_text="{background-color: #9D090E;color: white;}")
