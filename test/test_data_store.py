import mock
from src.acrewlib import Repository

TEST_KEY_STORE = 'test_key_store'
test_string = 'test1'
test_int = 12345
test_dict = {'test1': 'test2', 12345: 67890}
test_list = range(1, 11)


class TestDataStore:

    def setup_class(self):
        print(f'setup_class: {self.__name__}')
        print('----------------------------------')
        self.store = Repository(host='localhost', port=6379)

        # self.db_filedescriptor, acrewstic.app.config['DATABASE']
        #     = tempfile.mkstemp()
        # acrewstic.app.config['TESTING'] = True
        # self.app = acrewstic.app.test_client()
        # with acrewstic.app.app_context():
        #     acrewstic.init_db()

    def teardown_class(self):
        print(f'teardown_class: {self.__name__}')
        print('----------------------------------')

        # os.close(self.db_filedescriptor)
        # os.unlink(acrewstic.app.config['DATABASE'])

    def setup_method(self):
        self.store.delete(TEST_KEY_STORE)

    def teardown_method(self):
        self.store.delete(TEST_KEY_STORE)

    def test_0_put_string(self):
        current_size = len(self.store.fetch_all(TEST_KEY_STORE))
        assert current_size == 0
        self.store.append_item(TEST_KEY_STORE, test_string)
        new_size = len(self.store.fetch_all(TEST_KEY_STORE))
        assert new_size == current_size + 1
        print("Successfully setting up string")

    def test_1_put_int(self):
        current_size = len(self.store.fetch_all(TEST_KEY_STORE))
        assert current_size == 0
        self.store.append_item(TEST_KEY_STORE, test_int)
        new_size = len(self.store.fetch_all(TEST_KEY_STORE))
        assert new_size == current_size + 1
        print("Successfully setting up int")

    def test_2_put_dict(self):
        current_size = len(self.store.fetch_all(TEST_KEY_STORE))
        assert current_size == 0
        self.store.append_item(TEST_KEY_STORE, test_dict)
        new_size = len(self.store.fetch_all(TEST_KEY_STORE))
        assert new_size == current_size + 1
        print("Successfully setting up dict")

    def test_3_append_and_get(self):
        current_size = len(self.store.fetch_all(TEST_KEY_STORE))
        assert current_size == 0
        self.store.append_item(TEST_KEY_STORE, test_string)
        self.store.append_item(TEST_KEY_STORE, test_int)
        self.store.append_item(TEST_KEY_STORE, test_dict)
        new_size = len(self.store.fetch_all(TEST_KEY_STORE))
        assert new_size == current_size + 3
        item = self.store.get_item(TEST_KEY_STORE, 0)
        assert isinstance(item, str)
        item = self.store.get_item(TEST_KEY_STORE, 1)
        assert isinstance(item, int)
        item = self.store.get_item(TEST_KEY_STORE, 2)
        assert isinstance(item, dict)
        print("Successfully appending string, int and dict in correct order")

    def test_4_set_and_get(self):
        self.store.set(TEST_KEY_STORE, test_list)
        current_size = len(self.store.fetch_all(TEST_KEY_STORE))
        assert current_size == len(test_list)
        index = 4
        item = self.store.get_item(TEST_KEY_STORE, index)
        assert isinstance(item, int)
        assert item == index + 1
        new_size = len(self.store.fetch_all(TEST_KEY_STORE))
        assert new_size == len(test_list)
        assert new_size == current_size
        item = self.store.get_item(TEST_KEY_STORE, index)
        assert item == index + 1
        print("Successfully setting up list and retrieving items")
