def run(inputData):
    with open(inputData) as file:
        rucksacks = [line.rstrip() for line in file]

    def priority(letter):
        """
        To help prioritize item rearrangement, every item type can be converted to a priority:

        Lowercase item types a through z have priorities 1 through 26.
        Uppercase item types A through Z have priorities 27 through 52.
        """
        # https://docs.python.org/3/library/functions.html#ord
        if letter == letter.lower():
            return ord(letter.lower()) - 96
        else:
            return ord(letter.lower()) - 96 + 26

    priorityValues = []
    for ruck in rucksacks:
        if len(ruck) % 2 > 0:
            print(f'odd number of items in rucksack: {ruck}')
            raise
        halfwayIndex = int(len(ruck) / 2)
        frontHalf = ruck[0:halfwayIndex]
        backHalf = ruck[halfwayIndex:]
        commonItem = ''.join(set(frontHalf).intersection(backHalf))
        if len(commonItem) > 1:
            print('more than 1 common item - bad input')
            raise
        priorityValues.append(priority(commonItem))

    print(f'part 1: {sum(priorityValues):,}')

    """
    Part 2 
    """
    if len(rucksacks) % 3 > 0:
        print(f'{len(rucksacks)} cannot be divided into groups of 3 - bad input')
        raise

    groupStarts =  [3*i for i in range(int(len(rucksacks)/3))]

    priorityValues = []

    for groupStartIdx in groupStarts:
        group = rucksacks[groupStartIdx: groupStartIdx + 3]
        groupCommonItem = ''.join(set(group[0])\
                    .intersection(group[1])\
                    .intersection(group[2])
                )

        priorityValues.append(
            priority(groupCommonItem)
        )

    print(f'part 2: {sum(priorityValues):,}')
