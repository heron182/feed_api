from mongoengine import (
    Document,
    EmailField,
    ListField,
    ReferenceField,
    StringField,
    EmbeddedDocument,
    EmbeddedDocumentField,
)


class User(Document):
    name = StringField(required=True, max_length=100)
    password = StringField(required=True, min_length=8, max_length=50)
    email = EmailField(required=True)


class Comment(EmbeddedDocument):
    author = ReferenceField(User)
    comment = StringField(required=True, max_length=200)


class Post(Document):
    author = ReferenceField(User)
    title = StringField(required=True, max_length=100)
    content = StringField(required=True)
    comments = ListField(EmbeddedDocumentField(Comment))
