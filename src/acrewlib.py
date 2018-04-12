import json
from redis import StrictRedis


class Repository:

    def __init__(self, host, port):
        self.r = StrictRedis(host=host, port=port)

# store dictionary
#    redis.hmset(hkey, dict_to_store)
# retrieve dictionary
#    redis.hmget(hkey)
# lists
#    redis.lappend(hkey, string)
#    redis.llen

    def get_item(self, key_store, index):
        length = self.r.llen(key_store)
        if length == 0:
            return None
        if index >= length:
            raise Exception('Index out of range.')
        item_json = self.r.lindex(key_store, length - (index + 1))
        item_dict = json.loads(item_json)
        return item_dict

    def append_item(self, key_store, item):
        item_json = json.dumps(item)
        if not self.r.lpush(key_store, item_json):
            raise Exception('Unable to write key_store: [%s]' % item_json)

    def fetch_all(self, key_store):
        q = []
        length = self.r.llen(key_store)
        for i in range(length):
            item_json = self.r.lindex(key_store, length - (i + 1))
            item_dict = json.loads(item_json)
            q.append(item_dict)
        return q

    def set(self, key_store, list):
        self.r.delete(key_store)
        for item_dict in list:
            item_json = json.dumps(item_dict)
            if not self.r.lpush(key_store, item_json):
                raise Exception('Unable to write key_store: [%s]' % item_json)

    def delete(self, key_store):
        self.r.delete(key_store)
