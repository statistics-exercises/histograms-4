try:
    from AutoFeedback.funcchecks import check_func 
except:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "AutoFeedback"])
    from AutoFeedback.funcchecks import check_func

from AutoFeedback.varchecks import check_vars
from AutoFeedback.randomclass import randomvar
import unittest
from main import *

class helper : 
    def check_mean( n, probs ) :
        m = 0
        for i in range(n) : m = m + myvariable( probs ) 
        return m / n

myvars = np.array([0,1,2,3,4])
exp = np.dot( probs, myvars )
var = np.dot( probs, myvars*myvars ) - exp*exp

class UnitTests(unittest.TestCase) :
    def test_variable(self) : 
       inputs, variables = [], []
       for i in range(10): 
           inputs.append((probs,))
           myvar = randomvar( exp, variance=var, vmin=0, vmax=4, isinteger=True )
           variables.append( myvar )

       assert( check_func("myvariable", inputs, variables ) )

    def test_mean(self) : 
       inputs, variables = [], []
       for i in range(5):  
           nmean = (i+1)*10
           inputs.append((nmean,probs,))
           myvar = randomvar( exp, variance=var/nmean, vmin=0, vmax=4, isinteger=False )
           variables.append( myvar )

       assert( check_func("check_mean", inputs, variables, modname=helper ) )
