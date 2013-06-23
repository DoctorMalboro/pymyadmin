# -*- coding: utf-8 *-*

from flask import Flask
from pymyadmin.admin import setup_admin_for
from database import db_session
from flask import redirect

app = Flask(__name__)
app.config.update(
    SECRET_KEY='G#39uUX4Wn*ejOWCtw5$'
)
setup_admin_for(app)
app.run(debug=True)

# Redirects the site straight to the administration panel
@app.route('/')
def index():
    return redirect('/admin/')


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
