from mongoengine.fields import StringField, ReferenceField, BooleanField
from .base import BaseDocument, NULLIFY
from .index import User


class Post(BaseDocument):
    """
    投稿情報
    """
    meta = {"collection": "Posts"}

    text = StringField(
        db_field="text",
        help_text="投稿の内容",
        requred=True
    )
    author = ReferenceField(
        User, reverse_delete_rule=NULLIFY,
        db_field="author",
        help_text="投稿者の情報",
        requred=True
    )
    is_publish = BooleanField(
        db_field="is_publish",
        help_text="投稿を公開するかのフラグ"
    )
