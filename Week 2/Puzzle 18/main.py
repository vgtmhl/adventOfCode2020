RULE_KEY = 1398413738


def main():
    input = open("Week 2/Inputs/input_day_9.txt", "r").read().splitlines()

    i = 0
    j = 0

    while(i < len(input)):
        addendi = []
        addendi.append(int(input[i]))
        setResult = int(input[i])
        j = i+1

        while (j < len(input)):
            addendi.append(int(input[j]))
            setResult += int(input[j])

            if setResult == RULE_KEY:
                print(f'found key: {setResult}')
                print(f'encryption key: {min(addendi) + max(addendi)}')
                return

            j += 1

        i += 1

    print('nothing found')


if __name__ == '__main__':
    main()
