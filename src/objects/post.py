from graphene_mongo import MongoengineObjectType
from graphene.relay import Node
from ..models.index import Post as PostModel

class Post(MongoengineObjectType):
    class Meta:
        description = "Post"
        model = PostModel
        interfaces = (Node,)
