import unittest

DIRECTIONS = {
        0: 'NORTE',
        1: 'LESTE',
        2: 'SUL',
        3: 'OESTE'
    }

class Submarino(object):
    direction = 0
    x = 0
    y = 0
    z = 0

    def navigate(self, coordinates):
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

        result = []
        result.append(str(self.x))
        result.append(str(self.y))
        result.append(str(z))
        result.append(DIRECTIONS[self.direction])

        return ' '.join(result)
    
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

class SubmarinoTest(unittest.TestCase):

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

if __name__ == '__main__':
    unittest.main()