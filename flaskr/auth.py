#imports
import functools

from flask import abort

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from pandas.io.sql import execute
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


#Route and functionality for the register page
@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return redirect(url_for("auth.login"))

        flash(error)

    return render_template('auth/register.html')



# route and functionality built-in for logging in
@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


# route and functionality built-in for logging out
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

# functionality for loading the user information for the webpage
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


#route for function to call admin page
@bp.route('/admin', methods=('GET', 'POST'))
def admin():
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']



        db = get_db()
        db.execute(
            'UPDATE post SET title = ?, body = ?'
            ' WHERE id = ?',
            (title, content, id)
        )
        db.commit()
        return redirect(url_for('auth.admin'))

    db = get_db()
    error = None


    flash(error)
    threat = db.execute(
        'SELECT id, title, username, author_user_id, Field1, Field2, Field3, Field4, description, created_at, updated_at'
        ' FROM threat'
        ' ORDER BY updated_at DESC'

    ).fetchall()

    post = db.execute(
        'SELECT id, title, body, created, author_id'
        ' FROM post'

    ).fetchall()

    threats=threat
    posts=post

    return render_template('auth/admin.html', threats=threats, posts=posts)


'''
#function that's called when delete button is selected and user wants to delete blog post.
@bp.route('/<int:id>/delete', methods=('POST'))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('auth.admin'))
'''

#function that's called when post webpage is or is not found.
def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post