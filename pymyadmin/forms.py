from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, SelectField


ENGINES = (
    ('mysql', 'MySQL'),
    ('postgresql', 'PostgreSQL'),
    ('sqlite', 'SQLite'),
    ('oracle', 'Oracle')
)


class DatabaseForm(Form):
    engine = SelectField('Engine', choices=ENGINES)
    name = TextField('Name')
    user = TextField('User')
    host = TextField('Host')
    password = PasswordField('Password')
    db_name = TextField('DB name')
