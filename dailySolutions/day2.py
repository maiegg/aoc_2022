def run(inputData):
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
