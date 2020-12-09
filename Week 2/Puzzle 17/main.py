PREAMBLE_SIZE = 25


def main():
    input = open("Week 2/Inputs/input_day_9.txt", "r").read().splitlines()
    buffer = []

    i = 0
    while(i < len(input)):

        # first iteration
        if i == 0:
            buffer = input[0:PREAMBLE_SIZE]
            i += PREAMBLE_SIZE
            continue

        # after the first buffer is formed
        elif i > PREAMBLE_SIZE:
            buffer = input[i-PREAMBLE_SIZE: i]
            value = input[i]
            if not isAdditiveCombination(buffer, value):
                print(f'{value} breaks the rule')
                return

        # loop increment
        i += 1


# Optimizable: returns true if value is the result of the sum of any 2 values from the buffer
def isAdditiveCombination(buffer, value):
    for a in buffer:
        for b in buffer:
            if int(a) + int(b) == int(value):
                print(f'{value} is the result of {a} + {b}')
                return True

    return False


if __name__ == '__main__':
    main()
