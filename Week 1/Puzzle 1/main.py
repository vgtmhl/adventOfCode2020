def main():

    inputFile = open("Week 1/Inputs/input_day_1.txt", "r").read().splitlines()
    arr = [line for line in inputFile]
    arr.sort()

    # execution time halved compared to plain nested iteration
    for i in range(0, len(arr)):
        ceiling = 2020 - int(arr[i])
        for j in range(i, len(arr)):
            if int(arr[j]) > ceiling:
                continue
            if int(arr[i]) + int(arr[j]) == 2020:
                print(int(arr[i]) * int(arr[j]))


if __name__ == '__main__':
    main()
