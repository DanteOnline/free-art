from django.contrib import admin
from item.models import Script, Category, ScriptParam
from modeltranslation.admin import TabbedTranslationAdmin

# Register your models here.
class CategoryAdmin(TabbedTranslationAdmin):
    list_display = ['parent','name','has_image','is_top','is_middle','is_leaf']

admin.site.register(Category, CategoryAdmin)

class ScriptAdmin(TabbedTranslationAdmin):
    list_display = ['name','category']

admin.site.register(Script, ScriptAdmin)

class ScriptParamAdmin(TabbedTranslationAdmin):
    pass

admin.site.register(ScriptParam,ScriptParamAdmin)