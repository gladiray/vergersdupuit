from django.contrib import admin
from homepage.models import HomePage, HomePageSection

class HomePageSectionInline(admin.StackedInline):
    model = HomePageSection


class HomePageAdmin(admin.ModelAdmin):
    inlines = (HomePageSectionInline,)

# Register your models here.
#admin.site.register(StartPage, StartPageAdmin)
admin.site.register(HomePage, HomePageAdmin)
