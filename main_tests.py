import unittest

from main import Valuefetch


class TestValueFetch(unittest.TestCase):
    def test_runSuccessTest(self):
        print("test")
        valuefetch = Valuefetch()
        actual = valuefetch.process('{"a":{"b":{"c":"d"}}}', "a/b/c")
        expected = "d"
        self.assertEqual(actual, expected)

    def test_runKeyNotPresentTest(self):
        valuefetch = Valuefetch()
        actual = valuefetch.process('{"a":{"b":{"c":"d"}}}', "a/d/c")
        expected = "Invalid key:\t" + "d"
        self.assertEqual(actual, expected)

    def test_runJsonFailTest(self):
        valuefetch = Valuefetch()
        actual = valuefetch.process('{"a":{"b":{"c":"d"}}', "a/b/c")
        expected = "Invalid Json input"
        self.assertEqual(actual, expected)


if __name__ == '__main_tests__':
    unittest.main()
