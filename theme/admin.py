from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import DualLangPage

admin.site.register(DualLangPage, PageAdmin)