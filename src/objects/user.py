from graphene_mongo import MongoengineObjectType
from graphene.relay import Node
from ..models.index import User as UserModel

class User(MongoengineObjectType):
    class Meta:
        description = "User"
        model = UserModel
        interfaces = (Node,)
