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
    config.add_route('create_epub', '/builds/epub')
    config.add_route('create_pdf', '/builds/pdf')
    config.add_route('create_zip', '/builds/zip')
    config.add_route('builds', '/builds/{id}')


def init_celery(config):
    """Initialize Celery for usage by this application."""
    settings_prefix = 'cnxtransforms.celery.'
    from cnxtransforms import main
    celery_settings = {k[len(settings_prefix):]: v
                       for k, v in config.settings
                       if k.startswith(settings_prefix)}
    main.app.conf.update(**celery_settings)


def main(global_config, **settings):
    """Application factory"""
    config = Configurator(settings=settings)
    init_celery(config)
    declare_routes(config)

    config.scan(ignore='cnxport.tests')
    return config.make_wsgi_app()
