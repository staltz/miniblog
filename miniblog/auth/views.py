from flask import request, url_for, redirect, render_template, g
from flask.ext.login import login_user, logout_user, login_required
from miniblog import app
from miniblog import login_manager
from miniblog.auth.models import Admin, AdminForm


@login_manager.user_loader
def load_user(id):
    return Admin.query.get(int(id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = AdminForm(request.form)
        if form.validate():
            admin = Admin.query.filter_by(username=form.username.data).first()
            if admin is None:
                form.username.errors.append(u"No such user exists.")
            elif form.password.data != admin.password:
                form.password.errors.append(u"Wrong password.")
            else:
                login_user(admin)
                return redirect(url_for('index'))
    else:
        form = AdminForm()
    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
