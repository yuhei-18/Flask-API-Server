import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField
from .objects.index import User, Role, Post


class Query(graphene.ObjectType):
    node = Node.Field()
    users = MongoengineConnectionField(User)
    roles = MongoengineConnectionField(Role)
    posts = MongoengineConnectionField(Post)
