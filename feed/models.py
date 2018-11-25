from mongoengine import (
    Document,
    EmailField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    ListField,
    StringField,
)


class User(Document):
    name = StringField(required=True, max_length=100)
    password = StringField(required=True)
    email = EmailField(required=True)


class Author(EmbeddedDocument):
    name = StringField(required=True, max_length=100)
    email = EmailField(required=True)


class Comment(EmbeddedDocument):
    author = EmbeddedDocumentField(Author)
    content = StringField(required=True, max_length=200)


class Post(Document):
    author = EmbeddedDocumentField(Author)
    title = StringField(required=True, max_length=100)
    content = StringField(required=True)
    comments = ListField(EmbeddedDocumentField(Comment))
