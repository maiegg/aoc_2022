def run(inputData):
    with open(inputData) as file:
        lines = [line.rstrip() for line in file]

    dirsExplored = []
    dirParents = {}
    dirChildren = {}
    dirFileContents = {}
    currentDirectory = None
    parentOfCurrent = None

    for line in lines:
        if line == '$ cd ..':
            # current line is changing position; need to update orientation variables
            currentDirectory = parentOfCurrent
            parentOfCurrent = dirParents[currentDirectory]

        elif line[0:4] == '$ cd':
            pass
            # current line is changing position; need to update orientation variables
            child = line.split('$ cd ')[1]
            if child in dirParents.keys():
                pass
            else:
                dirParents[child] = currentDirectory
            parentOfCurrent = currentDirectory
            currentDirectory = child

        elif line[0:4] == '$ ls':
            # next line will provide information; this line can be ignored
            if currentDirectory in dirsExplored:
                dirAlreadyExplored = True
            else:
                dirAlreadyExplored = False
                dirsExplored.append(currentDirectory)

        elif line[0:3] == 'dir':
            # current line provides information about a child of currentDirectory
            # add this child to the list of currentDirectory's children of not already
            describedDir = line.split('dir ')[1]
            if currentDirectory in dirChildren.keys():
                if describedDir in dirChildren[currentDirectory]:
                    pass
                else:
                    dirChildren[currentDirectory].append(describedDir)
            else:
                dirChildren[currentDirectory] = [describedDir]

        elif line[0].isnumeric():
            # current line provides information about a file
            if currentDirectory in dirFileContents.keys():
                dirFileContents[currentDirectory].append(line)
            else:
                dirFileContents[currentDirectory] = [line]

        else:  # unexepcted input type (not cd or ls)
            print(f'Unexpected input: {line}')
            raise

    print(dirsExplored)
    dirTotalSize = {}
    for exploredDir in dirsExplored:
        print(f'{exploredDir} = exploredDir')
        dirTotalSize[exploredDir] = 0
        # [1] find all descendants
        if exploredDir in dirChildren.keys():
            # assemble full list of descendants
            allDescendantDirs = []
            children = dirChildren[exploredDir]  # list of children
            for child in children:
                allDescendantDirs.append(child)
                if child in dirChildren.keys():
                    children.extend(dirChildren[child])

            # [2] add up all descendants' file contents
            for descDir in allDescendantDirs:
                if descDir in dirFileContents.keys():
                    size = sum([int(item.split(' ')[0]) for item in dirFileContents[descDir]])
                    dirTotalSize[exploredDir] += size
                else:
                    pass

        # [3] add own file contents
        if exploredDir in dirFileContents.keys():
            size = sum([int(item.split(' ')[0]) for item in dirFileContents[exploredDir]])
            dirTotalSize[exploredDir] += size
    print('!!!')
    print(dirTotalSize)

    runningTotal = 0
    for k in dirTotalSize.keys():
        if (dirTotalSize[k] <= 100000):
            runningTotal += dirTotalSize[k]


    print(f'Total size of qualified directories is {runningTotal:,}')