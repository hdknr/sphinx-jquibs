"""
"""
#: Metadata

NAME = "sphinx-jquibs"
MOD_NAME = "sphinx_jquibs"
AUTHOR = "Hidek Nara"
NICKNAME= "hdknr"
EMAIL = "gmail[at]hdknr.com"
DESCRIPTION = "Sphinx Theme with jQuery UI Bootstrap"
CLASSIFIERS=[
        "Development Status :: 5 - Production/Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation",
    ]

#: Configure
import os
from sphinx_jquibs import get_version
from setuptools import setup, find_packages

_F = lambda fname : open(os.path.join(os.path.dirname(__file__), fname)).read()
_I = lambda fname : [ r for r in open(fname).read().split('\n') if len(r)>0] 

os.environ['COPYFILE_DISABLE'] = "true"

PKGS = [x for x in find_packages() if x.split('.')[0] == MOD_NAME]
SCRIPTS=glob.glob('scripts/*.py') if os.path.isdir('scripts') else []
INSTALL_REQUIRES= _I('requirements.txt') if os.path.isfile('requirements.txt') else []

#: Setup

setup(
    name = NAME,
    version= get_version(),
    description= DESCRIPTION,
    long_description= _F("README.rst"),
    url="https://github.com/%s/%s/" % ( NICKNAME,NAME ),
    author= AUTHOR,
    author_email= EMAIL,
    classifiers=CLASSIFIERS,
    packages=PKGS,
    scripts=SCRIPTS,
    install_requires = INSTALL_REQUIRES,
    include_package_data=True,
    use_2to3=True,
)
