from modeltranslation.translator import translator, TranslationOptions
from team.models import Developer, Tester

class DeveloperTranslationOptions(TranslationOptions):

    fields = ('name','role')

translator.register(Developer, DeveloperTranslationOptions)

class TesterTranslationOptions(TranslationOptions):
    fields = ['name']

translator.register(Tester, TesterTranslationOptions)