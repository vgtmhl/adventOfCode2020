def main():
    lines = open("Week 1/Inputs/input_day_3.txt", "r").read().splitlines()
    treesForSlopes = [0, 0, 0, 0, 0]
    totalTrees = 1

    treesForSlopes[0] = collisionsForSlope(lines, 1, 1)
    treesForSlopes[1] = collisionsForSlope(lines, 3, 1)
    treesForSlopes[2] = collisionsForSlope(lines, 5, 1)
    treesForSlopes[3] = collisionsForSlope(lines, 7, 1)
    treesForSlopes[4] = collisionsForSlope(lines, 1, 2)

    for n in treesForSlopes:
        totalTrees = totalTrees * n

    print(totalTrees)


def collisionsForSlope(lines, right, down):
    lineLen = len(lines[0])
    collisions = 0
    index = 0

    for i in range(0, len(lines), down):
        if i == 0:
            index = 0
        else:
            index = index+right if (index+right <
                                    lineLen) else (index+right - lineLen)

        if lines[i][index] == '#':
            collisions += 1

    return collisions


if __name__ == '__main__':
    main()
