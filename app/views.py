from app import app, lm, db
from flask import g, render_template, current_app, redirect
from flask_login import current_user
from datetime import datetime
from app.login.models import User
from app.entities.models import Scheduler


@app.route('/')
def main():
    if not current_user.is_authenticated:
        return redirect('/login')
    resources_data = Scheduler.get_resources_data()
    data = Scheduler.get_data_group(current_user)
    return render_template('main.html', title='Schedule',
                           resourcesData=resources_data, data=data)


@lm.user_loader
def load_user(id_user):
    return User.query.get(int(id_user))


@app.before_request
def before_request():
    g.user = current_user
    if g.user.is_authenticated:
        g.user.last_seen = datetime.utcnow()
        db.session.commit()


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    raise error  # Show real error in debug mode


def log_error(*args, **kwargs):
    current_app.logger.error(*args, **kwargs)
