import unittest
import calories

class TestCalorie(unittest.TestCase):
    def tes_calories_burned(self):
        result = calories.calories_burned(duration = 15, exercise= "berlari")
        self.assertEqual(result,100)

if __name__ == '__main__':
    unittest.main()