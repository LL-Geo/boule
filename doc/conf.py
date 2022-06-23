# Copyright (c) 2019 The Boule Developers.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
#
# This code is part of the Fatiando a Terra project (https://www.fatiando.org)
#
import datetime

import boule

# Project information
# -----------------------------------------------------------------------------
project = "Boule"
copyright = f"{datetime.date.today().year}, The {project} Developers"  # noqa: A001
if len(boule.__version__.split(".")) > 3:
    version = "dev"
else:
    version = boule.__version__

# General configuration
# -----------------------------------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.doctest",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx_design",
    "sphinx_copybutton",
    "jupyter_sphinx",
]

# Configuration to include links to other project docs when referencing
# functions/classes
intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "numpy": ("https://docs.scipy.org/doc/numpy/", None),
    "pygmt": ("https://www.pygmt.org/latest/", None),
    "ensaio": ("https://www.fatiando.org/ensaio/latest/", None),
}

# Autosummary pages will be generated by sphinx-autogen instead of sphinx-build
autosummary_generate = []

# Otherwise, the Return parameter list looks different from the Parameters list
napoleon_use_rtype = False
# Otherwise, the Attributes parameter list looks different from the Parameters
# list
napoleon_use_ivar = True

# Sphinx project configuration
templates_path = ["_templates"]
exclude_patterns = ["_build", "**.ipynb_checkpoints"]
source_suffix = ".rst"
# The encoding of source files
source_encoding = "utf-8"
master_doc = "index"
pygments_style = "default"
add_function_parentheses = False

# HTML output configuration
# -----------------------------------------------------------------------------
html_title = f'{project} <span class="project-version">{version}</span>'
html_logo = "_static/boule-logo.png"
html_favicon = "_static/favicon.png"
html_last_updated_fmt = "%b %d, %Y"
html_copy_source = True
html_static_path = ["_static"]
# CSS files are relative to the static path
html_css_files = ["custom.css"]
html_extra_path = []
html_show_sourcelink = False
html_show_sphinx = True
html_show_copyright = True

html_theme = "sphinx_book_theme"
html_theme_options = {
    "repository_url": "https://github.com/fatiando/boule",
    "repository_branch": "main",
    "path_to_docs": "doc",
    "launch_buttons": {
        "binderhub_url": "https://mybinder.org",
        "notebook_interface": "jupyterlab",
    },
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
    "home_page_in_toc": False,
}
