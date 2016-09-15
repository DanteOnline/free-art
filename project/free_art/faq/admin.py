from django.contrib import admin
from faq.models import Faq
from modeltranslation.admin import TabbedTranslationAdmin

# Register your models here.
class FaqAdmin(TabbedTranslationAdmin):
    list_display = ['question']

admin.site.register(Faq, FaqAdmin)
