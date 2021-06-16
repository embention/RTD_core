from os import path

from docutils import nodes
from sphinx.environment.collectors import EnvironmentCollector
from sphinx import addnodes
from sphinx.util.osutil import relative_uri

__version__ = (0, 7, 3)


def setup(app):
    app.add_html_theme('press', path.abspath(path.dirname(__file__)))
