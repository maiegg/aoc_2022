def run(inputData):
    # read txt file into list (1 entry per line)
    with open(inputData) as file:
        lines = [line.rstrip() for line in file]

    """
    Part 1. How many positions does the tail visit? 
    """
    # let the starting position be (0,0) for both T and H
    tail_positions = []
    tail_current_pos = (0,0)
    head_current_pos = (0,0)
    head_previous_pos = None

    def directions_to_coords(current_pos, dirr, dist=1):
        """

        :param current_pos: tuple of current (x,y) position
        :param dirr: direction of instructed movement
        :param dist: distance of instructed movement
        :return: new position (x,y)
        """

        if dirr == 'U':
            return current_pos[0], current_pos[1] + dist
        elif dirr == 'L':
            return current_pos[0] - dist, current_pos[1]
        elif dirr == 'R':
            return current_pos[0] + dist, current_pos[1]
        elif dirr == 'D':
            return current_pos[0], current_pos[1] - dist
        else:
            print(f'Unrecognized input - {dirr}')
            raise

    for move in lines:

        direction = move.split(' ')[0]
        distance = int(move.split(' ')[1])

        # turn instruction in a list of 1-step moves
        instructions = [(direction, i) for i in [1] * distance]

        for instr in instructions:
            print(f'{move}: {instr} --> {head_current_pos}')
            # update H position (current and previous)
            head_previous_pos = head_current_pos
            head_current_pos = directions_to_coords(head_current_pos, instr[0], instr[1])

            # if needed, update T position
            tail_current_x = tail_current_pos[0]
            tail_current_y = tail_current_pos[1]
            head_current_x = head_current_pos[0]
            head_current_y = head_current_pos[1]

            if (
                (abs(tail_current_x - head_current_x) > 1) or
                (abs(tail_current_y - head_current_y) > 1)
            ):  # tail not adjacent to head
                # update tail position
                tail_current_pos = head_previous_pos

                # add tail position to tracking list
                tail_positions.append(
                    tail_current_pos
                )

    print(tail_positions)
    print(len(tail_positions))
