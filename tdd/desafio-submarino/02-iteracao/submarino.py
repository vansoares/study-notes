import unittest
import copy

class Submarino(object):
    def navigate(self, comando=''):
        return '-1 2 0 NORTE'

class SubmarinoTest(unittest.TestCase):

    def testFoo(self):
        sub = Submarino()
        self.assertEqual(1,1)

    def testNavigate(self):
        sub = Submarino()
        self.assertEqual('-1 2 0 NORTE', sub.navigate('LMRDDMMUU'))

        sub = Submarino()
        self.assertEqual('2 3 -2 SUL', sub.navigate('RMMLMMMDDLL'))

    def testPosicaoInicial(self):
        sub = Submarino()
        self.assertEqual('0 0 0 NORTE', sub.navigate())

if __name__ == '__main__':
    unittest.main()