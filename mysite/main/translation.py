from .models import Person
from modeltranslation.translator import register, TranslationOptions

@register(Person)
class PersonTranslationOptions(TranslationOptions):
    fields = ('name', 'about',)