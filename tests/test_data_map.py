import os
import acrewstic
import tempfile
import redis
import mock
from nose import with_setup


class TestDataMap:

    def setup(self):
        pass
        # self.db_filedescriptor, acrewstic.app.config['DATABASE']
        #     = tempfile.mkstemp()
        # acrewstic.app.config['TESTING'] = True
        # self.app = acrewstic.app.test_client()
        # with acrewstic.app.app_context():
        #     acrewstic.init_db()

    def teardown(self):
        pass
        # os.close(self.db_filedescriptor)
        # os.unlink(acrewstic.app.config['DATABASE'])

    @with_setup(setup, teardown)
    def test(self):
        assert True

    @mock.patch.object(redis.StrictRedis, 'info')
    def test_get_version(self, mock_info):
        mock_info.assert_not_called()
