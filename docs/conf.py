# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os, sys
sys.path.insert(0, os.path.abspath('../'))


# -- Project information -----------------------------------------------------

project = 'torchvtk'
copyright = '2020, Dominik Engel, Marc Fabian Mezger'
author = 'Dominik Engel, Marc Fabian Mezger'

# The full version, including alpha/beta/rc tags
release = 'v0.2.5'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

napoleon_include_init_with_doc = True
autodoc_mock_imports = ['torch', 'torchvision', 'numpy', 'matplotlib', 'tqdm',
    'pydicom', 'dicom_numpy', 'torchinterp1d', 'torchsearchsorted', 'psutil']

from recommonmark.transform import AutoStructify
github_root_doc = 'https://github.com/xeTaiz/torchvtk/tree/master/docs/'
def setup(app):
    app.add_config_value('recommonmark_config', {
        'auto_toc_tree_section': 'Contents'
    }, True)
    app.add_transform(AutoStructify)