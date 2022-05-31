import unittest

from chapter15_4 import Die


class TestDieClass(unittest.TestCase):


    def test_Die_num_sides(self):

        d6 = Die()
        d10 = Die(10)
        self.assertEqual(6,d6.num_sides,msg="骰子面数初始化错误")
        self.assertEqual(10,d10.num_sides,msg="骰子面数初始化错误")

    def test_Die_roll(self):

        d6 = Die()

        randnum = d6.roll()
        self.assertTrue(6>=randnum>=1,msg="骰子投掷出了超出范围的数字")


if __name__ == "__main__":
    unittest.main()