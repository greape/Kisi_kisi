import unittest
import calories

class Test(unittest.TestCase):
    def test_0_calculateTotal(self):
        self.assertEqual(calories.calories_burned(duration=15, exercise='bersepeda'), 120)

if __name__ == '__main__':
    unittest.main()