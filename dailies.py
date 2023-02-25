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
def day4(inputData):
    with open(inputData) as file:
        cleaningAssignments = [line.rstrip() for line in file]
    """
    Part 1. 
    In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections
    their partner will already be cleaning, so these seem like the most in need of reconsideration.
    In how many assignment pairs does one range fully contain the other?
    """
    fullyContained = 0
    for pairAssignment in cleaningAssignments:
        elf1 = [int(item) for item in pairAssignment.split(',')[0].split('-')]
        elf2 = [int(item) for item in pairAssignment.split(',')[1].split('-')]

        if elf1[0] < elf2[0]:
            # outside lower bound is elf 1
            # elf 2 must be contained within elf 1
            # elf 2 upper bound must be leq to elf 1 upper bound
            if elf2[1] <= elf1[1]:
                fullyContained += 1
        elif elf1[0] == elf2[0]:
            # start on same value; will always be fullyContained
            fullyContained += 1
        else:
            # outside lower bound is elf 2
            # elf 1 must be contained within elf 2
            # elf 1 upper bound must be leq to elf 2 upper bound
            if elf1[1] <= elf2[1]:
                fullyContained += 1
    print(f'Part 1: {fullyContained}')

    """
    Part 2. 
    [T]he Elves would like to know the number of pairs that overlap at all.
    """
    overlaps = 0
    # overlap == one lower bound is less than one upper bound
    for pairAssignment in cleaningAssignments:
        elf1 = [int(item) for item in pairAssignment.split(',')[0].split('-')]
        elf2 = [int(item) for item in pairAssignment.split(',')[1].split('-')]

        elvesSorted = [elf1, elf2] # might need to check sorting key/behavior
        elvesSorted.sort()

        if elvesSorted[0][1] >= elvesSorted[1][0]:
            overlaps += 1
    print(f'Part 2: {overlaps}')
def day5(inputData):
    with open(inputData) as file:
        inputDataRead = [line.rstrip() for line in file]

    # identify the diagram portion of input
    # loop through lines until blank line
    begStacks = []
    movesIdxStart = 0
    for l in inputDataRead:
        begStacks.append(l)
        movesIdxStart += 1
        if len(l) == 0:
            break

    # the remainder of the input file is move instructions
    moves = inputDataRead[movesIdxStart:len(inputDataRead)]

    # reorganize the input into something usable
    """
    our input rows look like this:
    0 [
    1 T ...
    2 ]
    3 sp
    4 [ 
    5 V ...
    6 ] 
    7 sp 
    ...
    
    so with 9 crate stacks, the indices we care about are every other odd number up to 35:
    1, x, 5, x, 9, x, 13, x, 17, x, 21, x , 25, x, 29, x, 33, x
    
    generalize this to any number of crate stacks:
    9*4 = 36 
    36 - 1 = 35 
    for (n) stacks, find every other odd number up to n*4 - 1 
    will always start with 1
    """
    stackIndices = [int(s) for s in begStacks[-2].split() if s.isdigit()]

    columnIndices = []
    i = 1
    while i <= (max(stackIndices) * 4 - 1):
        columnIndices.append(i)
        i += 4


    stackToColumnIdx = dict(zip(stackIndices, columnIndices))

    """
    iterate through stacks (columns)
    keep a list of the crate letters, in order, that belong to each column in the starting arrangement 

    goal = dict of lists 
    stacks {
      1 : [T, V, J, W, ...,
      2 : [ ..., 
    } 
    """
    stacks = {}
    for stackIdx in stackIndices:
        stacks[stackIdx] = []
        for row in begStacks[0:-2]:  # last row is blank, second-to-last row is stack indices
            if len(row) >= stackToColumnIdx[stackIdx]:
                if row[stackToColumnIdx[stackIdx]] != ' ':
                    stacks[stackIdx].append(row[stackToColumnIdx[stackIdx]])
            else:
                pass
                # print('!', row, stackToColumnIdx[stackIdx])

    stacksBeginning = stacks.copy()

    """
    Part 1.
    """
    print('before:')
    for stackIdx in stackIndices:
        print(stackIdx, stacks[stackIdx])
    #
    # cratesKeptStart = []
    # for stackIdx in stackIndices:
    #     for i in stacks[stackIdx]:
    #         cratesKeptStart.append(i)

    for part in [1, 2]:

        stacks = stacksBeginning.copy()

        for move in moves:
            # print('move =',move)
            move = [int(s) for s in move.split() if s.isdigit()]

            amt = move[0]
            moveFrom = move[1]
            moveTo = move[2]

            # print(moveTo, stacks[moveTo])
            # print(moveFrom, stacks[moveFrom])

            # capture crates to move
            cratesToMove = stacks[moveFrom][0:amt]

            if part == 2:
                cratesToMove.reverse()
            else:
                pass

            if len(cratesToMove) != amt:
                raise

            # append to moveTo stack
            for c in cratesToMove:
                stacks[moveTo].insert(0, c)

            # remove from moveFrom stack
            stacks[moveFrom] = stacks[moveFrom][amt : len(stacks[moveFrom])]

            # print(moveTo, stacks[moveTo])
            # print(moveFrom, stacks[moveFrom])
        answer = []
        for stackIdx in stackIndices:
            answer.append(stacks[stackIdx][0])
        print(f'\nAnswer to part {part}: {"".join(answer)}')
        # print('\nafter:')
        # for stackIdx in stackIndices:
        #     print(stackIdx, stacks[stackIdx])

def day6(inputData):
    with open(inputData) as file:
        message = [line.rstrip() for line in file]
    message = message[0] # reformat into single string - this input is different than the others

    """
    Part 1 - start of packet marker 
    """
    # first eligible start character is the fourth (index 3)
    for endIdx in range(3, len(message)):
        lastFour = message[endIdx-4:endIdx]

        if len(set(lastFour)) == 4:
            print(f'Part 1: {lastFour} found after scanning {endIdx} characters')
            break

    """
    Part 2 - start of message market 
    """
    for endIdx in range(13, len(message)):
        lastFour = message[endIdx-14:endIdx]

        if len(set(lastFour)) == 14:
            print(f'Part 2: {lastFour} found after scanning {endIdx} characters')
            break