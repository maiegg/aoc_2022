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
def runOld(inputData):
    with open(inputData) as file:
        lines = [line.rstrip() for line in file]

    """
    goal: to print total size of all directories below a certain size 

    - keep a list of all directories
    - keep a dictionary of each directory and its own file sizes
    - keep a dictionary of each directory and its child directories

    - loop trough list of directories, adding child directory sizes to content sizes

    """
    lines = lines[0:13]

    # output variables
    dirFileContents = {}  # (dir : total file contents [size])
    dirChildren = {}  # (dir : list of children)
    dirParents = {}  # dir : parent dir)

    # tracking variables
    currentDirectory = None
    parentOfCurrent = None
    dirsExplored = []

    for line in lines:
        # print(line)
        if line == '$ cd ..':
            # current line is changing position; need to update orientation variables
            currentDirectory = parentOfCurrent
            parentOfCurrent = dirParents[currentDirectory]

        elif line[0:4] == '$ cd':
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
            # update dirChildren to describe this relationship if not already
            if currentDirectory in dirChildren.keys():
                describedDir = line.split('dir ')[1]
                if describedDir in dirChildren[currentDirectory]:
                    pass
                else:
                    dirChildren[currentDirectory].append(describedDir)
                del describedDir
            else:
                dirChildren[currentDirectory] = [line.split('dir ')[1]]

        elif line[0].isnumeric():
            # current line provides information about a file
            # do NOT increment the file size counter again if dirAlreadyExplored
            if not dirAlreadyExplored:
                if currentDirectory in dirFileContents.keys():
                    dirFileContents[currentDirectory] += int(line.split(' ')[0])
                else:
                    dirFileContents[currentDirectory] = int(line.split(' ')[0])

            # else, dir already explored, pass

        else:  # unexepcted input type (not cd or ls)
            print(f'Unexpected input: {line}')
            raise

    """
    calculate a total directory size for each directory explored
    """
    dirTotalSize = {}
    for thisdir in dirsExplored:
        # for thisdir in ['/']:
        # start with 0
        print('output:')
        dirTotalSize[thisdir] = 0

        # add the sizes of any files in directory
        if thisdir in dirFileContents.keys():
            dirTotalSize[thisdir] += dirFileContents[thisdir]

        # the hard part - recursively add up all the dir's descendants' sizes
        if thisdir in dirChildren.keys():
            allDescendantDirs = []
            children = dirChildren[thisdir]  # list of children
            for child in children:
                allDescendantDirs.append(child)
                if child in dirChildren.keys():
                    print('!!!', child, dirChildren[child])
                    children.extend(dirChildren[child])
            print(thisdir, allDescendantDirs)
            for descDir in allDescendantDirs:
                if descDir in dirFileContents.keys():
                    dirTotalSize[thisdir] += dirFileContents[descDir]
                else:
                    pass
    print('!!!')
    print(dirTotalSize)