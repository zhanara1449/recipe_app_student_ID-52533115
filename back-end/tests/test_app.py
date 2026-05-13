import unittest
from app import app

class FlaskTestCase(unittest.TestCase):


    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    
    def test_homepage(self):

        response = self.app.get('/')

        self.assertEqual(response.status_code, 200)

    def test_search_page(self):

        response = self.app.get('/search')

        self.assertEqual(response.status_code, 200)

    def test_recipe_detail(self):

        response = self.app.get('/recipe/1')

        self.assertEqual(response.status_code, 200)


    
    def test_recipe_detail1(self):

        response = self.app.get('/recipe/567')

        self.assertEqual(response.status_code, 200)


  
    def test_stats_page(self):

        response = self.app.get('/stats')

        self.assertEqual(response.status_code, 200)


    def test_cuisine_page(self):

        response = self.app.get('/cuisine/Italian')

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()