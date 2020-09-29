from urllib.parse import urljoin
from os.path import join as pathjoin

from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

from furnace.services.fixtures_locator_service import FixtureLocatorService
from furnace.globals import ioc
from furnace.globals.const import const


fls = ioc.provide(FixtureLocatorService)
const.fixture_entries = "fixture_entries"
const.site_map_template = "site_map.tpl.html"


def site_map(request):
    fixture_entries = fls.get_fixtures_entries()
    return render(request, const.site_map_template, {const.fixture_entries: fixture_entries})


def to_fixture(request, *args):
    page = args[-1].lower()
    if page.endswith(const.ext_html_template):
        return _redirect_to_template(request, *args)
    elif page.endswith(const.ext_html):
        return _redirect_to_html(request, *args)
    else:
        raise Http404("The request url is not exist %s" % "/" % args)


def to_fixture_folder(request, *args):
    return render(request, pathjoin(*args, const.index_page))


def _redirect_to_html(request, *args):
    return render(request, pathjoin(*args))


def _redirect_to_template(request, *args):
    fixture_entries = fls.get_fixtures_entries()
    return render(request, "/".join(args), {const.fixture_entries: fixture_entries})
