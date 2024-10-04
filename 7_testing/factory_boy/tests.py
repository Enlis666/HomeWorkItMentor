import unittest
from factories import UserFactory
import HtmlTestRunner
class TestUserFactory(unittest.TestCase):

    def test_user_factory_creates_user(self):
        user = UserFactory()

        self.assertIsNotNone(user.username)
        self.assertIsNotNone(user.email)
        self.assertIsNotNone(user.first_name)
        self.assertIsNotNone(user.last_name)

        self.assertEqual(user.email, f'{user.username}@example.com')

        user2 = UserFactory()
        self.assertNotEqual(user.username, user2.username)

    def test_user_factory_creates_multiple_users(self):
        users = [UserFactory() for _ in range(5)]

        self.assertEqual(len(users), 5)

        usernames = [user.username for user in users]
        self.assertEqual(len(usernames), len(set(usernames)))

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./report_html'))

