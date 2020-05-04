from flask import Blueprint, current_app, request, jsonify
from .model import Subscribe, Group, User
from .serializer import SubscribeSchema

bp_subscribe = Blueprint('Subscribe', __name__)

@bp_subscribe.route('/subscribe', methods=['GET'])
def all():
    subscribe = Subscribe.query.all()
    result = []
    for sub in subscribe:
        user = sub.recipient
        item = {"id": sub.id, "email": user.email, "is_send": sub.is_send}
        result.append(item)
    return jsonify(result), 200

@bp_subscribe.route('/subscribe/group', methods=['POST'])
def subsgroup():
    group = Group.query.get(request.json['group_id'])    
    for user in group.groupuser:
        user_sub = User.query.get(user.id) 
        s = Subscribe(recipient = user_sub, is_send = True)
        current_app.db.session.add(s)
    try:
        current_app.db.session.commit()
        return jsonify({'msg': 'success'})
    except:
        return jsonify({'msg': 'error'})

@bp_subscribe.route('/subscribe/user', methods=['POST'])
def subsuser():
    try:
        for user in request.json:
            user_sub = User.query.get(user["user_id"]) 
            s = Subscribe(recipient = user_sub, is_send = True)
            current_app.db.session.add(s)
        current_app.db.session.commit()
        return jsonify({'msg': 'success'})
    except:
        return jsonify({'msg': 'error'})