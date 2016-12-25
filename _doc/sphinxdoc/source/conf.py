#-*- coding: utf-8 -*-
import sys
import os
import datetime
import re
#import sphinxjp.themes.basicstrap
import sphinx_bootstrap_theme

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))
sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.split(__file__)[0],
            "..",
            "..",
            "..",
            "..",
            "pyquickhelper",
            "src")))

from pyquickhelper.helpgen.default_conf import set_sphinx_variables, get_default_stylesheet

set_sphinx_variables(__file__, "Python pour un Actuaire", "Xavier Dupré, Vincent Bernardi",
                     2016, "bootstrap", None,
                     locals(), add_extensions=None, book=True,
                     extlinks=dict(issue=('https://github.com/sdpython/actuariat_python/issues/%s', 'issue')))

html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_logo = "project_ico_small.png"
language = "fr"

html_sidebars = {}

if html_theme == "bootstrap":
    html_theme_options = {
        'navbar_title': "home",
        'navbar_site_name': "Site",
        'navbar_links': [
            ("XD", "http://www.xavierdupre.fr", True),
            ("ENSAE",
             "http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/index.html", True),
            ("module", "py-modindex"),
            ("index", "genindex"),
        ],
        'navbar_sidebarrel': False,
        'navbar_pagenav': True,
        'navbar_pagenav_name': "Page",
        'globaltoc_depth': 3,
        'globaltoc_includehidden': "true",
        'navbar_class': "navbar navbar-inverse",
        'navbar_fixed_top': "true",
        'source_link_position': "nav",
        'bootswatch_theme': "lumen",
        # united = weird colors, sandstone=green, simplex=red, paper=trop bleu
        # lumen: OK
        # to try, yeti, flatly, paper, lumen
        'bootstrap_version': "3",
    }

blog_root = "http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/"
blog_background = False
html_context = {
    'css_files': get_default_stylesheet() + ['_static/my-styles.css'],
}
