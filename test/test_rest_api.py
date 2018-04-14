import json
import mock
from src.acrewstic import app
import mockredis


class TestRestApi:

    def setup_class(self):
        print(f'setup_class: {self.__name__}')
        print('----------------------------------')
        self.client = app.test_client()
        self.client.testing = True

    def teardown_class(self):
        print(f'teardown_class: {self.__name__}')
        print('----------------------------------')

    @mock.patch('redis.StrictRedis', mockredis.mock_strict_redis_client)
    def test_0_get_version(self):
        # mock_info.return_value = json.dumps({'version': 'fakeRedis'})
        result = self.client.get('/acrewstic/version')
        assert result.status_code == 200
        # mock_info.assert_called()
        data = json.loads(result.data)
        print(f'Receiving data: {data}')
        # assert data['redis_info']['version'] == 'fakeRedis'

    def test_1_get_tasks(self):
        result = self.client.get('/acrewstic/tasks')
        assert result.status_code == 200
        data = json.loads(result.data)
        print(f'Receiving data: {data}')
        assert len(data['tasks']) == 2

    def test_2_get_task(self):
        task_id = 2
        result = self.client.get('/acrewstic/tasks/%s' % task_id)
        assert result.status_code == 200
        data = json.loads(result.data)
        print(f'Receiving data: {data}')
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
            f'/acrewstic/tasks/{task_id}',
            data=json.dumps(update_task),
            content_type='application/json'
        )
        assert result.status_code == 200
        result = self.client.get(f'/acrewstic/tasks/{task_id}')
        assert result.status_code == 200
        data = json.loads(result.data)
        print(f'Receiving data: {data}')
        assert data['task']['id'] == task_id
        assert data['task']['done']
        assert data['task']['title'] == 'NewTitle2'

    def test_5_delete_task(self):
        task_id = 1
        result = self.client.delete(f'/acrewstic/tasks/{task_id}')
        assert result.status_code == 200
        data = json.loads(result.data)
        print(f'Receiving data: {data}')
        assert data['result']

    def test_6_delete_unexisting_task(self):
        task_id = 1
        result = self.client.delete(f'/acrewstic/tasks/{task_id}')
        print(f'Receiving data: {json.loads(result.data)}')
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
            f'/acrewstic/tasks/{task_id}',
            data=json.dumps(update_task),
            content_type='application/json'
        )
        print(f'Receiving data: {json.loads(result.data)}')
        assert result.status_code == 404
        data = json.loads(result.data)
        assert data['error'] == 'Not found'

    def test_8_update_with_with_wrong_encoding(self):
        task_id = 2
        update_task = {
            'done': 'True'
        }
        result = self.client.put(
            f'/acrewstic/tasks/{task_id}',
            data=json.dumps(update_task),
            content_type='application/json'
        )
        assert result.status_code == 400

    def test_9_get_unexisting_api(self):
        result = self.client.get('/acrewstic/unexisting')
        print(f'Receiving data: {json.loads(result.data)}')
        assert result.status_code == 404
        data = json.loads(result.data)
        assert data['error'] == 'Not found'
