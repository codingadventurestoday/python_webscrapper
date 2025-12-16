import unittest

from scrap_code.scrap_website import get_first_paragraph_from_html
from scrap_code.scrap_website import get_h1_from_html

class testGetH1(unittest.TestCase):
    def test_get_h1_from_html_basic(self):
        input_body = '<html><body><h1>Test Title</h1></body></html>'
        actual = get_h1_from_html(input_body)
        expected = "Test Title"
        self.assertEqual(actual, expected)

    def test_get_first_paragraph_from_html_main_priority(self):
        input_body = '''<html><body>
            <p>Outside paragraph.</p>
            <main>
                <p>Main paragraph.</p>
            </main>
        </body></html>'''
        actual = get_first_paragraph_from_html(input_body)
        expected = "Main paragraph."
        self.assertEqual(actual, expected)

    def test_no_main_get_first_paragraph(self):
        input_body = '''<html><body>
                <p>Just happy to be here</p>
            </body></html>'''
        actual = get_first_paragraph_from_html(input_body)
        expected = 'Just happy to be here'
        self.assertEqual(actual, expected)





if __name__ == '__main__':
    unittest.main()