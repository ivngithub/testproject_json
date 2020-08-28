import click

from flask_script import Manager, Shell
from flask_migrate import MigrateCommand

from app import app, db

manager = Manager(app)


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@app.cli.command('start-project')
def start_project():
    """
    start project start-project >>>db.create_all()
    """
    from app import db
    db.create_all()


if __name__ == '__main__':
    manager.run()
