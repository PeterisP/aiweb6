__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Lucas Theis <lucas@theis.io>'
__docformat__ = 'epytext'

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from publications.bibtex import import_bibtex_data, parse
from publications.models import Publication, Type

def import_bibtex(request):
	if request.method == 'POST':

		if not request.POST['bibliography']:
			errors = {'bibliography' : 'This field is required.'}
		else:
			# try to parse BibTex
			bib = parse(request.POST['bibliography'])
			response = import_bibtex_data(bib)
			errors = response['errors']

		if errors:
			# some error occurred
			return render_to_response(
				'admin/publications/import_bibtex.html', {
					'errors': errors,
					'title': 'Import BibTex',
					'types': Type.objects.all(),
					'request': request},
				RequestContext(request))
		else:		
			# show message
			messages.info(request, response['msg'])

			# redirect to publication listing
			return HttpResponseRedirect('../')
	else:
		return render_to_response(
			'admin/publications/import_bibtex.html', {
				'title': 'Import BibTex',
				'types': Type.objects.all(),
				'request': request},
			RequestContext(request))

import_bibtex = staff_member_required(import_bibtex)
