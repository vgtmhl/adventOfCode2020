def main():
    lines = open("Inputs/input_day_3.txt", "r").read().splitlines()
    lineLen = len(lines[0])
    trees = 0
    index = 0

    for i in range(0, len(lines)):
        if i == 0:
            index = 0
        else:
            index = index+3 if (index+3 < lineLen) else (index+3 - lineLen)

        if lines[i][index] == '#':
            trees += 1

    print(trees)


if __name__ == '__main__':
    main()
