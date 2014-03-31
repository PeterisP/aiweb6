from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.fields import RichTextField
from django.utils.translation import ugettext, ugettext_lazy as _

class DualLang(models.Model):
	"""
	Implements a page with dual language rich text content
	Currently hardcoded to EN/LV, but could be made generic
	"""

	title_lv = models.CharField(_("Title_LV"), max_length=500)

	content_en = RichTextField(_("Content_EN"), blank=True)
	content_lv = RichTextField(_("Content_LV"), blank=True)

	search_fields = ("content_en","content_lv")

	class Meta:
		abstract = True

class DualLangPage(Page, DualLang):
	"""
	Implements a page with dual language rich text content
	Currently hardcoded to EN/LV, but could be made generic
	"""

	class Meta:
		verbose_name = _("Dual language page")
		verbose_name_plural = _("Dual language pages")
