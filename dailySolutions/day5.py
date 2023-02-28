def run(inputData):
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
            stacks[moveFrom] = stacks[moveFrom][amt: len(stacks[moveFrom])]

            # print(moveTo, stacks[moveTo])
            # print(moveFrom, stacks[moveFrom])
        answer = []
        for stackIdx in stackIndices:
            answer.append(stacks[stackIdx][0])
        print(f'\nAnswer to part {part}: {"".join(answer)}')
        # print('\nafter:')
        # for stackIdx in stackIndices:
        #     print(stackIdx, stacks[stackIdx])

