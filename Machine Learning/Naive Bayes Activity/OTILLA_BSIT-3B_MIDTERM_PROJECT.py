import csv
import matplotlib.pyplot as plt


def process(mushroomsRow, mushroomsCol, poiCount, ediCount):
    for row in mushroomsRow:
        for i in range(23):
            if not any(dat[0] == row[i] for dat in mushroomsCol[i][1]):
                if i != 22:
                    mushroomsCol[i][1].append([row[i], 0, 0, 0])

            for dat in mushroomsCol[i][1]:
                if dat[0] == row[i]:
                    dat[1] = dat[1] + 1
                    if i != 22:
                        if row[22] == 'poisonous':
                            dat[3] = dat[3] + 1
                        if row[22] == 'edible':
                            dat[2] = dat[2] + 1
                    break


def count(mushroomsRow, mushroomsCol, poiCount, ediCount):
    for row in mushroomsRow:
        if row[len(mushroomsCol) - 1] == 'poisonous':
            poiCount += 1
        elif row[len(mushroomsCol) - 1] == 'edible':
            ediCount += 1
    return poiCount, ediCount


def computation(mushroomsCol, input, type, class_count, size):
    pmc = 1

    for i in range(len(input)):
        for dat in mushroomsCol[i][1]:
            if dat[0] == input[i]:
                if type == 'poisonous':
                    pmc = pmc * (int(dat[3]) / int(class_count))
                elif type == 'edible':
                    pmc = pmc * (int(dat[2]) / int(class_count))

                break

    p = (pmc * class_count) / size
    return p


def visualization(mushroomsCol, ediResult, poiResult, input):
    edible = 0
    poisonous = 0
    convex_count = None
    for i in range(len(input)):
        for item in mushroomsCol:
            if item[0] == mushroomsCol[i][0]:
                for attribute in item[1]:
                    if attribute[0] == input[i]:
                        edible = attribute[2]
                        poisonous = attribute[3]

                        results = [edible, poisonous]

                        # Plot results
                        labels = ['Edible', 'Poisonous']
                        plt.bar(labels, results)
                        plt.title(item[0])
                        plt.xlabel(input[i])
                        plt.ylabel('Probability')
                        plt.show()

    results = [ediResult, poiResult]

    # Plot of Over all Results
    labels = ['Edible', 'Poisonous']
    plt.bar(labels, results)
    plt.title('Mushroom Classification')
    plt.xlabel('Class')
    plt.ylabel('Probability')
    plt.show()


if __name__ == '__main__':
    mushroomsCol = []
    mushroomsRow = []
    poiCount = 0
    ediCount = 0
    category = ['poisonous', 'edible']

    with open('MushroomCSV.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')

        i = 0
        for row in reader:
            i += 1
            if i == 1:
                for entry in row:
                    mushroomsCol.append([entry, []])
                continue

            mushroomsRow.append(row)

    process(mushroomsRow, mushroomsCol, poiCount, ediCount)
    poiCount, ediCount = count(mushroomsRow, mushroomsCol, poiCount, ediCount)

    #Sample input: convex, scaly, yellow, yes, almond, free, close, broad, brown, enlarging, club, smooth, smooth, white, white, partial, white, one, pendant, black, scattered, meadows
    input = input("Enter sample instance: ")
    input = input.split(', ')

    if len(input) != len(mushroomsCol) - 1:
        print("Error: Invalid input")
        exit()

    poiResult = computation(mushroomsCol, input, category[0], poiCount, len(mushroomsRow))
    ediResult = computation(mushroomsCol, input, category[1], ediCount, len(mushroomsRow))

    visualization(mushroomsCol, ediResult, poiResult, input)

    print("\nProbability of being Poisonous: ", poiResult)
    print("Probability of being Edible: ", ediResult)

    if poiResult > ediResult:
        print(str(poiResult) + " > " + str(
            ediResult) + " therefore the mushroom base on the given instance is Poisonous.")
    else:
        print(str(ediResult) + " < " + str(
            poiResult) + " therefore the mushroom base on the given instance is Not Poisonous.")