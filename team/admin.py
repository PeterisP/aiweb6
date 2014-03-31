from django.contrib import admin

# Register your models here.
from mezzanine.pages.admin import PageAdmin
from .models import Person

admin.site.register(Person, PageAdmin)