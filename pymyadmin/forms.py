from flask.ext.wtf import Form
from wtforms import TextField, SelectField

# TODO: Change password te password field
#       Reset password or rewrite modify

ENGINES = (
    ('', '--'),
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
    password = TextField('Password')
    db_name = TextField('DB name')
