# -*- coding: utf-8 -*-
import sys
import os
from pyquickhelper.helpgen.default_conf import set_sphinx_variables
import actuariat_python
import pydata_sphinx_theme

sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))

set_sphinx_variables(__file__, "Python pour un Actuaire", "Xavier Dupré",
                     2022, "pydata_sphinx_theme", pydata_sphinx_theme.get_html_theme_path(),
                     locals(), add_extensions=None, book=True, nblayout='table',
                     extlinks=dict(
                         issue=('https://github.com/sdpython/actuariat_python/issues/%s', 'issue')),
                     doc_version=actuariat_python.__version__)

html_logo = "phdoc_static/project_ico_small.png"
language = "fr"
html_split_index = True

blog_root = "http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/"
blog_background = False
html_css_files = ['my-styles.css']
epkg_dictionary['machine learning'] = 'https://fr.wikipedia.org/wiki/Apprentissage_automatique'
