def main():
    input = open("Week 2/Inputs/input_day_10.txt", "r").read().splitlines()
    adaptersList = []
    oneJoltCounter = 0
    threeJoltsCounter = 1

    for entry in input:
        adaptersList.append(int(entry))

    adaptersList.sort()

    for i in range(1, len(adaptersList)):
        current = adaptersList[i]
        previous = adaptersList[i-1]

        if current == (previous + 1):
            oneJoltCounter += 1

        elif current == (previous + 3):
            threeJoltsCounter += 1

    if min(adaptersList) == 1:
        oneJoltCounter += 1

    print(f'{oneJoltCounter} 1-jolt differences and {threeJoltsCounter} 3-jolt differences')
    print(f'therefore, the solution is {oneJoltCounter * threeJoltsCounter}')


if __name__ == '__main__':
    main()
