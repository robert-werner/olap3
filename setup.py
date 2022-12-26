# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='olap',
      version='0.4',
      description='Interface to OLAP DBs',
      author='Leonid Kolesnichenko (original author: Norman Krämer)',
      author_email='xperience439@gmail.com',
      packages=find_packages(),
      namespace_packages=['olap'],
      package_dir={'olap': 'olap'},
      install_requires=required,
      url="https://github.com/robert-werner/olap",
      license='Apache Software License 2.0',
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Development Status :: 3 - Alpha",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Libraries :: Python Modules"
      ]
      )
