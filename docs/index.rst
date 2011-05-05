Flask-Sassy
===========

::

    sassy = Sassy(app)
    url_for('stylesheet', filename='main.css')  #=> /stylesheets/main.css

Sassy stylesheets are located in ``stylesheets/`` next to the similar
``static/`` and ``templates/`` directories. They are exposed over HTTP from
a path with the same name, mounted at the application script root and
compiled on-demand when requested with a ``.css`` extension.

For production deployments the stylesheets can be precompiled and served as
static files with the webserver. To make this easy, a method is provided::

    app.config['SASSY_COMPRESS'] = True

    # Not necessarily the same directory as above;
    # just any directory that we serve with the webserver as /stylesheets
    sassy.compile('/var/www/myapp/stylesheets')

You could add a Flask-Script command for it and make it part of your
deployment procedure with Fabric, for example.
