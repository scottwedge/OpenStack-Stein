# Copyright (c) 2010 OpenStack Foundation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
# Neutron documentation build configuration file, created by
# sphinx-quickstart on Tue May 18 13:50:15 2010.
#
# This file is execfile()d with the current directory set to it's containing
# dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import logging
import os
import sys

import eventlet

# module ref generation can cause partial greening resulting in thread issues
# during the linkcheck builder, so initialize eventlet upfront
eventlet.monkey_patch()

# NOTE(amotoki): In case of oslo_config.sphinxext is enabled,
# when resolving automodule neutron.tests.functional.db.test_migrations,
# sphinx accesses tests/functional/__init__.py is processed,
# eventlet.monkey_patch() is called and monkey_patch() tries to access
# pyroute2.common.__class__ attribute. It raises pyroute2 warning and
# it causes sphinx build failure due to warning-is-error = 1.
# To pass sphinx build, ignore pyroute2 warning explicitly.
logging.getLogger('pyroute2').setLevel(logging.ERROR)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NEUTRON_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", ".."))
sys.path.insert(0, NEUTRON_DIR)
sys.path.append(os.path.abspath("ext"))

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.graphviz',
    'sphinx.ext.todo',
    'openstackdocstheme',
    'support_matrix',
    'oslo_config.sphinxext',
    'oslo_config.sphinxconfiggen',
    'oslo_policy.sphinxext',
    'oslo_policy.sphinxpolicygen',
]

# Project cross-reference roles
openstack_projects = [
    'neutron',
    'nova',
]

# openstackdocstheme options
repository_name = 'openstack/neutron'
bug_project = 'neutron'
bug_tag = 'doc'

todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = []

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Neutron'
copyright = u'2011-present, OpenStack Foundation.'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# Version info
from neutron.version import version_info as neutron_version
release = neutron_version.release_string()
# The short X.Y version.
version = neutron_version.version_string()

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
# unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['neutron.']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
# html_theme_path = ["."]
# html_theme = '_theme'
html_theme = 'openstackdocs'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = ['_theme']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%Y-%m-%d %H:%M'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'neutrondoc'


# -- Options for LaTeX output ------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author,
# documentclass [howto/manual]).
latex_documents = [
    ('index', 'Neutron.tex', u'Neutron Documentation',
     u'Neutron development team', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True

# -- Options for oslo_config.sphinxconfiggen ---------------------------------

_config_generator_config_files = [
    'dhcp_agent.ini',
    'l3_agent.ini',
    'linuxbridge_agent.ini',
    'macvtap_agent.ini',
    'metadata_agent.ini',
    'metering_agent.ini',
    'ml2_conf.ini',
    'neutron.conf',
    'openvswitch_agent.ini',
    'sriov_agent.ini',
]


def _get_config_generator_config_definition(conf):
    config_file_path = '../../etc/oslo-config-generator/%s' % conf
    # oslo_config.sphinxconfiggen appends '.conf.sample' to the filename,
    # strip file extentension (.conf or .ini).
    output_file_path = '_static/config-samples/%s' % conf.rsplit('.', 1)[0]
    return (config_file_path, output_file_path)


config_generator_config_file = [
    _get_config_generator_config_definition(conf)
    for conf in _config_generator_config_files
]

# -- Options for oslo_policy.sphinxpolicygen ---------------------------------

policy_generator_config_file = '../../etc/oslo-policy-generator/policy.conf'
sample_policy_basename = '_static/neutron'

linkcheck_anchors_ignore = [
    # skip gerrit anchors
    r'\/q\/.*',
    r'q\,.*',
    r'\/c\/.*'
]
