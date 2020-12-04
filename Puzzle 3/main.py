def main():
    inputFile = open("Inputs/input_day_2.txt", "r").read().splitlines()
    hits = 0

    for line in inputFile:
        min, max = line.split(' ')[0].split('-')
        letter = line.split(' ')[1].replace(':', '')
        password = line.split(':')[1].strip()

        times = password.count(letter)
        if (times >= int(min) and times <= int(max)):
            hits += 1

    print(hits)


if __name__ == '__main__':
    main()
