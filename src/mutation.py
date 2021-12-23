import graphene
from .mutations.index import CreateUser, CreatePost


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()
