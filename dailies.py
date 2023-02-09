def day1(inputData):
    """
    :param inputData: daily input data source
    :return: none, print answers
    """
    # read txt file into list (1 entry per line)
    with open(inputData) as file:
        lines = [line.rstrip() for line in file]

    # iterate through list; where next row is empty string, current index is one elf's endpoint
    # store elf (start, stop) indices
    lastElfIdx = 0  # beginning index of current elf
    elfBoundaries = []  # list of tuples of elf (start, stop) indices
    for i in range(len(lines) - 1):
        if lines[i + 1] == '':
            elfBoundaries.append((lastElfIdx, i))
            lastElfIdx = i + 2  # next beginning index is the row after the blank row

    caloriesPerElf = []
    for tup in elfBoundaries:
        caloriesPerElf.append(sum([int(i) for i in lines[tup[0] : tup[1]+1]]), )

    # Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?

    # "slow" way: list.remove(list.max()) - have to iterate over list 3 times to find top 3 values
    # might behave weird if there are 2+ elves carrying the same, max number of calories

    # sort list and retrieve top 3 values (default sort is asc)

    print(f'part 1: {max(caloriesPerElf)}')
    print(f'part 2: {sum(caloriesPerElf[-3:])}')
    return
def day2(inputData):
    # read txt file into list (1 entry per line)
    with open(inputData) as file:
        lines = [line.rstrip() for line in file]

    # split opponent and own plays into tuples
    lines = [item.split(' ') for item in lines]

    convert = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }

    gamesConverted = [(item[0], convert[item[1]]) for item in lines]

    """
    The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)
    plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).
    """

    def score(opp, own):
        """
        winning plays (opp, own):

        A, B
        B, C
        C, A


        losing plays:
        A, C
        B, A
        c, B

        """

        # A for Rock, B for Paper, and C for Scissors
        scorePerPlay = {
            'A': 1,
            'B': 2,
            'C': 3
        }

        # lexicographic sorting - A < B < C
        outcomeBonus = 0
        if opp == own:  # draw
            outcomeBonus += 3

        elif opp == 'C' and own == 'A':  # only one winning play is lexicographically out of order
            outcomeBonus += 6

        elif opp == 'A' and own == 'C':  # only one losing play is lexicographically out of order
            pass

        elif opp < own:  # win
            outcomeBonus += 6

        else:  # lose
            pass

        return (outcomeBonus + scorePerPlay[own])

    scores = [score(item[0], item[1]) for item in gamesConverted]
    print(f'part 1: {sum(scores)}')

    """
    Part two 
    """
    # A for Rock, B for Paper, and C for Scissors
    convert = {
        # if opponent plays A and you desire [outcome]:
        'A': {
            'Z': 'B',  # win
            'X': 'C',  # lose
            'Y': 'A'  # draw
        },
        'B': {
            'Z': 'C',
            'X': 'A',
            'Y': 'B'
        },
        'C': {
            'Z': 'A',
            'X': 'B',
            'Y': 'C'
        }

    }

    gamesConverted = [(item[0], convert[item[0]][item[1]]) for item in lines]

    scores = [score(item[0], item[1]) for item in gamesConverted]
    print(f'part 2: {sum(scores)}')
def day3(inputData):
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