#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (C) 2015-2019 Peter Magnusson <peter@kmpm.se>
"""Setup for nodemcu-uploader"""

from setuptools import setup

exec(open('nodemcu_uploader/version.py').read())  # pylint: disable=W0122

setup(name='nodemcu-uploader',
      version=__version__,  # noqa: F821
      install_requires=[
          'pyserial>=3.4'
      ],
      packages=['nodemcu_uploader'],
      # package_dir={'nodemcu_uploader': 'lib'},
      url='https://github.com/kmpm/nodemcu-uploader',
      author='kmpm',
      author_email='peter@birchroad.net',
      description='tool for uploading files to the filesystem of an ESP8266 running NodeMCU.',
      keywords=['esp8266', 'upload', 'nodemcu'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Programming Language :: Python :: 3.5'
      ],
      license='MIT',
      test_suite="tests.get_tests",
      entry_points={
          'console_scripts': [
              'nodemcu-uploader=nodemcu_uploader.main:main_func'
          ]
      },
      zip_safe=False
    )
