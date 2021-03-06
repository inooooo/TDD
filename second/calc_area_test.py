import unittest
from calc_area import calc_area,all_method, to_float

class Test_calc_area(unittest.TestCase):

    def test_calc_area(self):
        self.assertEqual(3, calc_area(1))
        self.assertEqual(196350, calc_area(250))
        self.assertEqual(0, calc_area(0))
        self.assertEqual(31416, calc_area(100))
        self.assertEqual(7, calc_area(1.5))
        self.assertEqual(314159265, calc_area(10000))
        self.assertTrue(isinstance(calc_area(1.5), int))

    def test_all_method(self):
        io = IO_mock()
        all_method(io)
        self.assertEqual([314,196350,31416,7],io.result)

    def test_to_float(self):
        self.assertEqual([10.0, 250.0, 100.0, 1.5], to_float(["10\n", "250\n", "100\n", "1.5\n"]))

class IO_mock:
    def input_data(self):
        return [10,250,100,1.5]

    def output_data(self,result):
        self.result = result

if __name__ == '__main__':
	unittest.main()
