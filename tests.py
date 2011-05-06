from attest import assert_hook

from flask import Flask, url_for, Response
from attest import Tests

from flaskext.attest import request_context, get
from flaskext.sassy import Sassy


TESTING = True


@request_context
def appcontext():
    sassy = Sassy()
    app = Flask(__name__)
    app.config.from_object(__name__)
    sassy.init_app(app)
    yield app

app = Tests(contexts=[appcontext])


@app.test
def url_for_stylesheet():
    assert url_for('stylesheet', filename='main.css') == '/stylesheets/main.css'


@app.test
@get('/stylesheets/main.css')
def compiles_on_get(response):
    compiled = '.selector a{display:block}.selector strong{color:#00f}'
    assert response == Response(compiled, mimetype='text/css')
