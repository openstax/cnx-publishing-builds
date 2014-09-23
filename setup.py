# -*- coding: utf-8 -*-
import sys
from setuptools import setup, find_packages


IS_PY3 = sys.version_info > (3,)

install_requires = (
    'pyramid',
    )
tests_require = [
    ]
extras_require = {
    'test': tests_require,
    }
description = """\
Application for building CNX export file formats."""

if not IS_PY3:
    tests_require.append('mock')

setup(
    name='cnx-port',
    version='0.1',
    author='Connexions team',
    author_email='info@cnx.org',
    url="https://github.com/connexions/cnx-port",
    license='AGPL, See also LICENSE.txt',
    description=description,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    test_suite='cnxport.tests',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'cnxport': [],
        },
    entry_points="""\
    [paste.app_factory]
    main = cnxport.main:main
    """,
    )
