def run(inputData):
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
