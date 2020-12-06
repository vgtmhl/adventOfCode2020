def main():
    inputFile = open("Inputs/input_day_6.txt", "r").read().splitlines()
    groupEntry = ''
    groupEntries = []
    totalAnswered = 0

    # manipulate so that results from the same group are on one line only
    for line in inputFile:
        if line:
            groupEntry += (line + ' ')
        else:
            groupEntries.append(groupEntry)
            groupEntry = ''

    if groupEntry:
        groupEntries.append(groupEntry)


    for entry in groupEntries:
        people = entry.count(' ')
        for ans in list(set(entry.replace(' ', ''))):
            if entry.count(ans) == people:
                totalAnswered += 1
            

    print(totalAnswered)


if __name__ == '__main__':
    main()
