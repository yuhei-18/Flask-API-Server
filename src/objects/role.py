from graphene_mongo import MongoengineObjectType
from graphene.relay import Node
from ..models.index import Role as RoleModel

class Role(MongoengineObjectType):
    class Meta:
        description = "Role"
        model = RoleModel
        interfaces = (Node,)
