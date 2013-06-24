from pymyadmin.modules import BaseModule
from pymyadmin.modules import expose
from flask import g
from flask import url_for
from flask import request
from flask import redirect


class DatabaseModelView(BaseModule):
    """A view for the settings."""

    public = True
    endpoint = 'databases'
    verbose_name = 'Databases'

    @expose('/')
    def list(self):
        Databases = g.table.Databases
        databases = g.rows.query(Databases).all()
        return self.render('databases/list.html', database_list=databases)

    @expose('/add', methods=("GET", "POST"))
    def add(self):
        """Add a new database."""

        if request.method == 'GET':
            return self.render('databases/add.html')

        database = g.table.Databases()
        database.host = request.form['host']
        database.port = request.form['port']
        database.name = request.form['name']
        database.engine = request.form['engine']
        database.username = request.form['username']
        database.password = request.form['password']

        g.rows.insert(database)

        return redirect(url_for('list'))

    @expose('/remove/<int:_id>/', methods=("GET", "POST"))
    def remove(self, _id):
        return ''

    @expose('/edit/<int:_id>/', methods=("GET", "POST"))
    def edit(self, _id):
        return ''

    @expose('/connect/<int:_id>/', methods=("GET", "POST"))
    def connect(self, _id):
        return ''
