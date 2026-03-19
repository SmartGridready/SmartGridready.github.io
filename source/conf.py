# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SmartGridready Documentation'
copyright = '2026, SmartGridready'
author = 'Hans Furrer, Kevin Arm, Matthias Krebs'

release = '0.2'
version = '0.2.0'

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

# -- Options for HTML output
html_scaled_image_link = False

numfig = True

# sources that are not published yet
exclude_patterns = ['content/communicator-description-file.rst']

# Icons for target audiences
rst_epilog = """
.. |planner| image:: /_static/icons/planner.png
   :height: 1cm
   
.. |supplier| image:: /_static/icons/supplier.png
   :height: 1cm

.. |grid| image:: /_static/icons/grid.png
   :height: 1cm

.. |dev| image:: /_static/icons/developer.png
   :height: 1cm
"""
