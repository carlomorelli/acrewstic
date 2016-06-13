import json
import acrewstic
import threading
from nose import with_setup
from urllib2 import urlopen


class ClientApi():
    def request(self, api):
        url = "http://localhost:5000" + api
        response = urlopen(url)
        raw_data = response.read().decode('utf-8')
        return json.loads(raw_data)


# class ServerApi(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#         self.app = acrewstic.app
#     def run(self):
#         self.app.run()


class TestRestApi():

    def setup(self):
        self.client = ClientApi()
        # self.server = ServerApi()
        


    @with_setup(setup)
    def test_get_tasks(self):
        api = '/acrewstic/tasks'
        # self.server.start()
        try:
            response = self.client.request(api)
            print response
            assert 'tasks' in response
            #self.assertEqual(response['name'], 'Test User')
        except:
            print "ERROR: connection rejected"
            assert False
