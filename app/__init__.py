from flask_io import FlaskIO
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
io = FlaskIO()
bcrypt = Bcrypt()
