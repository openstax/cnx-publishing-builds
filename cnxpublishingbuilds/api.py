# -*- coding: utf-8 -*-
# ###
# Copyright (c) 2014, Rice University
# This software is subject to the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
# ###
from cnxtransforms.main import app as celery_app
from cnxtransforms.tasks import (
    make_styled_epub, make_pdf, make_zip,
    )
from pyramid import httpexceptions
from pyramid.view import view_config


@view_config(route_name='create_epub', request_method='POST', renderer='json')
def create_epub(request):
    """Accepts an EPUB and callback. Responds with a build URL."""
    if 'file' not in request.POST:
        raise httpexceptions.HTTPBadRequest("Missing file in POST body.")

    callback_url = request.POST.get('callback-url', None)
    file = request.POST['file'].file

    if callback_url is not None:
        raise NotImplementedError("TODO")

    result = make_epub.delay(file)

    url = request.route_url('builds', id=result.id)
    request.response.status = '202 Accepted'
    return {'url': url, 'id': result.id}


@view_config(route_name='create_pdf', request_method='POST', renderer='json')
def create_pdf(request):
    """Accepts an EPUB and callback. Responds with a build URL."""
    if 'file' not in request.POST:
        raise httpexceptions.HTTPBadRequest("Missing file in POST body.")

    callback_url = request.POST.get('callback-url', None)
    file = request.POST['file'].file

    if callback_url is not None:
        raise NotImplementedError("TODO")

    result = make_pdf.delay(file)

    url = request.route_url('builds', id=result.id)
    request.response.status = '202 Accepted'
    return {'url': url, 'id': result.id}


@view_config(route_name='create_zip', request_method='POST', renderer='json')
def create_zip(request):
    """Accepts an EPUB and callback. Responds with a build URL."""
    if 'file' not in request.POST:
        raise httpexceptions.HTTPBadRequest("Missing file in POST body.")

    callback_url = request.POST.get('callback-url', None)
    file = request.POST['file'].file

    if callback_url is not None:
        raise NotImplementedError("TODO")

    result = make_zip.delay(file)

    url = request.route_url('builds', id=result.id)
    request.response.status = '202 Accepted'
    return {'url': url, 'id': result.id}


@view_config(route_name='builds', request_method='GET', renderer='json')
def get_build(request):
    """Retrieve information about the build. This includes the state of the
    build and the resulting artifacts list.
    """
    task_id = request.matchdict['id']
    result = celery_app.AsyncResult(task_id)

    is_ready = result.ready()
    is_success = result.successful()
    info = {
        'is_finished': is_ready,
        'state': result.state,
        }
    if is_ready and is_success:
        # TODO This needs to be changed. The results will be absolute paths
        #      as they appear on the filesystem. Change to a set of JSON
        #      bits that contain the filename and a full URL to download the
        #      artifact (i.e. /builds/{id}/artifacts/{idx}/{filename})
        info['artifacts'] = result.result

    return info
