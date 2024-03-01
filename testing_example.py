import unittest

def add(x, y):
    return x + y

class TestAddFunction(unittest.TestCase):
    
    def test_add_positive_numbers(self):
        result = add(3, 6)
        self.assertEqual(result, 9)
        


    def test_add_negative_numbers(self):
        result = add(-4, -8)
        self.assertEqual(result, -12)

    def test_add_negative_positive_numbers(self):
        result = add(4, -11)
        self.assertEqual(result, -7)


if __name__ == "__main__":
    unittest.main()