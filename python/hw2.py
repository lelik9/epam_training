import sys
try:
    from Tools.scripts.treesync import raw_input
except ImportError:
    pass

top = {
    'F': ['T', 'R', 'B', 'L'],
    'BC': ['T', 'L', 'B', 'R'],
    'T': ['F', 'R', 'BC', 'L'],
    'B': ['F', 'L', 'BC', 'R'],
    'L': ['F', 'B', 'BC', 'T'],
    'R': ['F', 'T', 'BC', 'B'],
       }


def cube_rubiq(sides, turns):
    for turn in turns:
        if turn in sides:
            for s_index, s in enumerate(sides):
                if turn != s:
                    side_index = top[turn].index(s)

                    try:
                        sides[s_index] = top[turn][side_index+1]
                    except IndexError:
                        sides[s_index] = top[turn][0]
    return sides


if __name__ == '__main__':
    sides = raw_input("Cube side: ").replace('\n', '').upper().split(',')
    turns = raw_input("Turns: ").replace('\n', '').split(',')

    if len(turns) > 70:
        print('Too many turns')
        sys.exit(1)

    print(cube_rubiq(sides, turns))
