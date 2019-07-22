from flask import render_template, Blueprint, flash, redirect, url_for
from .user_models import db, User
from aplikasi import has_role, login_required
from . import ModelView
from wtforms import PasswordField
from aplikasi.otentikasi import bcrypt

pengguna_bp = Blueprint(
    'pengguna',
    __name__,
    template_folder='../templates/anggota',
    url_prefix="/pengguna"
)

class UserAdminView(ModelView):
    column_searchable_list = ('username',)
    column_sortable_list = ('username',)
    column_exclude_list = ('created_at', 'updated_at')
    form_excluded_columns = ('password',)

    def scaffold_form(self):
        form_class = super(UserAdminView, self).scaffold_form()
        # form_class.password = PasswordField('Password')
        return form_class
    
    def create_model(self, form):
        model = self.model()
        model.username = form.username.data
        model.password = bcrypt.generate_password_hash(form.password.data)
        form.populate_obj(model)
        self.session.add(model)
        self._on_model_change(form, model, True)
        self.session.commit()