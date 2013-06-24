from saw import DB
from saw import sa


db = DB(name='pymyadmin.db', engine='sqlite')


class Databases(db.Model):
    """A database."""

    __tablename__ = 'Databases'

    id = sa.Column(
            u'id',
            sa.Integer,
            primary_key=True)

    host = sa.Column(
            u'host',
            sa.String,
            unique=True)

    port = sa.Column(
            u'port',
            sa.Integer,
            nullable=True)

    name = sa.Column(
            u'name',
            sa.String,
            unique=True)

    engine = sa.Column(
            u'engine',
            sa.String,
            unique=True)

    username = sa.Column(
            u'username',
            sa.String,
            nullable=True)

    password = sa.Column(
            u'password',
            sa.String,
            nullable=True)

