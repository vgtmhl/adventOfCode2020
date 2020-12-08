from os import getcwd


rules = {}
result = []


def main():
    inputFile = open("Week 2/Inputs/input_day_7.txt", "r").read().splitlines()

    for line in inputFile:
        arr = line.split()
        container = arr[0] + arr[1]
        contentDict = {}

        for i in range(4, len(arr)-2):
            if arr[i] == "no":
                rules[container] = {}
                break

            if i % 4 == 0:
                contentValue = arr[i]
                contentKey = arr[i+1] + arr[i+2]

                contentDict[contentKey] = contentValue
                rules[container] = contentDict

    print(getContentFor("shinygold") - 1)


def getContentFor(bagType):
    accumulator = 1

    if not rules[bagType]:
        return 1

    for key, value in rules[bagType].items():
        accumulator += int(value) * int(getContentFor(key))

    return accumulator


if __name__ == '__main__':
    main()
