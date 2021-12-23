import graphene
from ..models.index import Post as PostModel, User
from ..objects.index import Post


class UpdatePostInput(graphene.InputObjectType):
    """
    投稿更新 Mutation 用の Input
    """
    id = graphene.String(required=True ,description="対象の投稿ID")
    text = graphene.String(description="投稿の内容")
    author_email = graphene.String(description="投稿者のメールアドレス")
    is_publish = graphene.Boolean(description="投稿を公開するかのフラグ")


class UpdatePost(graphene.Mutation):
    """
    投稿更新 Mutation
    """
    post = graphene.Field(Post)

    class Arguments:
        input = UpdatePostInput()

    @staticmethod
    def mutate(root, info, input):
        post = PostModel.objects.get(id=input.id)

        if input.author_email:
            user = User.objects.get(email=input.author_email)
            post.author = user

        if input.text:
            post.text = input.text

        if input.is_publish is not None:
            post.is_publish = input.is_publish

        post.save()
        return UpdatePost(post=post)
