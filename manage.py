import click
from flask.cli import with_appcontext

from application import app
from application import db

from script.github_crawling import Crawing


@click.command(name='github')
@click.option('--keyword')
@click.option('--page', default=1)
@with_appcontext
def github(keyword, page):
    gc = Crawing(app, db)
    gc.searcher(keyword, page)


@click.command(name='create_db')
@with_appcontext
def create_db():
    db.create_all()


app.cli.add_command(github)
app.cli.add_command(create_db)

if __name__ == "__main__":
    app.run()
