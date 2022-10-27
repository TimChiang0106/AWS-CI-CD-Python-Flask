import unittest
from main import hello_world


class TestHelloApp(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello_world(), "Hello Production World!")


if __name__ == '__main__':
    unittest.main()
