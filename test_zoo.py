import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()
    
    def testErr(self):
        self.assertEqual(self.zoo.get_ticket_price(-1),"err")
    
    def testNobirth(self):
        self.assertEqual(self.zoo.get_ticket_price(0),50)

    def testChild(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
       
    def testTeen(self):
        self.assertEqual(self.zoo.get_ticket_price(13),100)
    
    def testAdultTicket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21),150)

    def testOldPrice(self):
        self.assertEqual(self.zoo.get_ticket_price(70),100)
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()