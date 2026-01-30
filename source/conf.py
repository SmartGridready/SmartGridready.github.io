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
    'sphinx.ext.intersphinx',
    'sphinx_copybutton'
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

html_logo = "_static/SGr-Logo.svg"

# Override CSS to have text wrapping in tables
html_show_sourcelink = False
html_static_path = ['_static']
html_css_files = ['custom.css']

# JS to open new tab for external links
html_js_files = ['custom.js']


# -- Options for EPUB output
epub_show_urls = 'footnote'

numfig = True

# sources that are not published yet
exclude_patterns = ['content/communicator-description-file.rst']

# icons for target audiences
rst_epilog = """
.. |planner| unicode:: U+1F3E2
.. |supplier| unicode:: U+1F4DF
.. |grid|    unicode:: U+1F5FC
.. |dev|     unicode:: U+1F6E0
"""
