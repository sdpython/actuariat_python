#-*- coding: utf-8 -*-
"""
@file
@brief Some automation helpers to test notebooks and check they are still working fine.
"""
import os
from pyquickhelper.loghelper import noLOG
from pyquickhelper.ipythonhelper.notebook_helper import install_python_kernel_for_unittest
from pyquickhelper.ipythonhelper import execute_notebook_list
from pyquickhelper.pycode import is_travis_or_appveyor
import pyensae


def ls_notebooks(subfolder):
    """
    list the notebooks in a particular subfolder

    @param      subfolder   subfolder (related to this module)
    @return                 list of files
    """
    this = os.path.abspath(os.path.dirname(__file__))
    docnote = os.path.join(
        this,
        "..",
        "..",
        "..",
        "_doc",
        "notebooks",
        subfolder)
    notes = [
        os.path.normpath(
            os.path.join(
                docnote,
                _)) for _ in os.listdir(docnote)]

    keepnote = []
    for i, note in enumerate(notes):
        ext = os.path.splitext(note)[-1]
        if ext != ".ipynb":
            continue
        keepnote.append(note)
    return keepnote


def get_additional_paths():
    """
    returns a list of paths to add before running the notebooks,
    paths to pyquickhelper, pyensae, pymmails

    @return             list of paths
    """
    import pyquickhelper
    import pymyinstall
    import pyrsslocal
    import mlstatpy
    import jyquickhelper
    addpath = [os.path.dirname(pyquickhelper.__file__),
               os.path.dirname(pyensae.__file__),
               os.path.dirname(pyrsslocal.__file__),
               os.path.dirname(pymyinstall.__file__),
               os.path.dirname(mlstatpy.__file__),
               os.path.dirname(jyquickhelper.__file__),
               os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."),
               ]
    try:
        import ensae_teaching_cs
        addpath.append(os.path.dirname(ensae_teaching_cs.__file__))
    except ImportError as e:
        pass
    addpath = [os.path.normpath(os.path.join(_, "..")) for _ in addpath]
    return addpath


def clean_function_notebook(code):
    """
    function which clean cells when unittesting notebooks 1A

    @param      code        cell content
    @return                 modified code
    """
    code = code.replace(
        'run_cmd("exemple.xlsx"',
        'skip_run_cmd("exemple.xlsx"')

    skip = ["faire une chose avec la probabilité 0.7",
            "# déclenche une exception",
            "# pour lancer Excel",
            "for k in list_exercice_1 :",
            "return ....",
            "return [ .... ]",
            "def __init__(self, ...) :",
            "if random.random() <= 0.7 :",
            "dictionnaire_depart.items() [0]",
            "iterateur(0,10) [0]",
            "# ...... à remplir",
            'String.Join(",", a.Select(c=>c.ToString()).ToArray())',
            "# elle n'existe pas encore",
            "# boucle sur les 24 heures de la journée",
            "from ggplot import *",
            "geocode = True",
            # ggplot calls method show and it opens window blocking the offline
            # execution
            ]
    rep = [("# ...", "pass # "),
           ("%timeit -n1 -r1 ", ""),
           ("%timeit", "#%timeit"),
           ("show(p)", "#show(p)"),
           ("show(tabs)", "#show(tabs)"),
           ('http://www.gutenberg.org/cache/epub/4647/pg4647.txt',
            'http://www.xavierdupre.fr/enseignement/complements/pg4647.txt'),
           ]
    spl = ["# ......",
           "# elle n'existe pas encore",
           ]

    for s in skip:
        if s in code:
            return ""

    for s in spl:
        if s in code:
            code = code.split(s)[0]

    for s in rep:
        code = code.replace(s[0], s[1])
    return code


def execute_notebooks(folder, notebooks, filter, clean_function=None,
                      fLOG=noLOG, deepfLOG=noLOG, detailed_log=None):
    """
    Executes a list of notebooks.

    @param      folder          folder
    @param      notebooks       list of notebooks
    @param      filter          function which validate the notebooks
    @param      clean_function  cleaning function to apply to the code before running it
    @param      fLOG            logging function
    @param      deepfLOG        logging function used to run the notebook
    @param      detailed_log    log the output while running the notebook (when the notebook execution fails due to timeout
    @return                     dictionary tuple (statistics, { notebook_file: (isSuccess, outout) })

    The signature of function ``filter`` is::

        def filter(i, filename):
            return True or False

    """

    def valid_cell(cell):
        if "%system" in cell:
            return False
        if "df.plot(...)" in cell:
            return False
        if 'df["difference"] = ...' in cell:
            return False
        if 'print(next(it))' in cell:
            return False
        if "est d'indice 8 et non plus 9" in cell:
            return False
        return True

    kernel_name = None if is_travis_or_appveyor() else install_python_kernel_for_unittest(
        "actuariat_python")
    addpaths = get_additional_paths()
    if filter:
        notebooks = [_ for i, _ in enumerate(notebooks) if filter(i, _)]
    if len(notebooks) == 0:
        raise ValueError("Empty list of notebooks.")
    return execute_notebook_list(
        folder, notebooks, fLOG=fLOG, valid=valid_cell, additional_path=addpaths, kernel_name=kernel_name)
