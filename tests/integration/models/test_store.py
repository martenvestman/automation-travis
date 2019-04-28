from models.store import StoreModel
from models.item import ItemModel
from tests.base_test import BaseTest


class StoreTest(BaseTest):
    """
    def test_create_store_items_empty(self):
        store = StoreModel('tests')

        self.assertListEqual(store.items.all(), [],
                             "The store's items length was not 0 even though no items were added.")
    """

    def test_crud(self):
        with self.app_context():
            store = StoreModel('tests')

            self.assertIsNone(StoreModel.find_by_name('tests'),
                              "Found a store named 'tests' even though no store was created.")

            store.save_to_db()

            self.assertIsNotNone(StoreModel.find_by_name('tests'),
                                 "Did not find expected store named 'tests'.")

            store.delete_from_db()

            self.assertIsNone(StoreModel.find_by_name('tests'),
                              "Found a store named 'tests' even though all records in list were deleted")

    def test_store_relationship(self):
        with self.app_context():
            store = StoreModel('tests')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            self.assertEqual(store.items.count(), 1)
            self.assertEqual(store.items.first().name, 'test_item')

    def test_store_json(self):
        store = StoreModel('tests')
        expected = {
            'id': None,
            'name': 'tests',
            'items': []
            }

        self.assertDictEqual(store.json(), expected)

    def test_store_json_with_item(self):
        with self.app_context():
            store = StoreModel('tests')
            item = ItemModel('test_item', 19.99, 1)

            store.save_to_db()
            item.save_to_db()

            expected = {
                'id': 1,
                'name': 'tests',
                'items': [{'name': 'test_item', 'price': 19.99}]
            }

            self.assertDictEqual(store.json(), expected)
