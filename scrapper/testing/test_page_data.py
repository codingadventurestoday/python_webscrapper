import unittest

from scrap_code.scrap_website import extract_page_data

class TestExtractPageData(unittest.TestCase):
    def test_extract_page_data_basic(self):
        input_url = "https://blog.boot.dev"
        input_body = '''<html><body>
        <h1>Test Title</h1>
        <p>This is the first paragraph.</p>
        <a href="/link1">Link 1</a>
        <img src="/image1.jpg" alt="Image 1">
        </body></html>'''
        actual = extract_page_data(input_body, input_url)
        expected = {
        "url": "https://blog.boot.dev",
        "h1": "Test Title",
        "first_paragraph": "This is the first paragraph.",
        "outgoing_links": ["https://blog.boot.dev/link1"],
        "image_urls": ["https://blog.boot.dev/image1.jpg"]
        }
        self.assertEqual(actual, expected)
    
    def testNoAnchors(self):
        input_url = "https://blog.boot.dev"
        input_body = '''<html><body>
        <h1>Test Title</h1>
        <p>This is the first paragraph.</p>
        <img src="/image1.jpg" alt="Image 1">
        </body></html>'''
        actual = extract_page_data(input_body, input_url)
        expected = {
        "url": "https://blog.boot.dev",
        "h1": "Test Title",
        "first_paragraph": "This is the first paragraph.",
        "outgoing_links": [],
        "image_urls": ["https://blog.boot.dev/image1.jpg"]
        }
        self.assertEqual(actual, expected)

    def testNoImages(self):
        input_url = "https://blog.boot.dev"
        input_body = '''<html><body>
        <h1>Test Title</h1>
        <p>This is the first paragraph.</p>
        <a href="/link1">Link 1</a>
        '''
        actual = extract_page_data(input_body, input_url)
        expected = {
        "url": "https://blog.boot.dev",
        "h1": "Test Title",
        "first_paragraph": "This is the first paragraph.",
        "outgoing_links": ["https://blog.boot.dev/link1"],
        "image_urls": []
        }
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()