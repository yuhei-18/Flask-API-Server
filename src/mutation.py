import graphene
from .mutations.index import (
    CreateUser,
    CreatePost,
    UpdatePost,
    CreateRole,
)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    create_role = CreateRole.Field()
