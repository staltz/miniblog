from flask import request, url_for, redirect, render_template, g
from flask.ext.login import login_user, logout_user, login_required
from miniblog import app
from miniblog import login_manager
from miniblog.admin.models import Admin, AdminForm


@login_manager.user_loader
def load_user(id):
    return Admin.query.get(int(id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = AdminForm()
    if request.method == 'POST':
        form = AdminForm(request.form)
        if form.validate():
            admin = Admin.query.filter_by(username=form.username.data).first()
            if admin is None:
                # TODO fill form.username with error
                assert False
            if admin.password == form.password.data:
                login_user(admin)
                return redirect(url_for('index'))
            else:
                # TODO fill form.password with error
                assert False
    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))