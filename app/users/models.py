from datetime import datetime
import json
from sqlalchemy.sql.sqltypes import DateTime
from .. import db, bcrypt


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    enabled = db.Column(db.Boolean(), nullable=False, default=True)
    updated_at = db.Column(db.DateTime(), nullable=False, default=lambda: datetime.utcnow())
    created_at = db.Column(db.DateTime(), nullable=False, default=lambda: datetime.utcnow())

    def __init__(self, email, password):
        self.email = email
        self.enabled = True
        self.password = User.hashed_password(password)

    @staticmethod
    def hashed_password(password):
        return bcrypt.generate_password_hash(password).decode('utf-8')

    @staticmethod
    def get_user_with_email_and_password(email, password):
        user = User.query.filter_by(email=email).first()
        print(bcrypt.check_password_hash(user.password,password))
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return None
    
    def __repr__(self):
        return to_json(self, self.__class__)


def to_json(inst, cls):
    """
    Jsonify the sql alchemy query result.
    """
    d = dict()
    for c in cls.__table__.columns:
        v = getattr(inst, c.name)
        if isinstance(c.type, DateTime) and v is not None:
            try:
                d[c.name] = v.__str__()
            except:
                d[c.name] = "Error:  Failed to covert using "
        elif v is None:
            d[c.name] = str()
        else:
            d[c.name] = v
    return json.dumps(d)