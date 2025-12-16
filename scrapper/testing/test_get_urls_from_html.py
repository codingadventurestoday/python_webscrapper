import unittest

from scrap_code.scrap_website import get_urls_from_html, get_images_from_html

class testGetUrlsFromHtml(unittest.TestCase):
    def test_get_urls_from_html_absolute(self):
        input_url = "https://blog.boot.dev"
        input_body = '<html><body><a href="https://blog.boot.dev"><span>Boot.dev</span></a></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev"]
        self.assertEqual(actual, expected)
    
    def testNoAnchors(self):
        input_url = 'https://blog.boot.dev'
        input_body = '<html><body><p>This is a paragraph with no links or images.</p></body></html>'
        actual = get_urls_from_html(input_body, input_url)
        expected = []
        self.assertEqual(actual, expected)

    def testGetMultipleAnchors(self):
        input_url = 'https://boot.dev'
        input_body = '''
<html>
    <body>
        <p>Welcome to the site</p>
        <a href="/contact">Contact Us</a>
        <img src="logo.png" alt="Company Logo">
        <div>
            <a href="https://boot.dev/blog">Read Blog</a>
            <img src="/images/banner.jpg" alt="Banner">
        </div>
    </body>
</html>
'''
        actual = get_urls_from_html(input_body, input_url)
        expected = ['https://boot.dev/contact', 'https://boot.dev/blog']
        self.assertEqual(actual, expected)


class testGetImages(unittest.TestCase):
    def test_get_images_from_html_relative(self):
        input_url = "https://blog.boot.dev"
        input_body = '<html><body><img src="/logo.png" alt="Logo"></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = ["https://blog.boot.dev/logo.png"]
        self.assertEqual(actual, expected)
    
    def testNoImg(self):
        input_url = 'https://blog.boot.dev'
        input_body = '<html><body><p>This is a paragraph with no links or images.</p></body></html>'
        actual = get_images_from_html(input_body, input_url)
        expected = []
        self.assertEqual(actual, expected)

    def test(self):
        input_url = 'https://blog.boot.dev'
        input_body = '''
<html>
    <body>
        <p>Welcome to the site</p>
        <a href="/contact">Contact Us</a>
        <img src="logo.png" alt="Company Logo">
        <div>
            <a href="https://boot.dev/blog">Read Blog</a>
            <img src="/images/banner.jpg" alt="Banner">
        </div>
    </body>
</html>
'''
        actual = get_images_from_html(input_body, input_url)
        expected = ['https://blog.boot.dev/logo.png', 
                    'https://blog.boot.dev/images/banner.jpg']
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()