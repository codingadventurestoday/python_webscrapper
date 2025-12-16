import unittest

from helper.crawl import normalize_url

class testCrawl(unittest.TestCase):
    def test_normalize_url(self):
        input_url = "https://blog.boot.dev/path"
        actual = normalize_url(input_url)
        expected = 'blog.boot.dev/path'
        self.assertEqual(actual, expected)

    def test_http_normalize_url(self):
        input_url = "http://blog.boot.dev/path"
        actual = normalize_url(input_url)
        expected = 'blog.boot.dev/path'
        self.assertEqual(actual,expected)

    def test_backslash_normalize_url(self):
        input_url = "http://blog.boot.dev/path/"
        actual = normalize_url(input_url)
        expected = 'blog.boot.dev/path'
        self.assertEqual(actual,expected)

    def test_normalize_url_capitals(self):
        input_url = "https://BLOG.boot.dev/path"
        actual = normalize_url(input_url)
        expected = "blog.boot.dev/path"
        self.assertEqual(actual, expected)    

if __name__ == '__main__':
    unittest.main()