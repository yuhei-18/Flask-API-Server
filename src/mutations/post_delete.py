import graphene
from ..models.index import Post as PostModel
from ..objects.index import Post


class DeletePostInput(graphene.InputObjectType):
    """
    投稿削除 Mutation 用の Input
    """
    id = graphene.String(required=True ,description="対象の投稿ID")


class DeletePost(graphene.Mutation):
    """
    投稿削除 Mutation
    """
    id = graphene.String()

    class Arguments:
        input = DeletePostInput()

    @staticmethod
    def mutate(rooot, info, input):
        post = PostModel.objects.get(id=input.id)
        post.delete()
        return DeletePost(id=input.id)
