from os import path

from pyscss import scss


class Sassy(object):

    def init_app(self, app):
        self.compiler = scss.Scss()
        self.compiler.scss_opts.update(compress=False)
        self.app = app
        self.directory = path.join(app.root_path, 'stylesheets')
        app.add_url_rule('/stylesheets/<path:name>.css',
                         view_func=self.stylesheet)

    def compile(self, filename):
        with self.app.open_resource(path.join(self.directory, filename)) as f:
            contents = f.read()
        _old = scss.LOAD_PATHS
        scss.LOAD_PATHS = ','.join([self.directory, scss.LOAD_PATHS])
        try:
            compiled = self.compiler.compile(contents)
        finally:
            scss.LOAD_PATHS = _old
        return compiled

    def stylesheet(self, name):
        return self.app.response_class(self.compile(name + '.scss'),
                                       mimetype='text/css')
