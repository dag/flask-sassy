Flask-Sassy
===========

::

    sassy = Sassy(app)
    url_for('stylesheet', name='main')  #=> /stylesheets/main.css

Sassy stylesheets are located in ``stylesheets/`` next to the similar
``static/`` and ``templates/`` directories. They are exposed over HTTP from
a path with the same name, mounted at the application script root and
compiled on-demand when requested with a ``.css`` extension.

For production deployments the stylesheets can be precompiled and served as
static files with the webserver. To make this easy, a method is provided::

    sassy.compile_all('/var/www/myapp/stylesheets')

.. note::

    The argument is an output directory and not necessarily the same directory
    as the one containing the Sassy stylesheets. More likely, your
    application is installed as a Python package and you have a deployment
    directory containing a production config, maybe a ``.wsgi`` file if
    you're using mod_wsgi, maybe a directory for file uploads. This is most
    likely where you want to put this output stylesheets directory and
    serve it up using the ``Alias`` directive in the case of Apache.

You could add a Flask-Script command for it and make it part of your
deployment procedure with Fabric, for example. Precompiled stylesheets are
"minified" to use less bandwidth unlike the on-demand compiled stylesheets
which are intended for development and meant to be easier to debug.
