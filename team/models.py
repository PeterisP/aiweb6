from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField

class Person(Page):
	initials = models.CharField(max_length=100, blank=True)
	position_en = models.CharField(max_length=100, blank=True)	
	position_lv = models.CharField(max_length=100, blank=True)

	email = models.CharField(max_length=100, blank=True)
	ailab_employee = models.BooleanField(default=True)

	user = models.ForeignKey(User, null=True, blank=True)
	researchgate_url = models.CharField(max_length=300, blank=True)
	linkedin_url = models.CharField(max_length=300, blank=True)
	scholar_url = models.CharField(max_length=300, blank=True)

	projects_en = RichTextField(_("Projects_EN"), blank=True)
	projects_lv = RichTextField(_("Projects_LV"), blank=True)

	publications_en = RichTextField(_("Publications_EN"), blank=True)
	publications_lv = RichTextField(_("Publications_LV"), blank=True)

	search_fields = ("content_en","content_lv")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _("Person profile / CV")
		verbose_name_plural = _("Person profiles / CVs")


