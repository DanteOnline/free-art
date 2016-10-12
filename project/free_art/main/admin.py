from django.contrib import admin
from how_to_use.models import Subject, Step
from modeltranslation.admin import TabbedTranslationAdmin

# Register your models here.
class SubjectAdmin(TabbedTranslationAdmin):
    list_display = ['name']

admin.site.register(Subject, SubjectAdmin)

class StepAdmin(TabbedTranslationAdmin):
    list_display = ['number','name','subject']

admin.site.register(Step,StepAdmin)
