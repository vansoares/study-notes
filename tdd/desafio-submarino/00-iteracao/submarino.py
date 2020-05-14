import copy

def navigate(coordinates):
    DIRECTIONS = {
        0: 'NORTE',
        1: 'LESTE',
        2: 'SUL',
        3: 'OESTE'
    }

    initial_state = {
        'x': 0,
        'y': 0,
        'z': 0,
        'direction': 0
    }
    current_state = copy.copy(initial_state)
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

    result = current_state
    result['direction'] = DIRECTIONS[current_state['direction']]
    return result

if __name__ == '__main__':
    coordinates = input()
    print(navigate(coordinates))