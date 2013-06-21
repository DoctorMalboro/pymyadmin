# -*- coding: utf-8 *-*

from flask import Flask
from pymyadmin.admin import setup_admin_for


app = Flask(__name__)
setup_admin_for(app)

app.config.update(
    SECRET_KEY='G#39uUX4Wn*ejOWCtw5$'
)
app.run(debug=True)
