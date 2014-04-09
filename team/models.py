from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField
from publications.models import Publication

# AILab research projects
class Project(Page):
	funder = models.CharField(max_length=100, blank=True)
	program = models.CharField(max_length=300, blank=True)
	funding = models.CharField(max_length=100, blank=True)
	url = models.CharField(max_length=100, blank=True)
	startyear = models.IntegerField(max_length=4)
	endyear = models.IntegerField(max_length=4)
	people_list = models.CharField(max_length=300, blank=True)

	publications = models.ManyToManyField(Publication)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _("Project")
		verbose_name_plural = _("Projects")

# AILab employee and the related information
class Person(Page):
	asciiname = models.CharField(max_length=100)
	
	degree = models.CharField(max_length=100, blank=True)
	position_en = models.CharField(max_length=100, blank=True)	
	position_lv = models.CharField(max_length=100, blank=True)

	email = models.CharField(max_length=100, blank=True)
	ailab_employee = models.BooleanField(default=True)

	user = models.ForeignKey(User, null=True, blank=True)
	researchgate_url = models.CharField(max_length=300, blank=True)
	linkedin_url = models.CharField(max_length=300, blank=True)
	scholar_url = models.CharField(max_length=300, blank=True)
	github_url = models.CharField(max_length=300, blank=True)

	interests_en = models.CharField(max_length=300, blank=True)
	interests_lv = models.CharField(max_length=300, blank=True)

	projects = models.ManyToManyField(Project)
	publications = models.ManyToManyField(Publication)

	content_en = RichTextField(_("Content_EN"), blank=True)
	content_lv = RichTextField(_("Content_LV"), blank=True)

	search_fields = ("content_en", "content_lv")

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _("Person profile / CV")
		verbose_name_plural = _("Person profiles / CVs")

