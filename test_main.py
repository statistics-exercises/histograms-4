import unittest
import scipy.stats as st
from main import *

class UnitTests(unittest.TestCase) :
    def test_variable(self):
        myexp, myvar = 0, 0 
        for i in range(5) : 
           myexp = myexp + probs[i]*i
           myvar = myvar + probs[i]*i*i
        myvar = myvar - myexp

        mean = 0
        for i in range(100) : mean = mean + myvariable( probs )
        mean = mean  / 100 

        bar = np.sqrt(myvar/100)*st.norm.ppf( (0.99 + 1) / 2 ) 
        self.assertTrue( np.fabs( mean - myexp )<bar, "your function appears to be sampling from the wrong distribution" )
