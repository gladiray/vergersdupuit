from modeltranslation.translator import register, TranslationOptions
from homepage.models import HomePage, HomePageSection


@register(HomePageSection)
class HomePageSectionTranslationOptions(TranslationOptions):
    fields = ('text', 'alt_photo1', 'alt_photo2')

"""

@register(StartPage)
class StartPageTranslationOptions(TranslationOptions):
    fields = ('content', )



"""