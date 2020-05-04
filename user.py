from flask import Blueprint, current_app, request, jsonify
from .model import User
from .serializer import UserSchema

bp_user = Blueprint('User', __name__)

@bp_user.route('/user', methods=['GET'])
def all():
    us = UserSchema(many=True)
    result = User.query.all()
    return us.jsonify(result), 200

@bp_user.route('/user', methods=['POST'])
def add():
    try:
        u = User(request.json["name"], request.json["email"])
        current_app.db.session.add(u)
        current_app.db.session.commit()
        return jsonify({'msg': 'success'})
    except:
        return jsonify({'msg': 'error'})

@bp_user.route('/user/<id>', methods=['DELETE'])
def delete(id):
    User.query.filter(User.id == id).delete()
    try:
        current_app.db.session.commit()
        return jsonify({'msg': 'success'})
    except:
        return jsonify({'msg': 'error'})

@bp_user.route('/user/<id>', methods=['PUT'])
def modify(id):
    query = User.query.filter(User.id == id)
    query.update(request.json)
    try:
        current_app.db.session.commit()
        return jsonify({'msg': 'success'})
    except:
        return jsonify({'msg': 'error'})
    current_app.db.session.commit()


@bp_user.route('/user/<id>/groups', methods=['GET'])
def usergroups(id):
    us = UserSchema(many=True)
    user = User.query.get(id)
    return us.jsonify(user.groupuser), 200