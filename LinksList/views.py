# Create your views here.
import operator
from functools import reduce

from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from LinksList.models import Section, Site


def index(request, section_name=None):
    sections = Section.objects.all()
    if len(sections) == 0:
        return HttpResponseRedirect('/admin')
    if section_name:
        section = Section.objects.get(name=section_name)
        sites = Site.objects.filter(section=section).order_by('-hits')
    else:
        return HttpResponseRedirect(f'/sites/{sections[0].name}')

    return render(request, 'index.html', {'sections': sections, 'sites': sites, 'active_section': section_name})


def open_site(request, site_id):
    site = get_object_or_404(Site, id=site_id)
    site.hits = site.hits + 1
    site.save()

    return HttpResponseRedirect(site.url)


def search(request):
    query = request.GET.get('q', '')
    sections = Section.objects.all()
    if len(sections) == 0:
        return HttpResponseRedirect('/admin')
    if query:
        sites = search_keywords(query.split())
    else:
        return HttpResponseRedirect(f'/sites/{sections[0].name}')

    return render(request, 'index.html', {'sections': sections, 'sites': sites, 'active_section': ''})


def search_keywords(keywords):
    if isinstance(keywords, str):
        keywords = [keywords]

    if not isinstance(keywords, list):
        return None

    name_search = [Q(name__icontains=x) for x in keywords]
    description_search = [Q(description__icontains=x) for x in keywords]

    final_q = reduce(operator.or_,
                     [reduce(operator.or_, name_search), ] + [reduce(operator.or_, description_search), ])

    r_qs = Site.objects.filter(final_q).order_by("-hits")
    return r_qs
