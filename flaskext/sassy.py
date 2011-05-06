from os import path

from pyscss.scss import Scss


class Sassy(object):

    def init_app(self, app):
        self.compiler = Scss()
        self.app = app
        self.directory = path.join(app.root_path, 'stylesheets')
        app.add_url_rule('/stylesheets/<path:name>.css',
                         view_func=self.stylesheet)

    def compile(self, filename):
        with self.app.open_resource(path.join(self.directory, filename)) as f:
            scss = f.read()
        return self.compiler.compile(scss)

    def stylesheet(self, name):
        return self.app.response_class(self.compile(name + '.scss'),
                                       mimetype='text/css')
