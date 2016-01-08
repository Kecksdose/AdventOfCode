# import cmath


with open('data.txt', 'r') as f:
    directions = f.read()
    visited_homes = [complex(0, 0)]
    current_position = complex(0, 0)
    for direction in directions:
        if direction is ">":
            current_position += complex(1, 0)
        elif direction is "<":
            current_position += complex(-1, 0)
        elif direction is "^":
            current_position += complex(0, 1)
        elif direction is "v":
            current_position += complex(0, -1)
        if current_position not in visited_homes:
            visited_homes.append(current_position)

    print len(visited_homes)
