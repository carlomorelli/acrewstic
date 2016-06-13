import os
import acrewstic
import tempfile
from nose import with_setup







class TestDataMap():

    def setup(self):
        print "this is the setup"
        # self.db_filedescriptor, acrewstic.app.config['DATABASE'] = tempfile.mkstemp()
        # acrewstic.app.config['TESTING'] = True
        # self.app = acrewstic.app.test_client()
        # with acrewstic.app.app_context():
        #     acrewstic.init_db()

    def teardown(self):
        print"this is the teardown"
        # os.close(self.db_filedescriptor)
        # os.unlink(acrewstic.app.config['DATABASE'])


    @with_setup(setup, teardown)
    def test(self):
        assert True