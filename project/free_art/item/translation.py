from modeltranslation.translator import translator, TranslationOptions
from item.models import Category, Script, ScriptParam

class CategoryTranslationOptions(TranslationOptions):

    fields = ('name','short_desc','full_desc')

translator.register(Category, CategoryTranslationOptions)

class ScriptTranslation(TranslationOptions):
    fields = ('name','short_desc','full_desc')

translator.register(Script, ScriptTranslation)

class ScriptParamTranslation(TranslationOptions):
    fields = ('name','desc','default_value')

translator.register(ScriptParam, ScriptParamTranslation)