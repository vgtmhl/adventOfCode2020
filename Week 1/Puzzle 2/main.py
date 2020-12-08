def main():
    inputFile = open("Week 1/Inputs/input_day_1.txt", "r").read().splitlines()
    arr = [line for line in inputFile]

    # this clusterfuck reduces execution time from 1.1s to 0.3s over
    # plain nested iteration
    arr.sort()
    firstCeiling = int(max(arr)) * 2
    arrLen = len(arr)

    for i in range(0, arrLen):
        for j in range(i, arrLen):
            if int(arr[j]) > firstCeiling:
                continue
            secondCeiling = 2020 - (int(arr[i]) + int(arr[j]))
            for k in range(j, arrLen):
                if int(arr[k]) > secondCeiling:
                    continue
                if int(arr[i]) + int(arr[j]) + int(arr[k]) == 2020:
                    print(int(arr[i])*int(arr[j])*int(arr[k]))


if __name__ == '__main__':
    main()
