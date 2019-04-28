import json
from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest


class StoreTests(BaseTest):
    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                resp = client.post('/store/tests')

                self.assertEqual(resp.status_code, 201)
                self.assertIsNotNone(StoreModel.find_by_name('tests'))
                self.assertDictEqual({'id': 1, 'name': 'tests', 'items': []},
                                     json.loads(resp.data))

    def test_create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                client.post('/store/tests')
                resp = client.post('/store/tests')

                self.assertEqual(resp.status_code, 400)
                self.assertDictEqual({'message': "A store with name '{}' already exists.".format('tests')},
                                     json.loads(resp.data))

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                store = StoreModel('tests').save_to_db()
                resp = client.delete('/store/tests')

                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({'message': 'Store deleted'},
                                     json.loads(resp.data))

    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                store = StoreModel('tests').save_to_db()
                resp = client.get('/store/tests')

                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({'id': 1, 'name': 'tests', 'items': []},
                                     json.loads(resp.data))

    def test_store_not_found(self):
        with self.app() as client:
            with self.app_context():
                resp = client.get('/store/tests')

                self.assertEqual(resp.status_code, 404)
                self.assertDictEqual({'message': 'Store not found'},
                                     json.loads(resp.data))

    def test_store_found_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('tests').save_to_db()
                ItemModel('tests', 19.99, 1).save_to_db()

                resp = client.get('/store/tests')
                self.assertEqual(resp.status_code, 200)
                self.assertDictEqual({'id': 1, 'name': 'tests', 'items': [{'name': 'tests', 'price': 19.99}]},
                                     json.loads(resp.data))

    def test_store_list(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('tests').save_to_db()

                resp = client.get('/stores')
                self.assertDictEqual({'stores': [{'id': 1, 'name': 'tests', 'items': []}]},
                                     json.loads(resp.data))

    def test_store_list_with_items(self):
        with self.app() as client:
            with self.app_context():
                StoreModel('tests').save_to_db()
                ItemModel('tests', 19.99, 1).save_to_db()

                resp = client.get('/stores')

                self.assertDictEqual({'stores': [{'id': 1, 'name': 'tests', 'items': [{'name': 'tests', 'price': 19.99}]}]},
                                     json.loads(resp.data))
