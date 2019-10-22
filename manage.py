from flask_script import Command
from flask_script import Manager

from application import app

manager = Manager(app)

class Debug(Command):
    def run(self):
        app.run(host='0.0.0.0', port=5000, debug=True)

class Run(Command):
    def run(self):
        app.run(host='0.0.0.0', port=5000, debug=False)


if __name__ == "__main__":
    manager.add_command('debug', Debug)
    manager.add_command('run', Run)
    manager.run()