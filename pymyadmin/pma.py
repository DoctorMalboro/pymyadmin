# -*- coding: utf-8 *-*

from flask import Flask
from pymyadmin.admin import setup_admin_for
from flask import redirect


app = Flask(__name__)
setup_admin_for(app)

# Redirects the site straight to the administration panel

@app.route('/')
def index():
    return redirect('/admin/')

app.run(debug=True)
