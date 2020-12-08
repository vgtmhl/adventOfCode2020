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

    for key in rules:
        if eventuallyContainsGold(key):
            result.append(key)

    if "shinygold" in result:
        print(len(result) - 1)
    else:
        print(len(result))


def eventuallyContainsGold(bagType):
    if bagType == "shinygold":
        return True

    for bagType in rules[bagType]:
        if eventuallyContainsGold(bagType):
            return True

    return False


if __name__ == '__main__':
    main()
