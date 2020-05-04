from flask import Blueprint, current_app, request, jsonify
from .model import Group, User

bp_groupuser = Blueprint('groupuser', __name__)

#GroupUser relsationship
@bp_groupuser.route('/groupuser/<id>', methods=['PUT'])
def groupuser(id):
    try:
        group = Group.query.get(id)
        user = User.query.get(request.json["user_id"])
        group.groupuser.append(user)
        current_app.db.session.commit()
        return jsonify({'msg': 'success'})
    except:
        return jsonify({'msg': 'error'})

#GroupUser delete relsationship
@bp_groupuser.route('/groupuser/<id>/<user_id>', methods=['DELETE'])
def groupuserdelete(id, user_id):
    group = Group.query.get(id)
    for i in range(len(group.groupuser)):
        print(group.groupuser[i])
        user = group.groupuser[i]
        if int(user.id) == int(user_id):
            group.groupuser.pop(i)
            break
    try:
        current_app.db.session.commit()
        return jsonify({'msg': 'success'})
    except:
        return jsonify({'msg': 'error'})