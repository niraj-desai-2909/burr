# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import subprocess

project = "Burr"
copyright = "2025, Apache Software Foundation"
author = "Apache Burr PMC"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "myst_nb",
    "sphinx_sitemap",
    "sphinx_toolbox.collapse",
]

if os.getenv("GITHUB_ACTIONS"):  # only add googleanalytics if building on GitHub Actions
    extensions.append("sphinxcontrib.googleanalytics")
    googleanalytics_id = "G-20Z3J1CR22"

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_static_path = ["_static"]
html_favicon = "_static/favicon.ico"

html_css_files = [
    "custom.css",
    "testimonials.css",
]

html_title = "Burr"
html_theme_options = {
    "source_repository": "https://github.com/apache/burr",
    "source_branch": "main",
    "source_directory": "docs/",
    "light_css_variables": {
        "color-announcement-background": "#ffba00",
        "color-announcement-text": "#091E42",
    },
    "dark_css_variables": {
        "color-announcement-background": "#ffba00",
        "color-announcement-text": "#091E42",
    },
}

nb_execution_mode = "off"

exclude_patterns = ["README-internal.md"]

autodoc_typehints_format = "short"
python_maximum_signature_line_length = 100
python_use_unqualified_type_names = True

# -- for sitemap extension
GIT_BRANCH_OUTPUT = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
current_branch = GIT_BRANCH_OUTPUT.decode().strip()
if current_branch == "main":
    html_baseurl = "https://burr.apache.org/"
else:
    html_baseurl = "https://burr.staged.apache.org/"
html_extra_path = ["robots.txt"]
sitemap_locales = [None]
sitemap_url_scheme = "{link}"
