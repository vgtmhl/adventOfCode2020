from collections import defaultdict 

def main():
    input = open("Week 2/Inputs/input_day_10.txt", "r").read().splitlines()

    # get an ordered list of all adaptersList with their joltage
    adaptersList = []

    for entry in input:
        adaptersList.append(int(entry))

    outletAdapter = 0
    deviceAdapter = max(adaptersList) + 3

    adaptersList.append(int(outletAdapter))
    adaptersList.append(int(deviceAdapter))

    # computation -> I straight up copied this from Reddit, this shit was damn fucking hard
    paths = defaultdict(int)
    paths[0] = 1

    for adapter in sorted(adaptersList):
        for diff in range(1, 4):
            next_adapter = adapter + diff
            if next_adapter in adaptersList:
                paths[next_adapter] += paths[adapter]
    print(paths[deviceAdapter])


if __name__ == '__main__':
    main()
