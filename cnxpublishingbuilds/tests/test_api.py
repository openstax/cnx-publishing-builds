# -*- coding: utf-8 -*-
# ###
# Copyright (c) 2014, Rice University
# This software is subject to the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
# ###
import os
import io
import unittest
from pyramid import testing
from pyramid.request import Request

try:
    from unittest import mock
except ImportError:
    import mock


here = os.path.abspath(os.path.dirname(__file__))


class APITestCase(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        from ..main import declare_routes
        declare_routes(self.config)

    def tearDown(self):
        testing.tearDown()

    def test_create_pdf(self):
        build_id = 'dummy-id'
        file = io.BytesIO(b'abc123')
        post_params = {'file': ('book.epub', file,)}
        request = Request.blank('/builds/pdf', POST=post_params)
        # This would normally happen somewhere in routing.
        setattr(request, 'registry', self.config.registry)

        from cnxtransforms.main import app
        from cnxtransforms.tasks import make_pdf
        patcher = mock.patch.object(
            make_pdf, 'delay',
            return_value=app.AsyncResult(build_id))

        from ..api import create_pdf
        with patcher as patchy:
            resp = create_pdf(request)
            self.assertTrue(patchy.called)

        expected = {
            'url': request.route_url('builds', id=build_id),
            'id': build_id,
            }
        self.assertEqual(resp, expected)

    def test_create_epub(self):
        build_id = 'dummy-id'
        file = io.BytesIO(b'abc123')
        post_params = {'file': ('book.epub', file,)}
        request = Request.blank('/builds/epub', POST=post_params)
        # This would normally happen somewhere in routing.
        setattr(request, 'registry', self.config.registry)

        from cnxtransforms.main import app
        from cnxtransforms.tasks import make_epub
        patcher = mock.patch.object(
            make_epub, 'delay',
            return_value=app.AsyncResult(build_id))

        from ..api import create_epub
        with patcher as patchy:
            resp = create_epub(request)
            self.assertTrue(patchy.called)

        expected = {
            'url': request.route_url('builds', id=build_id),
            'id': build_id,
            }
        self.assertEqual(resp, expected)

    def test_create_zip(self):
        build_id = 'dummy-id'
        file = io.BytesIO(b'abc123')
        post_params = {'file': ('book.epub', file,)}
        request = Request.blank('/builds/zip', POST=post_params)
        # This would normally happen somewhere in routing.
        setattr(request, 'registry', self.config.registry)

        from cnxtransforms.main import app
        from cnxtransforms.tasks import make_zip
        patcher = mock.patch.object(
            make_zip, 'delay',
            return_value=app.AsyncResult(build_id))

        from ..api import create_zip
        with patcher as patchy:
            resp = create_zip(request)
            self.assertTrue(patchy.called)

        expected = {
            'url': request.route_url('builds', id=build_id),
            'id': build_id,
            }
        self.assertEqual(resp, expected)
