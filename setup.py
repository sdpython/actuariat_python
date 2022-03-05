# -*- coding: utf-8 -*-
import sys
import os
from setuptools import find_packages, setup
from pyquicksetup import read_version, read_readme, default_cmdclass

#########
# settings
#########

project_var_name = "actuariat_python"
versionPython = "%s.%s" % (sys.version_info.major, sys.version_info.minor)
path = "Lib/site-packages/" + project_var_name
readme = 'README.rst'
history = "HISTORY.rst"
requirements = None
KEYWORDS = [project_var_name, 'teachings', 'Xavier Dupré', 'actuariat']
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


setup(
    name=project_var_name,
    version=read_version(__file__, project_var_name, subfolder='src'),
    author='Xavier Dupré',
    author_email='xavier.dupre@gmail.com',
    license="MIT",
    url="http://www.xavierdupre.fr/app/actuariat_python/helpsphinx/index.html",
    download_url="https://github.com/sdpython/actuariat_python/",
    description=DESCRIPTION,
    long_description=read_readme(__file__),
    cmdclass=default_cmdclass(),
    keywords=KEYWORDS,
    classifiers=CLASSIFIERS,
    packages=packages,
    package_dir=package_dir,
    package_data=package_data,
    setup_requires=["pyquicksetup"],
    install_requires=[
        "pyquickhelper>=1.10", "pyensae", "pymyinstall", "mlstatpy",
        "scikit-learn", "pyrsslocal", "pandas", "numpy",
        "matplotlib", "jupyter"],
)
