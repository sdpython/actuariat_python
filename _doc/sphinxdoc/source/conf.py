import sys
import os
import datetime
import re
import sphinxjp.themes.basicstrap

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

from pyquickhelper.helpgen.default_conf import set_sphinx_variables

set_sphinx_variables(__file__,
                     "actuariat_python",
                     "Xavier Dupré, Vincent Bernardi",
                     2015,
                     "basicstrap",
                     None,
                     locals(),
                     add_extensions=None)

language = "fr"

blog_root = "http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/"
blog_background = False