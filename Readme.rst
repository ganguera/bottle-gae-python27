Bottle on GAE Python 2.7 WSGI Threadsafe
===================================================

This is a simple "Hello World" example on how to run Bottle_ on `Google App Engine`_ using Python 2.7 WSGI Threadsafe.

Bottle ships with a "ready-to-use" GAE adapter_, however, this adapter is specific for Python 2.5 which runs as CGI. If you want to run Bottle on Python 2.7 WSGI Threadsafe, you have to avoid running the server::

    bottle.run(server='gae')

Instead, just instantiate the Bottle class and assign it to the local variable 'app'::

    app = Bottle(catchall=False)

By default, all exceptions other than HTTPResponse or HTTPError will result in a 500 Internal Server Error response, so they won’t crash your WSGI server. You can turn off this behavior to handle exceptions in your middleware by setting ``bottle.app().catchall`` to ``False``.

.. _Bottle: http://bottlepy.org/docs/stable/
.. _`Google App Engine`: https://cloud.google.com/products/
.. _adapter: http://bottlepy.org/docs/stable/deployment.html#google-appengine
