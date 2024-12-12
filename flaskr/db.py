#imports
import sqlite3
from datetime import datetime

import click
from flask import current_app, g

# function used to connect to and call on data from the SQL database.
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

#Function used to close db
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

#Function used to call init_db
def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


#Function used to call the click command
@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


sqlite3.register_converter(
    "timestamp", lambda v: datetime.fromisoformat(v.decode())
)

#Function used to start the command
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)