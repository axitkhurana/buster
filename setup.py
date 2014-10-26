#!/usr/bin/env python

import os
from setuptools import setup
from buster import _version


setup(name="buster",
      version=_version.__version__,
      description="Static site generator for Ghost and Github",
      long_description=open("README.rst").read(),
      author="Akshit Khurana",
      author_email="axitkhurana@gmail.com",
      url="https://github.com/axitkhurana/buster",
      license="MIT",
      packages=["buster"],
      entry_points={"console_scripts": ["buster = buster.buster:main"]},
      install_requires=['GitPython==0.3.2.RC1', 'async==0.6.1', 'docopt==0.6.1', 'gitdb==0.5.4', 'pyquery==1.2.8', 'smmap==0.8.2']
    )
