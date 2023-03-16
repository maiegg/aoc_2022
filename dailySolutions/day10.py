def day10(inputData):
    # read txt file into list (1 entry per line)
    with open(inputData) as file:
        instructions = [line.rstrip() for line in file]

    """
    noop does nothing
    addx will increment the register on cycle n+2 
    """
    register = 1
    cycle_number = 0
    execution_queue = []
    signal_strengths = []

    for idx in range(222):
        cycle_number += 1
        # print(cycle_number)
        # do the cycle number math to check - want register value at beginning of cycle
        if (cycle_number == 20) or ((cycle_number - 20) % 40 == 0):
            print(f'cycle number {cycle_number}; register value: {register}; signal strength {register*cycle_number}')
            signal_strengths.extend([register*cycle_number])

        if idx < len(instructions):
            # add starts to execution queue
            if instructions[idx][0:4] == 'addx':
                execution_queue.extend(
                    [0, int(instructions[idx].split(' ')[1])]
                )
            elif instructions[idx][0:4] == 'noop':
                execution_queue.extend([0])
            else:
                print(f'malformed input: {instructions[idx]}')
                raise

        # execute out of queue
        if len(execution_queue) > 0:
            register += execution_queue[0]
            execution_queue.pop(0)

    print('\nAnswer:')
    print(f'Register: {register}')
    print(f'Cycles: {cycle_number}')
    print(f'Signal strength TOTAL: {sum(signal_strengths)}')
    print(signal_strengths)
    
  def day10part2(inputData):
    # read txt file into list (1 entry per line)
    with open(inputData) as file:
        instructions = [line.rstrip() for line in file]

    register = 1
    cycle_number = 0
    execution_queue = []

    all_rows_render = []
    this_row_render = ['.'] * 40
    pixel_to_draw = 0

    for idx in range(242):
        cycle_number += 1

        """
        Part 2. 
        each cycle, the pixel being drawn advances by 1 
        the sprite's position each cycle is the value of the register (CENTER of sprite)
        if the pixel being drawn is one of the 3 covered by the sprite, it lights up 
        """

        if (cycle_number - 1) % 40 == 0:
            pixel_to_draw = 0
            all_rows_render.append(this_row_render)
            this_row_render = ['.'] * 40

        if idx < len(instructions):
            # add starts to execution queue
            if instructions[idx][0:4] == 'addx':
                execution_queue.extend(
                    [0, int(instructions[idx].split(' ')[1])]
                )
            elif instructions[idx][0:4] == 'noop':
                execution_queue.extend([0])
            else:
                print(f'malformed input: {instructions[idx]}')
                raise

        print(f'cycle {cycle_number}: register {register}; pixel to draw {pixel_to_draw}')
        # check sprite position
        if abs(pixel_to_draw - register) <= 1:
            print('light')
            this_row_render[pixel_to_draw] = '#'
        pixel_to_draw += 1

        # execute out of queue
        if len(execution_queue) > 0:
            register += execution_queue[0]
            execution_queue.pop(0)

    print('---')
    # print final result
    for row in all_rows_render[1:]:
        print(''.join(row))
