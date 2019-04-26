from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest


class UserTest(UnitBaseTest):
    def test_create_user(self):
        user = UserModel('test', 'abc')

        self.assertEqual(user.username, 'test',
                         'Username "{}" cannot be found, please try again with a valid username.'.format(user.username))
        self.assertEqual(user.password, 'abc',
                         'Invalid password, please try again with a valid password')
