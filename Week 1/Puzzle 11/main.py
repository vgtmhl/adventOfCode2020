def main():
    inputFile = open("Week 1/Inputs/input_day_6.txt", "r").read().splitlines()
    groupEntry = ''
    groupEntries = []
    totalAnswered = 0

    # manipulate so that results from the same group are on one line only
    for line in inputFile:
        if line:
            groupEntry += line
        else:
            groupEntries.append(groupEntry)
            groupEntry = ''

    # for last line
    if groupEntry:
        groupEntries.append(groupEntry)

    # remove duplicates and add value to counter
    for entry in groupEntries:
        entry = list(set(entry))
        totalAnswered += len(entry)


if __name__ == '__main__':
    main()
