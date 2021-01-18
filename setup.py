# -*- coding: utf-8 -*-
import sys
import os
from distutils.core import setup
from setuptools import find_packages

#########
# settings
#########

project_var_name = "actuariat_python"
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'
history = "HISTORY.rst"
requirements = None
KEYWORDS = project_var_name + ', ENSAE, sqllite, database, teachings'
DESCRIPTION = """Helpers for teaching purposes (includes sqllite helpers)"""
CLASSIFIERS = [
    'Programming Language :: Python :: 3',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Development Status :: 5 - Production/Stable'
]

#######
# data
#######

packages = find_packages('src', exclude='src')
package_dir = {k: "src/" + k.replace(".", "/") for k in packages}
package_data = {
    project_var_name: ["*.xml"],
    project_var_name + ".automation": ["*.r", "*.ico"],
    project_var_name + ".data.data_elections": ["*.xls", "*.zip"],
    project_var_name + ".data.data_population": ["*.xlsx", "*.xls"],
}

############
# functions
############


def ask_help():
    return "--help" in sys.argv or "--help-commands" in sys.argv


def is_local():
    file = os.path.abspath(__file__).replace("\\", "/").lower()
    if "/temp/" in file and "pip-" in file:
        return False
    from pyquickhelper.pycode.setup_helper import available_commands_list
    return available_commands_list(sys.argv)


def verbose():
    print("---------------------------------")
    print("package_dir =", package_dir)
    print("packages    =", packages)
    print("package_data=", package_data)
    print("current     =", os.path.abspath(os.getcwd()))
    print("---------------------------------")

##########
# version
##########


if is_local() and not ask_help():
    def write_version():
        from pyquickhelper.pycode import write_version_for_setup
        return write_version_for_setup(__file__)

    write_version()

    versiontxt = os.path.join(os.path.dirname(__file__), "version.txt")
    if os.path.exists(versiontxt):
        with open(versiontxt, "r") as f:
            lines = f.readlines()
        subversion = "." + lines[0].strip("\r\n ")
        if subversion == ".0":
            raise Exception("Git version is wrong: '{0}'.".format(subversion))
    else:
        raise FileNotFoundError(
            "Unable to find '{0}' argv={1}".format(versiontxt, sys.argv))
else:
    # when the module is installed, no commit number is displayed
    subversion = ""

if "upload" in sys.argv and not subversion and not ask_help():
    # avoid uploading with a wrong subversion number
    raise Exception(
        "Git version is empty, cannot upload, is_local()={0}".format(is_local()))

##############
# common part
##############

if os.path.exists(readme):
    with open(readme, "r", encoding='utf-8-sig') as f:
        long_description = f.read()
else:
    long_description = ""
if os.path.exists(history):
    with open(history, "r", encoding='utf-8-sig') as f:
        long_description += f.read()

if "--verbose" in sys.argv:
    verbose()

if is_local():
    import pyquickhelper
    logging_function = pyquickhelper.get_fLOG()
    logging_function(OutputPrint=True)
    from pyquickhelper.pycode import process_standard_options_for_setup
    r = process_standard_options_for_setup(
        sys.argv, __file__, project_var_name,
        layout=["html"],
        unittest_modules=["pyquickhelper", "ensae_teaching_cs"],
        requirements=["pyquickhelper", "pyensae", "jyquickhelper",
                      "pyrsslocal", "pymyinstall", "mlstatpy", "ensae_teaching_cs"],
        additional_notebook_path=["pyquickhelper", "jyquickhelper",
                                  "pyensae", "pyrsslocal", "pymyinstall", "mlstatpy", "ensae_teaching_cs"],
        additional_local_path=["pyquickhelper", "jyquickhelper",
                               "pyensae", "pyrsslocal", "pymyinstall", "mlstatpy", "ensae_teaching_cs"],
        fLOG=logging_function, github_owner='sdpython',
        covtoken=("c310b252-ef1b-4454-896c-2d2e01670378", "'_UT_39_std' in outfile"))
    if not r and not ({"bdist_msi", "sdist",
                       "bdist_wheel", "publish", "publish_doc", "register",
                       "upload_docs", "bdist_wininst", "build_ext"} & set(sys.argv)):
        raise Exception("unable to interpret command line: " + str(sys.argv))
else:
    r = False

if ask_help():
    from pyquickhelper.pycode import process_standard_options_for_setup_help
    process_standard_options_for_setup_help(sys.argv)

if not r:
    if len(sys.argv) in (1, 2) and sys.argv[-1] in ("--help-commands",):
        from pyquickhelper.pycode import process_standard_options_for_setup_help
        process_standard_options_for_setup_help(sys.argv)
    from pyquickhelper.pycode import clean_readme
    from actuariat_python import __version__ as sversion
    long_description = clean_readme(long_description)
    setup(
        name=project_var_name,
        version=sversion,
        author='Xavier Dupré',
        author_email='xavier.dupre@gmail.com',
        license="MIT",
        url="http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/index.html",
        download_url="https://github.com/sdpython/actuariat_python/",
        description=DESCRIPTION,
        long_description=long_description,
        keywords=KEYWORDS,
        classifiers=CLASSIFIERS,
        packages=packages,
        package_dir=package_dir,
        package_data=package_data,
        setup_requires=["pyquickhelper"],
        install_requires=[
            "pyquickhelper>=1.10", "pyensae", "pymyinstall", "mlstatpy",
            "scikit-learn", "pyrsslocal", "pandas", "numpy",
            "matplotlib", "jupyter"],
    )
