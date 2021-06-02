import math
import unittest
import random

def wallis(n):
    value = 1
    for i in range(1,n+1):
        value = value*4*pow(i,2)/(4*(pow(i,2)) - 1)
    return 2*value

def monte_carlo(n):
    num=0
    den=0
    ratio=0
    for i in range(0,n):
        a = random.random()
        b = random.random()
        d = pow(pow(a,2) + pow(b,2) , 0.5)
        if(d<=1):
            num +=1
            den += 1
        else:
            den += 1
    ratio = float(num/den)
    return 4*ratio

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
