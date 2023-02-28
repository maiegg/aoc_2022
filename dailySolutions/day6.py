def run(inputData):
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

