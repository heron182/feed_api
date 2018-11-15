### A simple Flask/MongoDB API simulating a social network feed

#### Local development:
```
sudo docker-compose up -d
firefox localhost:8000/api/feed
```

#### GET [/feed]

#### 200
```
[
    {
        "pk": 1,
        "author": {
            "pk": 1,
            "name": "John Doe",
        },
        "title": "Awesome post",
        "content": "My super awesome post",
        "comments": [
            {
                "pk": 1,
                "author": {
                    "pk": 2,
                    "name": "Jane Doe",
                },
                "content": "Super cool"
            }
        ],
    },
    {
        "pk": 1,
        "author": {
            "pk": 1,
            "name": "Jane Doe",
        }
        "title": "Sooo sleepy",
        "content": "Just chilling",
        "comments": []
    }
]
```

#### POST [/feed]

```
{
    "author": {
        "pk": 1,
        "name": "John Doe",
    },
    "title": "Awesome post",
    "content": "My super awesome post"
}
```

#### POST [/feed/<feed-id>/comment]

```
{
    "author": {
        "pk": 2,
        "name": "Jane Doe"
    },
    "comment": "What a nice post huh!"
}
```

#### GET [/users]

```
[
    {
        "pk": 1,
        "name": "John Doe",
        "email": "jon@doe.com"
    },
    {
        "pk": 2,
        "name": "Jane Doe",
        "email": "jane@doe.com"
    }
]
```

#### POST [/users]

```
[
    {
        "name": "John Doe",
        "email": "john@doe.com",
        "password": "johnpasswd"
    }
]
```