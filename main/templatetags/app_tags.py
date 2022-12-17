import urllib

from django import template
from django.utils import http


register = template.Library()


@register.filter
def get_prop(dict_or_obj, prop_name):
    return dict_or_obj.get(prop_name, None)


@register.simple_tag(takes_context=True)
def replace_url_param(context, **kwargs):
    """ Updates the current path from existing GET parameters. """
    request = context.get('request')

    get = request.GET.copy()
    get.update(kwargs)
    return u'{path}?{params}'.format(
        path=request.path,
        params=urllib.parse.urlencode(get, 'utf-8')
    )


@register.filter
def normalize_lat_lon(coord):
    return str(coord).replace(',', '.')


@register.filter(name='get_param')
def get_param(dictionary, param):
    return dictionary[param]
