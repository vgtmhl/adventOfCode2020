
ins = []


def main():
    input = open("Week 2/Inputs/input_day_8.txt", "r").read().splitlines()

    for line in input:
        instruction, value = line.split(' ')
        ins.append(Instruction(instruction, value))

    for instr in ins:
        if instr.instruction == "jmp" or instr.instruction == "nop":
            instr.swap()
            ans = findSolution()

            if ans == 0:
                instr.swap()

                for instr in ins:
                    instr.dirty = False
                    
            else:
                print(ans)
                return 


def findSolution():
    accumulator = 0
    i = 0

    while i <= len(ins):

        if i == len(ins):
            return accumulator

        if ins[i].dirty:
            return 0
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
    swapped = 0  # 0 = not swapped, 1 = swapped, 2 = swapped back in place

    def swap(self):
        if self.instruction == "jmp":
            self.instruction = "nop"
        elif self.instruction == "nop":
            self.instruction = "jmp"

        self.swapped += 1

    def __init__(self, instruction, value):
        self.instruction = instruction
        self.value = value
        self.dirty = False


if __name__ == '__main__':
    main()
