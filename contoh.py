import unittest

class TestCalorie(unittest.TestCase):
    def tes_calories_burned(self):
        result = calories_burned(10, "berlari")
        self.assertEqual(result,100)

if __name__ == '__main__':
    unittest.main()