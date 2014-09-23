.. Note that the reStructuredText (rst) 'note' directive is not used,
   because github does not style these in a way that makes them obvious.
   If this document is ever put into a sphinx scroll,
   therefore outside of the github readme,
   the adjustment should be made to make notes use the rst 'note' directive.

==================================
Connexions Transformation Services
==================================

This project is an interface for building and monitoring CNX export formats.
For example, building a PDF for a newly published book. This service transforms
the content from its original format into other formats and allows
the submitting to monitor and retrieve the build results.

Getting started
---------------

Install using one of the following methods (run within the project root)::

    python setup.py install

Or::

    pip install .

Testing
-------

.. image:: https://travis-ci.org/Connexions/cnx-port.svg
   :target: https://travis-ci.org/Connexions/cnx-port

::

    python setup.py test

HTTP API
--------

Build creation routes
~~~~~~~~~~~~~~~~~~~~~

All build routes accept a POSTed EPUB ``file``. The EPUB file must be compatible
with the output of ``cnxepub.EPUB.to_file``. This is the internal CNX EPUB
format.

Optionally, a ``callback-url`` can be given. After the build task has run,
the callback-URL will be pinged as a GET request, which will also contain
query string information about the final state of the build task.

:/builds/pdf: Creates a PDF for the given content.

:/builds/epub: Creates a human readible EPUB3 with embedded EPUB2 capability

:/builds/zip: Creates a ZIP archive of all the content. This is mostly for
    internal use. At this time it includes the content in both CNXML and HTML
    as well as any resource files. In the legacy system, this was known as
    a *complete* or *offline* zip file.

All accepted builds will respond with a URL where the build can be monitored.

Build status monitoring
~~~~~~~~~~~~~~~~~~~~~~~

The builds can be monitored using the build identifier. After a build has
successfully been created the response will contain a build URL, which
contains the build identifier.

:/builds/{id}: Responds with information about the build using the given
    build ``id``.

License
-------

This software is subject to the provisions of the GNU Affero General
Public License Version 3.0 (AGPL). See license.txt for details.
Copyright (c) 2013 Rice University
