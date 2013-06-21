from pymyadmin.modules import BaseModule
from pymyadmin.modules import expose
from models import Database
from forms import DatabaseForm
from database import db_session
from flask import (
    redirect,
    flash,
    session
)


class DatabaseModelView(BaseModule):
    """A view for the settings."""

    public = True
    endpoint = 'databases'
    verbose_name = 'Databases'

    @expose('/')
    def list(self):
        database_list = Database.query.all()
        return self.render('databases/list.html', database_list=database_list)

    @expose('/add', methods=("GET", "POST"))
    def add(self):
        # TODO: Validations for fields
        database_form = DatabaseForm()
        if database_form.validate_on_submit():
            db_session.add(
                Database(
                    name=database_form.name.data,
                    user=database_form.user.data,
                    host=database_form.host.data,
                    password=database_form.password.data
                )
            )
            db_session.commit()
            flash("New database added!", "alert-success")
            return redirect('/admin/databases')

        return self.render('databases/add.html', database_form=database_form)

    @expose('/remove/<int:_id>/', methods=("GET", "POST"))
    def remove(self, _id):
        if _id is not None:
            obj = Database.query.filter_by(id=_id).first()
            db_session.delete(obj)
            db_session.commit()
            flash("Database connection deleted.", "alert-block")

        return redirect('/admin/databases')

    @expose('/edit/<int:_id>/', methods=("GET", "POST"))
    def edit(self, _id):
        # TODO: Validations for fields
        obj = Database.query.filter_by(id=_id).first()
        database_form = DatabaseForm(obj=obj)
        if database_form.validate_on_submit():
            database_form.populate_obj(obj)
            db_session.commit()
            flash("New database modify!", "alert-success")
            return redirect('/admin/databases')

        return self.render('databases/edit.html', database_form=database_form)

    @expose('/connect/<int:_id>/', methods=("GET", "POST"))
    def connect(self, _id):
        if _id is not None:
            db = Database.query.filter_by(id=_id).first()
            db.connect()
            session["db"] = db.id
            flash("Connected to %s." % (db.name), "success")

        return redirect('/admin/databases')

    @expose('/show-tables/<int:_id>/', methods=("GET", "POST"))
    def show_tables(self, _id):
        db = get_db_instance(_id)
        table_list = db.tables
        return self.render('crud/list_tables.html', table_list=table_list)

    @expose('/show-registers/', methods=("GET", "POST"))
    def show_registers(self):
        db = get_db_instance(session)
        table_list = db.tables
        return self.render('crud/list_tables.html', table_list=table_list)


def get_db_instance(database_id):
    if database_id is not None:
        db = Database.query.filter_by(id=database_id).first()
        return db.connect()
    else:
        return None
