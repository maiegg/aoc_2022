def run(inputData):
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