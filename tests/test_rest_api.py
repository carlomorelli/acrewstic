import json
import logging
import acrewstic


class TestRestApi: 

    @classmethod
    def setup_class(self):
        print "Setting up application"
        self.client = acrewstic.app.test_client()
        self.client.testing = True 

    @classmethod
    def teardown_class(self):
        print "Shutting down application"
        pass 

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
            'title'       : 'NewTitle',
            'description' : 'NewDescription'
        }
        result = self.client.post('/acrewstic/tasks', data=json.dumps(new_task), content_type = 'application/json')
        assert result.status_code == 201

    def test_4_update_task(self):
        update_task = {
            'title' : 'NewTitle2',
            'done'  : True
        }
        task_id = 2
        result = self.client.put('/acrewstic/tasks/%s' % task_id, data=json.dumps(update_task), content_type = 'application/json')
        assert result.status_code == 200
        result = self.client.get('/acrewstic/tasks/%s' % task_id)
        assert result.status_code == 200
        data = json.loads(result.data)
        print "Receving data: %s" % data
        assert data['task']['id'] == task_id
        assert data['task']['done'] == True
        assert data['task']['title'] == 'NewTitle2'
        
    def test_5_delete_task(self):
        task_id = 1
        result = self.client.delete('/acrewstic/tasks/%s' % task_id) 
        assert result.status_code == 200
        data = json.loads(result.data)
        print "Receving data: %s" % data
        assert data['result'] == True