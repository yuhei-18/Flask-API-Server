import datetime
from mongoengine import Document
from mongoengine.fields import DateTimeField

NULLIFY = 1  # リレーションがなくなった場合に NULL が設定される


class BaseDocument(Document):
    meta = {'abstract': True}

    created_at = DateTimeField()
    updated_at = DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        return super(BaseDocument, self).save(*args, **kwargs)
