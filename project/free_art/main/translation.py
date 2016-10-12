from modeltranslation.translator import translator, TranslationOptions
from how_to_use.models import Subject, Step

class SubjectTranslationOptions(TranslationOptions):
    fields = ['name']

translator.register(Subject, SubjectTranslationOptions)

class StepTranslationOptions(TranslationOptions):
    fields = ('name','description')

translator.register(Step, StepTranslationOptions)