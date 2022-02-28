from src.cal import avg_return
from src.Classes.Stocks import stock
import unittest

class TestAvgReturn(unittest.TestCase):
    def test_avg_return(self):
        s1 = stock("FB",0.45)
        s2 = stock("AAPL",0.30)
        s3 = stock("AMZN",0.90)
        s4 = stock("NFLX",0.6)
        s5 = stock("GOOGL",0.35)
        stocks = [s1,s2,s3,s4,s5]
        exepcted = 0.52
        actual = round(avg_return(stocks),2)
        self.assertEqual(exepcted,actual)
