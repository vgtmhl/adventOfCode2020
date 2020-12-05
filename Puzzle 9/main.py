totalRows = 128
totalCols = 8


def main():

    lines = open("Inputs/input_day_5.txt", "r").read().splitlines()
    highestSeatID = 0

    for line in lines:
        rowData = line[0:7]
        colData = line[7:10]

        row = calculateRow(rowData)
        col = calculateCol(colData)

        seatID = getSeatID(row, col)

        if seatID > highestSeatID:
            highestSeatID = seatID

    print(highestSeatID)


def calculateRow(rowData):
    row = 0

    for i in range(0, len(rowData)):

        if rowData[i] == "B":
            addendum = totalRows / (2**(i+1))
            row += addendum

    return row


def calculateCol(colData):
    col = 0

    for i in range(0, len(colData)):

        if colData[i] == "R":
            addendum = totalCols / (2**(i+1))
            col += addendum

    return col


def getSeatID(row, col):
    return row * 8 + col


if __name__ == '__main__':
    main()
