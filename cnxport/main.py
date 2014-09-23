# -*- coding: utf-8 -*-
# ###
# Copyright (c) 2014, Rice University
# This software is subject to the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
# ###
from pyramid.config import Configurator


__version__ = '0.1'
__name__ = 'cnxport'


def declare_routes(config):
    """Declaration of routes"""
    pass


def main(global_config, **settings):
    """Application factory"""
    config = Configurator(settings=settings)
    declare_routes(config)

    config.scan(ignore='cnxport.tests')
    return config.make_wsgi_app()
