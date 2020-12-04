import re


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
            print(f'{validPassports}: {passport}')

    # print outcome
    print('\n' + str(validPassports))


def isValidPassport(passport):

    mandatoryFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if not all(key in passport for key in mandatoryFields):
        return False

    # passport is valid if it contains all of these values
    birthdate = passport.get("byr")
    issueYear = passport.get("iyr")
    expirationYear = passport.get("eyr")
    height = passport.get("hgt")
    hairColor = passport.get("hcl")
    eyeColor = passport.get("ecl")
    passportId = passport.get("pid")

    # slightly more complex validation for height, so Itake care of it separately
    heightValue = int(re.findall(r'\d+', height)[0])
    heightMu = ''

    if "in" in height:
        heightMu = "in"
    elif "cm" in height:
        heightMu = "cm"
    else:
        return False

    if heightMu == "in":
        if heightValue < 59 or heightValue > 76:
            return False

    if heightMu == "cm":
        if heightValue < 150 or heightValue > 193:
            return False

    # rest of the validation is simpler so it can be handled in batch
    return(
        len(birthdate) == 4 and int(
            birthdate) >= 1920 and int(birthdate) <= 2002
        and
        len(issueYear) == 4 and int(
            issueYear) >= 2010 and int(issueYear) <= 2020
        and
        len(expirationYear) == 4 and int(
            expirationYear) >= 2020 and int(expirationYear) <= 2030
        and
        re.match(r'#[0-9a-f]{6}', hairColor)
        and
        eyeColor in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        and
        re.match(r'[0-9]{9}', passportId)
    )


if __name__ == '__main__':
    main()
