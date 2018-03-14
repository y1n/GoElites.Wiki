# Add any paths that contain custom static files (such as style sheets) here, 
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', 'rtfd-css']

# Logo and version display.
html_logo = 'img/ge_logo_small_outline.png'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

# Add custom .css files
# https://github.com/snide/sphinx_rtd_theme/issues/117#issuecomment-41571653
def setup(app):
   app.add_stylesheet("custom.css")
   app.add_stylesheet("rtfd-css.css")

   