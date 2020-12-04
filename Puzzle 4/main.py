def main():
    inputFile = open("Inputs/input_day_2.txt", "r").read().splitlines()
    hits = 0

    for line in inputFile:
        pos1, pos2 = line.split(' ')[0].split('-')
        letter = line.split(' ')[1].replace(':', '')
        password = line.split(':')[1].strip()

        if (password[int(pos1)-1] == letter) ^ (password[int(pos2)-1] == letter):
            hits += 1

    print(hits)


if __name__ == '__main__':
    main()
