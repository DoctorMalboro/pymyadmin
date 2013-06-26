# -*- coding: utf-8 *-*

from flask import Flask
from flask import g
from pymyadmin.admin import setup_admin_for
from pymyadmin.databases import db


db.create()
app = Flask(__name__)
setup_admin_for(app)


@app.before_request
def before_request():
    g.table = db.table
    g.rows = db.rows


app.run(debug=True)
