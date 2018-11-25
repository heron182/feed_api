from feed.models import User, Comment, Post, Author
from passlib.apps import custom_app_context as pwd_context
from feed import create_app

app = create_app()

with app.app_context():
    user1 = User.objects.create(
        name="John", email="johndoe@test.com", password=pwd_context.encrypt("12345678")
    )

    user2 = User.objects.create(
        name="Jane", email="janedoe@test.com", password=pwd_context.encrypt("12345678")
    )

    comment1 = Comment(
        author=Author(name=user1.name, email=user1.email), content="Comment 1"
    )
    comment2 = Comment(
        author=Author(name=user2.name, email=user2.email), content="Comment 2"
    )

    Post.objects.create(
        author=Author(name=user1.name, email=user1.email),
        title="Post 1",
        content="Content for post 1",
        comments=[comment1, comment2],
    )
    Post.objects.create(
        author=Author(name=user2.name, email=user2.email),
        title="Post 2",
        content="Content for post 2",
        comments=[comment1],
    )
    Post.objects.create(
        author=Author(name=user1.name, email=user1.email),
        title="Post 3",
        content="Content for post 3",
    )
