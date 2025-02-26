# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SmartGridready Documentation'
copyright = '2025, SmartGridready'
author = 'Hans Furrer'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

'''
html_theme = "sphinx_book_theme"
html_theme_options = {
    "collapse_navigation": False,  # Prevents collapsing
    "navigation_depth": 3,  # Keeps submenus expanded
}
'''


html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    "collapse_navigation": False,  # Prevents collapsing
    "navigation_depth": 4,         # Ensures deeper levels stay open
}

# Override CSS to have text wrapping in tables
html_static_path = ['_static']
html_css_files = ['custom.css']


# -- Options for EPUB output
epub_show_urls = 'footnote'

numfig = True