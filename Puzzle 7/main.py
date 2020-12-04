def main():
    input = open("Inputs/input_day_4.txt", "r").read().splitlines()
    
    # needed variables declaration
    validPassports = 0
    passportString = ''
    passportStrings = []
    passportDict = {}
    passportDicts = []

    # manipulate so that each passport entry data is in one line
    for line in input:
        if line:
            passportString += (line + ' ')
        else:
            passportStrings.append(passportString)
            passportString = ''

    # for each passport entry
    for string in passportStrings:
        pairs = string.split(' ')

        # for each string entry, make it a dict
        for pair in pairs:
            if pair:
                key, value = pair.split(':')
                passportDict[key] = value

        # append the dict to a list of dictionaries
        passportDicts.append(passportDict)
        passportDict = {}

    # for each dictionary represting a passport, validate it
    for passport in passportDicts:
        if isValidPassport(passport):
            validPassports += 1

    # print outcome
    print(validPassports)


def isValidPassport(passport):
    # passport is valid if it contains all of these values
    mandatoryFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    return all(key in passport for key in mandatoryFields)


if __name__ == '__main__':
    main()
