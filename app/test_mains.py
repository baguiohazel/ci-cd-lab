import unittest 
from app.main import add

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(6, 3), 9) 

if __name__ == "__main__":
    unittest.main()
