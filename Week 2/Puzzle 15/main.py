

def main():
    input = open("Week 2/Inputs/input_day_8.txt", "r").read().splitlines()
    ins = []

    for line in input:
        instruction, value = line.split(' ')
        ins.append(Instruction(instruction, value))

    accumulator = 0
    i = 0

    while i < len(ins):

        if ins[i].dirty:
            print(accumulator)
            return
        else:
            ins[i].dirty = True

        if ins[i].instruction == "jmp":
            i += int(ins[i].value)

        elif ins[i].instruction == "acc":
            accumulator += int(ins[i].value)
            i += 1

        elif ins[i].instruction == "nop":
            i += 1



class Instruction():
    instruction = ''
    value = ''
    dirty = False

    def __init__(self, instruction, value):
        self.instruction = instruction
        self.value = value
        self.dirty = False


if __name__ == '__main__':
    main()
