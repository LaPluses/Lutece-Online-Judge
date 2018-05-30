from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse

from jinja2 import Environment,evalcontextfilter, Markup, escape
from django_gravatar.helpers import get_gravatar_url
import re


_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')
 
@evalcontextfilter
def nl2br(eval_ctx, value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', Markup('<br>\n'))
                          for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result

def register_judge_result( env ):
    from submission.judge_result import get_judge_result_color, get_judge_result_icon , check_judge_result_in_listshow_field, is_compile_error, is_judger_error, get_CE_JE_info
    env.filters['get_judge_result_color'] = get_judge_result_color
    env.filters['get_judge_result_icon'] = get_judge_result_icon
    env.filters['check_judge_result_in_listshow_field'] = check_judge_result_in_listshow_field
    env.filters['is_compile_error'] = is_compile_error
    env.filters['is_judger_error'] = is_judger_error
    env.filters['get_CE_JE_info'] = get_CE_JE_info

def register_language( env ):
    from utils.language import get_prism
    env.filters['get_prism'] = get_prism

def append_query_parameters( url , query ):
    return url + '?' + query if len( query ) else url

def environment(**options):
    env = Environment(**options)
    env.filters['nl2br'] = nl2br
    register_judge_result( env )
    register_language( env )
    env.filters['append_query_parameters'] = append_query_parameters
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'gravatar_url': get_gravatar_url,
    })
    return env