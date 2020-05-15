import unittest
import copy

DIRECTIONS = {
        0: 'NORTE',
        1: 'LESTE',
        2: 'SUL',
        3: 'OESTE'
    }

class Submarino(object):
    x = 0
    y = 0
    z = 0
    direction = 0
    initial_state = {
            'x': 0,
            'y': 0,
            'z': 0,
            'direction': 0
        }
    current_state = {}

    def navigate(self, coordinates):
        current_state = copy.copy(self.initial_state)
        for i, operation in enumerate(coordinates):
            if operation == 'L':
                current_state['direction'] -= 1

                if current_state['direction'] == -1:
                    current_state['direction'] = 3

            elif operation == 'R':
                current_state['direction'] += 1

                if current_state['direction'] == 4:
                    current_state['direction'] = 0

            elif operation == 'M':
                if current_state['direction'] == 0:
                    current_state['y'] += 1
                elif current_state['direction'] == 1:
                    current_state['x'] += 1
                elif current_state['direction'] == 2:
                    current_state['y'] -= 1
                elif current_state['direction'] == 3:
                    current_state['x'] -= 1

            elif operation == 'U':
                current_state['z'] += 1

            elif operation == 'D':
                current_state['z'] -= 1

        result = []
        result.append(str(current_state['x']))
        result.append(str(current_state['y']))
        result.append(str(current_state['z']))
        result.append(DIRECTIONS[current_state['direction']])

        return ' '.join(result)

class SubmarinoTest(unittest.TestCase):

    def testFoo(self):
        sub = Submarino()
        self.assertEqual(1,1)

    def testNavigate(self):
        sub = Submarino()
        coordinates = sub.navigate('LL')
        self.assertEqual('0 0 0 SUL', coordinates)

if __name__ == '__main__':
    unittest.main()