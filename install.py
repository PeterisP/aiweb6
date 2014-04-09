#!/usr/bin/env python

from os import environ
environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from settings import *
from theme.models import DualLangPage
from team.models import Person, Project
from publications.bibtex import import_bibtex_data, parse
from publications.models import Publication
from collections import namedtuple
import json

def createPage (title, title_lv, content_en='', content_lv='', parent_id = None):
	p = DualLangPage(title=title, title_lv = title_lv, content_en=content_en, content_lv=content_lv, parent_id = parent_id)
	p.save()
	return p.id

about_text = "<p class=\"p1\">Kop\u0161 savas darb\u012bbas pirms\u0101kumiem 1989.\u00a0gad\u0101 LU Matem\u0101tikas un inform\u0101tikas instit\u016bta (LUMII) M\u0101ksl\u012bg\u0101 intelekta laboratorijas (AILab) galvenais p\u0113t\u012bjumu virziens ir bijusi datorlingvistika. AILab darb\u012bba latvie\u0161u valodas datorlingvistikas p\u0113t\u012bjumos un izstr\u0101d\u0113s notiek vair\u0101kos virzienos (Mil\u010donoka\u00a0et\u00a0al.\u00a02004; Gr\u016bz\u012btis\u00a0et\u00a0al. 2004; B\u0101rzdi\u0146\u0161\u00a0u.\u00a0c.\u00a02006; Skadi\u0146a\u00a0et\u00a0al.\u00a02010; Gr\u016bz\u012btis\u00a02012), aptverot praktiski visus anal\u012bzes un sint\u0113zes l\u012bme\u0146us:</p>\n<p class=\"p1\">\u2013 gramatikas anal\u012bzes un sint\u0113zes metodes un r\u012bkus,</p>\n<p class=\"p1\">\u2013 rakst\u012bt\u0101s un run\u0101t\u0101s valodas korpusus (uzkr\u0101\u0161anu un mar\u0137\u0113\u0161anu),</p>\n<p class=\"p1\">\u2013 ma\u0161\u012bnlas\u0101m\u0101s v\u0101rdn\u012bcas un leksisk\u0101s ontolo\u0123ijas (semantiskos t\u012bklus),</p>\n<p class=\"p1\">\u2013 likumb\u0101z\u0113to un statistisko ma\u0161\u012bntulko\u0161anu,</p>\n<p class=\"p1\">\u2013 semantisk\u0101s anal\u012bzes un diskursa reprezent\u0101cijas metodes,</p>\n<p class=\"p1\">\u2013 kontrol\u0113tas dabisk\u0101s valodas un form\u0101las valodas mijiedarb\u012bbu,</p>\n<p class=\"p1\">\u2013 runas sint\u0113zi un (eksperiment\u0101lu) anal\u012bzi.</p>"
about_en = "Since 1987 the Artificial Intelligence Laboratory (AILab) at the Institute of Mathematics and Computer Science of the University of Latvia has been concerned with natural language processing. It is one of the major centres dealing with the collection and exploration of Latvian lexical data in the NLP in Latvia. at the Laboratory."
createPage('About', 'Par mums', about_en, about_text)

team_id = createPage('Team', 'Komanda')

#research_text = "<p class=\"p1\">SIA \u201cIT kompetences centrs\u201d p\u0113t\u012bjumu projekts Nr. 2.7. \u201cTeksta autom\u0101tiskas datorlingvistiskas anal\u012bzes p\u0113t\u012bjums jauna inform\u0101cijas arh\u012bva produkta izstr\u0101d\u0113\u201d (2013); apjoms\u00a0\u2014 Ls 98\u00a0643,19</p>\n<p class=\"p1\">SIA \u201cIT kompetences centrs\u201d p\u0113t\u012bjumu projekts Nr. 2.10. (2013)</p>\n<p class=\"p2\">Valsts p\u0113t\u012bjumu programmas Nr.3\u00a0 \u201eNacion\u0101l\u0101 identit\u0101te (valoda, Latvijas v\u0113sture, kult\u016bra un cilv\u0113kdro\u0161\u012bba)\u201d projekts Nr.3 \u201eValoda \u2013 nacion\u0101l\u0101s identit\u0101tes pamats 3.4. Latvie\u0161u valodas gramatika un elektroniskie resursi\u201d (2010\u20132013);\u00a0 apjoms\u00a0\u2014</p>\n<p class=\"p3\">Valsts p\u0113t\u012bjumu programmas Nr.2\u00a0 \u201eInovat\u012bvu daudzfunkcion\u0101lu materi\u0101lu, sign\u0101lapstr\u0101des un inform\u0101tikas tehnolo\u0123iju izstr\u0101de konkur\u0113tsp\u0113j\u012bgiem zin\u0101t\u0146u ietilp\u012bgiem produktiem\u201d projekts Nr.5 \u201eJaunas inform\u0101cijas tehnolo\u0123ijas, balst\u012btas uz ontolo\u0123ij\u0101m un mode\u013cu transform\u0101cij\u0101m\u201d (2010\u20132013); apjoms\u00a0\u2014</p>\n<p class=\"p4\">ERAF darb\u012bbas programmas \u201eUz\u0146\u0113m\u0113jdarb\u012bba un inov\u0101cijas\u201d aktivit\u0101tes \u201eAtbalsts zin\u0101tnei un p\u0113tniec\u012bbai\u201d projekts Nr. 2011/0009/2DP/2.1.1.1.0/10/APIA/VIAA/112 \u201cSemantisko datub\u0101zu platforma nozaru speci\u0101listiem\u201d (2011\u20132013); apjoms\u00a0\u2014 Ls 410\u00a0968 Pla\u0161\u0101k sk. (k\u0101da ir lapa???)</p>\n<p class=\"p5\"></p>\n<p class=\"p4\">Dal\u012bba Latvijas\u2013Lietuvas p\u0101rrobe\u017eu sadarb\u012bbas programmas projekt\u0101 \u201eHumanit\u0101r\u0101s izgl\u012bt\u012bbas p\u0113tniec\u012bbas infrastrukt\u016bras izveide Austrumlatvij\u0101, Lietuv\u0101\u201d (\u201eHipiLatLit\u201d) (2007\u20132013); apjoms\u00a0\u2014 395 758,00 EUR. Pla\u0161\u0101k sk. http://hipilatlit.ru.lv/lv/</p>\n<p class=\"p5\"></p>\n<p class=\"p1\">\u201eSen\u0101s rakst\u012bbas tulko\u0161anas risin\u0101juma izstr\u0101de\u201d, \u012bstenojot ERAF projektu \u201eDigit\u0101l\u0101s bibliot\u0113kas pakalpojumu att\u012bst\u012bba\u201d, iepirkums nr. LNB/2011/39/ERAF (2013); apjoms\u00a0\u2014 Ls\u00a024\u00a0351</p>\n<p class=\"p4\">Latvie\u0161u valodas a\u0123ent\u016bras projekts \u201eL\u012bdzsvarota m\u016bsdienu latvie\u0161u valodas tekstu korpusa papla\u0161in\u0101\u0161ana\u201d, l\u012bgums Nr. 4.6/2012-9 // 3-27-27 (15.10.2012.\u201328.02.2013.); apjoms\u00a0\u2014 3000</p>\n<p class=\"p5\"></p>\n<p class=\"p5\"></p>\n<p class=\"p6\"><b>[beigu gads] 2012</b></p>\n<p class=\"p5\"></p>\n<p class=\"p4\">\u201eLatvie\u0161u valodas atbalsta r\u012bku izstr\u0101de resursu atkl\u0101\u0161anai\u201d, \u012bstenojot ERAF projektu \u201eDigit\u0101l\u0101s bibliot\u0113kas pakalpojumu att\u012bst\u012bba\u201d; iepirkums Nr. LNB/2011/33/ERAF (2012); apjoms\u00a0\u2014 Ls 50\u00a0203</p>\n<p class=\"p5\"></p>\n<p class=\"p7\">R\u012bgas pa\u0161vald\u012bbas a\u0123ent\u016bras \u201eR\u012bgas pils\u0113tas arhitekta birojs\u201d pas\u016bt\u012bjums \u201ePils\u0113tvides terminolo\u0123ijas v\u0101rdn\u012bcas digitaliz\u0101cija un interneta versijas mode\u013ca izveide\u201d, l\u012bgums Nr.\u00a03-27-35 (1.11.2012.\u201320.12.2012); apjoms\u00a0\u2014 Ls\u00a03000</p>\n<p class=\"p5\"></p>\n<p class=\"p6\"><b>[beigu gads] 2011</b></p>\n<p class=\"p5\"></p>\n<p class=\"p4\">ES 7.\u00a0pamatprogrammas projekts \u201eCommon Language Recources and Technology Infrastructure\u201d (Vienota valodas resursu un tehnolo\u0123iju infrastrukt\u016bra; CLARIN), l\u012bgums Nr. ES 10-19//3-27-13, sagatavo\u0161anas posms\u00a0\u2014 CLARIN organiz\u0101cijas izveide, pl\u0101no\u0161ana, prototipa izveide (2008\u20132011); apjoms\u00a0\u2014 20\u00a0550. Pla\u0161\u0101k sk. http://clarin.lv/</p>\n<p class=\"p4\">Latvie\u0161u valodas a\u0123ent\u016bras projekts \u201eL\u012bdzsvarot\u0101 m\u016bsdienu latvie\u0161u valodas tekstu korpusa satura vad\u012bbas sist\u0113mas izstr\u0101de un metadatu standartiz\u0113\u0161ana\u201d, l\u012bgums Nr. 4.6/9-2010 // 3-27-19 (1.12.2010.\u201315.06.2011.); apjoms\u00a0\u2014 Ls\u00a03000</p>\n<p class=\"p5\"></p>\n<p class=\"p6\"><b>[beigu gads] 2010</b></p>\n<p class=\"p5\"></p>\n<p class=\"p1\">Latvijas Zin\u0101tnes padomes grants 09.1544 \u201eFaktor\u0113to meto\u017eu lietojums ang\u013cu-latvie\u0161u statistiskaj\u0101 ma\u0161\u012bntulko\u0161anas sist\u0113m\u0101, iek\u013caujot inform\u0101tikas instrumentu \u012bpa\u0161\u0101 noz\u012bm\u012bguma un funkciju Latvijas t\u0101l\u0101kai izaugsmei anal\u012bzi, mode\u013cu izv\u0113les un to adekv\u0101tuma p\u0101rbaudi\u201d (2009\u20132012); apjoms\u00a0\u2014 16\u00a0165. Pla\u0161\u0101k sk. http://smtdemo.ailab.lv/</p>\n<p class=\"p5\"></p>\n<p class=\"p6\"><b>[beigu gads] 2009</b></p>\n<p class=\"p5\"></p>\n<p class=\"p4\">Valsts p\u0113t\u012bjumu programmas \u201eInform\u0101cijas tehnolo\u0123iju zin\u0101tnisk\u0101 b\u0101ze\u201d projekts \u201eSemantisk\u0101 t\u012bmek\u013ca izp\u0113te, att\u012bst\u012b\u0161ana un piem\u0113ro\u0161ana Latvijas vajadz\u012bb\u0101m\u201d (2005\u20132009); apjoms\u00a0\u2014 Ls 494\u00a0944. Pla\u0161\u0101k sk. http://www.semti-kamols.lv/</p>\n<p class=\"p3\">Valsts p\u0113t\u012bjumu programmas \u201eLetonika: p\u0113t\u012bjumi par v\u0113sturi, valodu un kult\u016bru\u201d projekts \u201eLatvie\u0161u valodas skaidrojo\u0161o v\u0101rdn\u012bcu un jaunaizguvumu datub\u0101ze\u201d (2006\u20132009); apjoms\u00a0\u2014</p>\n<p class=\"p4\">Valsts valodas a\u0123ent\u016bras atbalst\u012btais projekts \u201eL\u012bdzsvarot\u0101 m\u016bsdienu latvie\u0161u valodas tekstu korpusa papla\u0161in\u0101\u0161ana\u201d, l\u012bgums Nr. 4-9/5-2009 (2009); apjoms\u00a0\u2014 Ls\u00a09000</p>\n<p class=\"p5\"></p>\n<p class=\"p6\">Latvie\u0161u valodas runas korpuss, (2006\u20132009); apjoms\u00a0\u2014 Ls\u00a010\u00a0124</p>\n<p class=\"p5\"></p>\n<p class=\"p6\"><b>[beigu gads] 2008</b></p>\n<p class=\"p5\"></p>\n<p class=\"p1\">Latvijas Zin\u0101tnes padomes projekts Nr. 08.2172 \u201eDatoriz\u0113ta saist\u012btas runas anal\u012bze\u201d (2008); apjoms\u00a0\u2014 Ls 1497</p>\n<p class=\"p1\">Latvijas Zin\u0101tnes padomes projekts Nr. 08.2173 \u201eDatoriz\u0113t\u0101s latvie\u0161u-ang\u013cu leksikogr\u0101fijas meto\u017eu izstr\u0101de\u201d (2008); apjoms\u00a0\u2014 Ls\u00a02666</p>\n<p class=\"p1\">Valsts valodas a\u0123ent\u016bras atbalst\u012btais projekts \u201eLatvie\u0161u valodas korpusa programmat\u016bras izstr\u0101des otrais posms\u201d, l\u012bgums Nr.\u00a04-9/15-2008 (2008); apjoms\u00a0\u2014\u00a0</p>\n<p class=\"p4\">Valsts valodas a\u0123ent\u016bras atbalst\u012btais projekts \u201eLatvie\u0161u valodas korpusa programmat\u016bras izstr\u0101des pirmais posms\u201d, l\u012bgums Nr. 4\u20139/22\u20132007 // 3-27-21 (2007\u20132008); apjoms\u00a0\u2014 Ls\u00a08700\u00a0</p>\n<p class=\"p5\"></p>\n<p class=\"p6\">Valsts valodas a\u0123ent\u016bras atbalst\u012btais projekts \u201eLatvie\u0161u valodas korpusa teksta metadatu sagatavo\u0161ana\u201d, l\u012bgums Nr. 4-9/23-2007 // 3-27-22 (2007\u20132008); apjoms\u00a0\u2014 Ls\u00a09000</p>\n<p class=\"p5\"></p>\n<p class=\"p6\"><b>[beigu gads] 2007</b></p>\n<p class=\"p5\"></p>\n<p class=\"p6\">Latvijas Zin\u0101tnes padomes projekts Nr. 06.0043.5.2 \u201eLatvie\u0161u valodas runas korpuss\u201d (2005\u20132007); apjoms\u00a0\u2014 Ls 5350</p>\n<p class=\"p1\">Dal\u012bba Latvijas Zin\u0101tnes padomes projekt\u0101 Nr. 05.1359 \u201eInform\u0101cijas un sakaru tehnolo\u0123ijas: latvie\u0161u terminolo\u0123ija\u201d (2005\u20132007); apjoms\u00a0\u2014 Ls 14\u00a0076\u00a0</p>\n<p class=\"p1\">Latvijas Zin\u0101tnes padomes projekts Nr. 05.1532 \u201eUnivers\u0101las leksikona sist\u0113mas model\u0113\u0161ana latvie\u0161u valodai\u201d (2005\u20132007); apjoms\u00a0\u2014 Ls 15\u00a0573</p>\n<p class=\"p1\">Latvijas Zin\u0101tnes padomes projekts Nr. 05.1534 \u201eStatistisko meto\u017eu izv\u0113rt\u0113jums ang\u013cu \u2013 latvie\u0161u tulko\u0161anas sist\u0113m\u0101\u201d (2005\u20132007); apjoms\u00a0\u2014 Ls 11\u00a0260</p>\n<p class=\"p7\">Latvijas Zin\u0101tnes padomes projekts Nr. 05.1528 \u201eKvantu algoritmi un to sare\u017e\u0123\u012bt\u012bba\u201d (2005\u20132007); apjoms\u00a0\u2014 Ls 19\u00a0357</p>"
research_text = ""
research_id = createPage('Research', 'Pētījumi', research_text, research_text)

resource_text = "<table style=\"\" border=\"0\">\n<tbody>\n<tr>\n<td valign=\"middle\">\n<p><a href=\"http://www.semti-kamols.lv/\">www.semti-kamols.lv</a></p>\n<p><a href=\"http://www.tezaurs.lv/\">www.tezaurs.lv</a></p>\n<p><a href=\"http://www.korpuss.lv/\">www.korpuss.lv</a></p>\n<p><a href=\"http://www.clarin.lv/\">www.clarin.lv</a></p>\n<p>\u00a0</p>\n<p><a href=\"http://valoda.ailab.lv/\">valoda.ailab.lv</a></p>\n<p><a href=\"http://runa.ailab.lv/\">runa.ailab.lv</a></p>\n<p><a href=\"http://eksperimenti.ailab.lv/\">eksperimenti.ailab.lv</a></p>\n</td>\n</tr>\n</tbody>\n</table>"
createPage('Language resources', 'Valodas resursi', resource_text, resource_text)

conf_text = "<ul class=\"ul1\">\n<li class=\"li1\">LU 72. konferences Datorlingvistikas sekcija 2014. gada 19. febru\u0101r\u012b</li>\n<li class=\"li1\">18th Nordic Conference on Computational Linguistics (NODALIDA), May 12\u201313, 2011 (http://nodalida2011.lumii.lv/)\u00a0</li>\n<li class=\"li1\">4th International Conference \u201cHuman Language Technologies\u00a0\u2014 the Baltic Perspective\u201d, October 7\u20138, 2010 <b>(</b><a href=\"http://hlt2010.lumii.lv/\">http://hlt2010.lumii.lv/</a>)</li>\n<li class=\"li1\">Nordic Graduate School of Language Technology, short courses \u201cLexicography, lexicology, and corpus analysis\u201d, November 2007 (<a href=\"http://lumii.lv/ngslt/hanks/\">http://lumii.lv/ngslt/hanks</a><a href=\"http://lumii.lv/ngslt/h\">/</a>) and\u00a0 \u201cCorpus Annotation: Sentence and Discourse\u201d, March 2009 (<a href=\"http://lumii.lv/ngslt/hajicova\">http://lumii.lv/ngslt/hajicova</a>)\u00a0</li>\n<li class=\"li1\">\u201cCLARIN and the National Corpus\u201d, November 3, 2008 (http://clarin.lv/) <b>(CLARIN un Nacion\u0101l\u0101 korpusa semin\u0101rs )</b>\u00a0</li>\n<li class=\"li2\">LU 66. konferences Datorlingvistikas sekcija 2008. gada 6. febru\u0101r\u012b\u00a0</li>\n<li class=\"li1\">The First Baltic Conference \u201cHuman Language Technologies \u2014 the Baltic Perspective\u201d, April 21<b>\u2013</b>22, 2004\u00a0</li>\n<li class=\"li1\">\u201cLanguage &amp; Technology in Europe 2000\u201d, Riga, November 10\u201311, 1994</li>\n</ul>"
createPage('Conferences', 'Konferences', conf_text, conf_text)

createPage('Publications', 'Publikācijas', '', '')

def createPerson (person):
	p = Person(title=person['name'], parent_id = team_id)

	p.asciiname = person['name'].translate(str.maketrans('āčēģīķļņšūžĀČĒĢĪĶĻŅŠŪŽ','acegiklnsuzACEGIKLNSUZ'))
	if person['name'] == 'Baiba Valkovska (dzim. Saulīte)':
		p.asciiname = 'Baiba Saulite'

	p.degree = person['degree']
	p.position_lv = person['position']
	if person.get('position_en'):
		p.position_en = person['position_en']
	else:
		p.position_en = person['position']

	p.interests_lv = person['interests']
	if person.get('interests_en'):
		p.interests_en = person['interests_en']
	else:
		p.interests_en = person['interests']

	if person.get('email'):
		p.email = person.get('email')


	if person.get('researchgate'):
		p.researchgate_url = person.get('researchgate')
	if person.get('linkedin'):
		p.linkedin_url = person.get('linkedin')
	if person.get('scholar'):
		p.scholar_url = person.get('scholar')

	if person.get('interests'):
		p.interests_lv = person.get('interests')
	if person.get('url'):
		p.content_lv = '<a href="%s">%s</a>' % (person['url'], person['url'])
		p.content_en = p.content_lv
	if person.get('content'):
		p.content_lv = person.get('content')
		p.content_en = p.content_lv
	p.save()

def findPerson(name):
	surname = name.split('.')[-1].strip()
	if surname=='Saulīte':
		surname='Saulite'
	if surname=='Rabante' or surname=='Rābante':
		surname='Rābante-Buša'


	for person in Person.objects.all():		
		if person.title.endswith(surname) or person.asciiname.endswith(surname):
			return person

	neatrodamie = ['Balodis','Opmanis','Podnieks','Liepiņš','Liepins','Sproģis','Sprogis','Rikačovs', 'Rikacovs', 'Zviedris','Skadiņš','Vasiļjevs','Vasiljevs','Čerāns','Cerans','Barinskis','Ovcinnikova','Truksans',
					'Angelov','Kaljurand','Davis','Fuchs','Damljanovic','Kuhn','Borin','Gornostay','Hoefler','Smedt','Pedersen','Wyner','Jones','Bielinskiene','Kovalevskaite','Rimkute','Utka','Heidens','Merzlyakov','Losnegaard','Olsen',"Lind\\'en",'de Smedt']
	if surname in neatrodamie:
		return

	print( 'Nevarēju atrast %s' % (name,) )

def createProject(project):
	p = Project(title=project['title'], parent_id = research_id, in_menus = False)
	p.startyear = project['start']
	p.endyear = project['end']
	p.funder = project['funder']
	if project.get('program'):
		p.program = project['program']
	if project.get('funding'):
		p.funding = project['funding']
	if project.get('url'):
		p.url = project['url']
	p.people_list = project['people']
	p.save()
	for name in p.people_list.split(';'):
		person = findPerson(name.strip())
		if person:
			person.projects.add(p)
	p.save()

with open ('initialdata/people.json', 'r') as f:
	people = json.load(f)
	people.sort(key=lambda x:x['name'])
	for p in people:
		createPerson(p)

with open ('initialdata/projects.json', 'r') as f:
	projects = json.load(f)
	for p in projects:
		createProject(p)

with open ('initialdata/pubs.json', 'r') as f:
	Publication.objects.all().delete()
	pubs = json.load(f)
	for pub in pubs:
		bibtex = pub.get('bibtex')
		if '@' in bibtex:			
			bib = parse(bibtex)
			response = import_bibtex_data(bib)
			if response['errors']:
				print(response)
				print(bibtex)
				pass
	
			if len(response['publications']) != 1:
				print(response)
				print('Gribēju atbildē vienu publikācijas objektu..')
			publication = response['publications'][0]

			for author in publication.authors_list:
				person = findPerson(author.strip())
				if person:
					person.publications.add(publication)
			if pub['authors']:
				for author in pub['authors'].split(','):
					person = findPerson(author.strip())
					if person and person not in publication.person_set.all():
						print('Autori: no %s neatradām %s\n\t %s' % (pub['authors'], author, publication.authors))


			if pub.get('year') and str(pub.get('year')) != publication.year:
				print(bibtex)
				print('Gadi: |%s| vs |%s| %s %s' % (pub.get('year'), publication.year, str(type(pub.get('year'))), str(type(publication.year))))

		else:			
			volume = pub['volume']
			number = None
			if 'Nr. ' in volume:
				volume = volume[4:]
			if 'Vol. ' in volume:
				volume = volume[5:]
			if '(' in volume:
				number = int(volume.split('(')[1][:-1])
				volume = int(volume.split('(')[0])
			if not volume:
				volume = None
			year = pub['year']
			if not year:
				year = None # tukšo string aizstājam ar none
			publication = Publication(
					type_id=2,
					title=bibtex, # excelī tajā vietā bija raksta nosaukums 
					authors=pub.get('authors'),
					year=year,
					journal=pub['journal'],
					publisher=pub['publisher'],
					volume=volume,
					external=False)
			publication.save()

			for author in publication.authors_list:
				person = findPerson(author.strip())
				if person:
					person.publications.add(publication)
			# --- beigas tam, ja jāveido publikācija pašam jo nav bibtex

		if pub['indexed']:
			publication.indexed = pub['indexed']
			publication.save()
		if pub['project_name']:
			for name in pub['project_name'].split(';'):
				for project in Project.objects.all():
					if project.title == name.strip():
						project.publications.add(publication)
						break
				else:
					print('Neatradām projektu %s' % (name,))

			pass
