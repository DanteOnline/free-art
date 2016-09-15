from django.contrib import admin
from team.models import Developer, Tester
from modeltranslation.admin import TabbedTranslationAdmin

# Register your models here.
class DeveloperAdmin(TabbedTranslationAdmin):
    list_display = ['name','role']

admin.site.register(Developer, DeveloperAdmin)

class TesterAdmin(TabbedTranslationAdmin):
    list_display = ['name']

admin.site.register(Tester, TesterAdmin)