# -*- encoding:utf-8 -*-
# 给出两个整数a和b, 求他们的和, 但不能使用 + 等数学运算符。
import unittest

def addd(x, y):
    if y==0:
            return x
    # 按位运算，x^y 得到二者相异互补的结果
    x1=x^y
    # x&y 得到需要进位的坐标，y1<<得到进位的数值
    y1=x&y
    return addd(x1, y1<<1)


class mytest(unittest.TestCase): 
  
  def setUp(self): 
    pass
  
  def tearDown(self): 
    pass
  
  def test_add1(self): 
    self.assertEqual(addd(3, 5), 8, 'test 3+5 fail') 
  def test_add2(self): 
    self.assertEqual(addd(23, 34), 57, 'test 23+34 fail') 


if __name__ =='__main__': 
  unittest.main()
