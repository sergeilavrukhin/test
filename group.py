from flask import Blueprint, current_app, request, jsonify
from .model import Group
from .serializer import GroupSchema

bp_group = Blueprint('group', __name__)

@bp_group.route('/group', methods=['GET'])
def all():
    gs = GroupSchema(many=True)
    result = Group.query.all()
    return gs.jsonify(result), 200

@bp_group.route('/group', methods=['POST'])
def add():
    try:
        g = Group(request.json["name"])
        current_app.db.session.add(g)
        current_app.db.session.commit()
        return jsonify({'msg': 'success'})
    except:
        return jsonify({'msg': 'error'})

@bp_group.route('/group/<id>', methods=['DELETE'])
def delete(id):
    Group.query.filter(Group.id == id).delete()
    try:
        current_app.db.session.commit()
        return jsonify({'msg': 'success'})
    except:
        return jsonify({'msg': 'error'})

@bp_group.route('/group/<id>', methods=['PUT'])
def modify(id):
    query = Group.query.filter(Group.id == id)
    query.update(request.json)
    try:
        current_app.db.session.commit()
        return jsonify({'msg': 'success'})
    except:
        return jsonify({'msg': 'error'})


@bp_group.route('/group/<id>/users', methods=['GET'])
def groupusers(id):
    gs = GroupSchema(many=True)
    group = Group.query.get(id)
    return gs.jsonify(group.groupuser), 200