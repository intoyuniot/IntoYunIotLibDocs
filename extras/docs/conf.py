import sys
import os
import shlex
import subprocess

# on_rtd is whether we are on readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

if on_rtd:
    subprocess.call('doxygen', shell=True)

extensions = ['breathe']
breathe_projects = { 'IntoYunIotLibDocs': 'xml' }
breathe_default_project = "IntoYunIotLibDocs"
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'IntoYunIotLibDocs'
copyright = u'2013-Present, MOLMC'
author = u'IntoYunIotLibDocs'
version = '1.0'
release = '1.0'
language = 'zh_CN'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
todo_include_todos = False
html_static_path = ['_static']
htmlhelp_basename = 'IntoYunIotLibDocsdoc'
latex_elements = {
}
latex_documents = [
  (master_doc, 'IntoYunIotLibDocs.tex', u'IntoYunIotLibDocs Documentation',
   u'IntoYunIotLibDocs', 'manual'),
]
