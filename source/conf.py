# Configuration file for the Sphinx documentation builder.

project = '半导体刻蚀技术'
copyright = '2026'
author = 'Semiconductor Etching Knowledge Base'
release = '1.0'

extensions = [
    'sphinxcontrib.mermaid',
    'sphinx.ext.mathjax',
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

html_theme = 'furo'
html_static_path = ['_static']
html_title = '半导体刻蚀技术知识库'
html_theme_options = {
    'navigation_with_keys': True,
    'sidebar_hide_name': False,
}

latex_engine = 'xelatex'
latex_elements = {
    'preamble': r'''
\usepackage{fontspec}
\setmainfont{Noto Sans CJK SC}
''',
}

todo_include_todos = True
