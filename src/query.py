import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField
from .objects.index import User


class Query(graphene.ObjectType):
    node = Node.Field()
    all_users = MongoengineConnectionField(User)
