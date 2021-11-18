import unittest

class TestMyProgram(unittest.TestCase):

    def test_sum(*args):
        sum: float or int = 0
        if 0 in args:
            raise ValueError('Invalid length')
        elif type(args) is not float or int:
            raise ValueError('Invalid type for argument')
        sum += args
        return sum

if __name__ == '__main__':
    unittest.main()
