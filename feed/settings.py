class DevSettings(object):
    MONGODB_SETTINGS = {"host": "mongodb://db:27017/feed"}


class TestSettings(object):
    MONGODB_SETTINGS = {"host": "mongodb://db:27017/feed_test"}
    TESTING = True
