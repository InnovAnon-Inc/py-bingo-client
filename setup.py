#!/usr/bin/env python

import os
from distutils.core import setup
import subprocess

# convert readme to rst format
try:
   import pypandoc
   long_description = pypandoc.convert('README.md', 'rst')
except:
   long_description = ''

versionfile = "client/version.py"
if not os.path.isfile(versionfile):
    # assume git checkout
    __version__ = str(subprocess.check_output(["git", "describe", "--tag", "--always"])).strip("\n")
else:
    # created by pip
    exec(open(versionfile).read())

setup(
    version=__version__,
    name='py-bingo-client',
    description='Multiplayer networking Bingo',
    long_description=long_description,
    author='InnovAnon, Inc.',
    author_email='InnovAnon-Inc@protonmail.com',
    url='https://github.com/InnovAnon-Inc/py-bingo-client',
    packages=['client', 'client/scene'],
)
