### GET [/feeds]

#### 200
```
[
    {
        "pk": 1,
        "author": {
            "pk": 1
            "name": "John Doe",
        }
        "title": "Awesome post",
        "content": "My super awesome post"
        "comments": [
            {
                "pk": 1,
                "author": {
                    "pk": 2,
                    "name": "Jane Doe",
                }
                "content": "Super cool"
            }
        ]
    },
    {
        "pk": 1,
        "author": {
            "pk": 1
            "name": "Jane Doe",
        }
        "title": "Sooo sleepy",
        "content": "Just chilling"
        "comments": []
    }
]
```

### POST [/feeds]

```
{
    "author": {
        "pk": 1
        "name": "John Doe",
    }
    "title": "Awesome post",
    "content": "My super awesome post"
}
```


### GET [/users]

```
[
    {
        "pk": 1
        "name": "John Doe"
    },
    {
        "pk": 2
        "name": "Jane Doe"
    }
]
```