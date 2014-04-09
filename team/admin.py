from django.contrib import admin

# Register your models here.
from mezzanine.pages.admin import PageAdmin
from .models import Person, Project

admin.site.register(Person, PageAdmin)
admin.site.register(Project, PageAdmin)