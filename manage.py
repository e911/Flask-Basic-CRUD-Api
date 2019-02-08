import os
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import url_for
from app import db
from app.application import create_app
from app.config import config_map
import urllib

app = create_app(config_map[os.environ['FLASK_CONFIG']])

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def list_routes():
	import urllib
	output = []
	for rule in app.url_map.iter_rules():
		options = {}
		for arg in rule.arguments:
			options[arg] = "[{0}]".format(arg)
			methods = ','.join(rule.methods)
			url = url_for(rule.endpoint, **options)
			line = urllib.parse.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
			output.append(line)
	for line in output:
		print (line)

if __name__ == "__main__":
    manager.run()
