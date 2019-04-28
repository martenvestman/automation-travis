from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('tests', 'abc')

        self.assertEqual(user.username, 'tests',
                         'Username "{}" cannot be found, please try again with a valid username.'.format(user.username))
        self.assertEqual(user.password, 'abc',
                         'Invalid password, please try again with a valid password')
