import unittest
import calorie

class TestCalorie(unittest.TestCase):
    def tes_calories_burned(self):
        result = calorie.total_session_burned_cal('berenang', 'bersepeda', each_session_duration=10)
        self.assertEqual(result,200)

if __name__ == '__main__':
    unittest.main()