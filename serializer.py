from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from .model import Group, User, Subscribe

# Init ma
ma = Marshmallow()


def configure(app):
    ma.init_app(app)

# Group Schema
class GroupSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Group
        load_instance = False

# User Schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = False

# Subscribe Schema
class SubscribeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Subscribe
        load_instance = False
