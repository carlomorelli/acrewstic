import json
import mock
import redis
import acrewstic


class TestRestApi:

    @classmethod
    def setup_class(self):
        print "Setting up application..."
        self.client = acrewstic.app.test_client()
        self.client.testing = True

    @classmethod
    def teardown_class(self):
        print "Shutting down application..."

    @mock.patch.object(redis.StrictRedis, 'info')
    def test_0_get_version(self, mock_info):
        # result = self.client.get('/acrewstic/version')
        # assert result.status_code == 200
        self.client.get('/acrewstic/version')
        mock_info.assert_called()

    def test_1_get_tasks(self):
        result = self.client.get('/acrewstic/tasks')
        assert result.status_code == 200
        data = json.loads(result.data)
        print "Receving data: %s" % data
        assert len(data['tasks']) == 2

    def test_2_get_task(self):
        task_id = 2
        result = self.client.get('/acrewstic/tasks/%s' % task_id)
        assert result.status_code == 200
        data = json.loads(result.data)
        print "Receving data: %s" % data
        assert len(data) == 1
        assert data['task']['id'] == task_id

    def test_3_post_task(self):
        new_task = {
            'title': 'NewTitle',
            'description': 'NewDescription'
        }
        result = self.client.post(
            '/acrewstic/tasks',
            data=json.dumps(new_task),
            content_type='application/json'
        )
        assert result.status_code == 201

    def test_4_update_task(self):
        update_task = {
            'title': 'NewTitle2',
            'done': True
        }
        task_id = 2
        result = self.client.put(
            '/acrewstic/tasks/%s' % task_id,
            data=json.dumps(update_task),
            content_type='application/json'
        )
        assert result.status_code == 200
        result = self.client.get('/acrewstic/tasks/%s' % task_id)
        assert result.status_code == 200
        data = json.loads(result.data)
        print "Receving data: %s" % data
        assert data['task']['id'] == task_id
        assert data['task']['done']
        assert data['task']['title'] == 'NewTitle2'

    def test_5_delete_task(self):
        task_id = 1
        result = self.client.delete('/acrewstic/tasks/%s' % task_id)
        assert result.status_code == 200
        data = json.loads(result.data)
        print "Receving data: %s" % data
        assert data['result']

    def test_6_delete_unexisting_task(self):
        task_id = 1
        result = self.client.delete('/acrewstic/tasks/%s' % task_id)
        print "Receving data: %s" % json.loads(result.data)
        assert result.status_code == 404
        data = json.loads(result.data)
        assert data['error'] == 'Not found'

    def test_7_update_unexisting_task(self):
        update_task = {
            'title': 'NewTitle2',
            'done': True
        }
        task_id = 1
        result = self.client.put(
            '/acrewstic/tasks/%s' % task_id,
            data=json.dumps(update_task),
            content_type='application/json'
        )
        print "Receving data: %s" % json.loads(result.data)
        assert result.status_code == 404
        data = json.loads(result.data)
        assert data['error'] == 'Not found'

    def test_8_update_with_with_wrong_encoding(self):
        task_id = 2
        update_task = {
            'done': 'True'
        }
        result = self.client.put(
            '/acrewstic/tasks/%s' % task_id,
            data=json.dumps(update_task),
            content_type='application/json'
        )
        assert result.status_code == 400

    def test_9_get_unexisting_api(self):
        result = self.client.get('/acrewstic/unexisting')
        print "Receving data: %s" % json.loads(result.data)
        assert result.status_code == 404
        data = json.loads(result.data)
        assert data['error'] == 'Not found'


