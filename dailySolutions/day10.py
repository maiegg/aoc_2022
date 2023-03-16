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