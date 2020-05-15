import unittest

DIRECTIONS = {
        0: 'NORTE',
        1: 'LESTE',
        2: 'SUL',
        3: 'OESTE'
    }

class Submarino(object):

    def __init__(self):
        self.direction = 0
        self.x = 0
        self.y = 0
        self.z = 0

    def navigate(self, coordinates=''):
        for i, operation in enumerate(coordinates):
            if operation == 'L':
                self.left()

            elif operation == 'R':
                self.right()

            elif operation == 'M':
                self.move()

            elif operation == 'U':
                self.up()

            elif operation == 'D':
                self.down()

        return f'{self.x} {self.y} {self.z} {DIRECTIONS[self.direction]}'
    
    def left(self):
        self.direction -= 1

        if self.direction == -1:
            self.direction = 3
        
        return self.direction

    def right(self):
        self.direction += 1

        if self.direction == 4:
            self.direction = 0
        return self.direction

    def up(self):
        self.z += 1
        if self.z > 0:
            self.z = 0
        return self.z

    def down(self):
        self.z -= 1
        return self.z

    def move(self):
        if self.direction == 0:
            self.y += 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y -= 1
        elif self.direction == 3:
            self.x -= 1


class SubmarinoTest(unittest.TestCase):

    def testNavigate(self):
        sub = Submarino()
        self.assertEqual('-1 2 0 NORTE', sub.navigate('LMRDDMMUU'))

        sub = Submarino()
        self.assertEqual('2 3 -2 SUL', sub.navigate('RMMLMMMDDLL'))

    def testPosicaoInicial(self):
        sub = Submarino()
        self.assertEqual('0 0 0 NORTE', sub.navigate())


    def testPosicionamento(self):
        sub = Submarino()
        self.assertEqual(0, sub.direction)
        self.assertEqual(3, sub.left())
        self.assertEqual(0, sub.right())
        self.assertEqual(1, sub.right())
        self.assertEqual(2, sub.right())

    def testProfundidade(self):
        sub = Submarino()
        self.assertEqual(0, sub.z)
        self.assertEqual(-1, sub.down())
        self.assertEqual(-2, sub.down())
        self.assertEqual(-3, sub.down())
        self.assertEqual(-2, sub.up())
        self.assertEqual(-1, sub.up())
        self.assertEqual(0, sub.up())
        self.assertEqual(0, sub.up())

    ## Quando foi movimentar para o norte, add +1 no y
    def testMovimentandoParaNorte(self):
        sub = Submarino()
        sub.direction = 0

        sub.move()
        self.assertEqual(0, sub.x)
        self.assertEqual(1, sub.y)

        sub.move()
        self.assertEqual(0, sub.x)
        self.assertEqual(2, sub.y)

        sub.move()
        self.assertEqual(0, sub.x)
        self.assertEqual(3, sub.y)


    ## Quando foi movimentar para o sul, subtrai 1 no y
    def testMovimentandoParaSul(self):
        sub = Submarino()
        sub.direction = 2

        sub.move()
        self.assertEqual(0, sub.x)
        self.assertEqual(-1, sub.y)

        sub.move()
        self.assertEqual(0, sub.x)
        self.assertEqual(-2, sub.y)

        sub.move()
        self.assertEqual(0, sub.x)
        self.assertEqual(-3, sub.y)

    ## Quando foi movimentar para o leste, add +1 no x
    def testMovimentandoParaLeste(self):
        sub = Submarino()
        sub.direction = 1

        sub.move()
        self.assertEqual(0, sub.y)
        self.assertEqual(1, sub.x)

        sub.move()
        self.assertEqual(0, sub.y)
        self.assertEqual(2, sub.x)

        sub.move()
        self.assertEqual(0, sub.y)
        self.assertEqual(3, sub.x)

    ## Quando foi movimentar para o oeste, subtrai 1 no x
    def testMovimentandoParaOeste(self):
        sub = Submarino()
        sub.direction = 3

        sub.move()
        self.assertEqual(0, sub.y)
        self.assertEqual(-1, sub.x)

        sub.move()
        self.assertEqual(0, sub.y)
        self.assertEqual(-2, sub.x)

        sub.move()
        self.assertEqual(0, sub.y)
        self.assertEqual(-3, sub.x)

if __name__ == '__main__':
    unittest.main()