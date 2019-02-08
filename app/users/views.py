from datetime import datetime
from flask import Blueprint
from flask import request, jsonify,redirect,g
from flask_io import fields
from sqlalchemy import func
from sqlalchemy_utils.functions import sort_query
from .models import User
from .schemas import UserSchema
from .. import db, io
from app.application import logger
from sqlalchemy.exc import IntegrityError

app = Blueprint('users', __name__, url_prefix='/users')


@app.route('/create_user', methods=['POST'])
@io.from_body('user', UserSchema)
@io.marshal_with(UserSchema)
def create_user(user):
    print(user)
    u = User(email=user["email"], password=user["password"])
    db.session.add(u)
    try:
        db.session.commit()
    except IntegrityError:
        return jsonify(message="User with that email already exists"), 409

    # new_user = User.query.filter_by(email=user["email"]).first()
    # return jsonify(
    #         id = new_user.id,
    #         token = (new_user)
    #     )


@app.route("/user", methods=["GET"])
@io.marshal_with(UserSchema)
def get_current_user():
    return jsonify(result=g.current_user)


@app.route('/<int:id>', methods=['GET'])
@io.marshal_with(UserSchema)
def get_user(id):
    user = User.query.with_entities(User.id, User.email, User.created_at, User.enabled).filter_by(id=id).first()
    if not user:
        return io.not_found('User not found: ' + str(id))

    return jsonify(result=user)


@app.route('/', methods=['GET'])
@io.from_query('email', fields.String())
@io.from_query('order_by', fields.String(missing='email'))
@io.from_query('offset', fields.Integer(missing=0))
@io.from_query('limit', fields.Integer(missing=10))
@io.marshal_with(UserSchema)
def list_users(email, order_by, offset, limit):
    query = User.query.with_entities(User.id, User.email, User.created_at, User.enabled)

    if email:
        query = query.filter(func.lower(User.email).contains(func.lower(email)))
    if order_by:
        query = sort_query(query, order_by)
    if offset:
        query = query.offset(offset)
    if limit:
        query = query.limit(limit)

    return jsonify(result=query.all())
