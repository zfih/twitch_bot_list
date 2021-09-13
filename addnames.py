import sys
import getopt
from os.path import exists

# read given file and return set of unique names
def readFileAndCollectNames(filename, names, existingList = False):
    if not exists(filename):
        print("File:", filename, "does not exists")
        return

    oldCount = 0
    newCount = 0

    file = open(filename, 'r')
    currentLine = file.readline()
    while currentLine:
        name = currentLine
        
        # newline
        if not name or name.isspace():
            currentLine = file.readline()
            continue
        
        # if the item is in the existing list, remove the ".ban"
        if existingList and currentLine.split()[0] == ".ban" :
            name = currentLine.split()[1]

        name = name.strip()

        if name in names:
            oldCount += 1
        else:
            newCount += 1
            names.append(name)

        currentLine = file.readline()
    
    if not existingList:
        print(oldCount, "names already in lists")
        print(newCount, "new names added to lists")

    file.close()

# writes listfile with names
def writeListFile(filename, names):
    file = open(filename, 'w')
    for name in names:
        if name and not name.isspace():
            name.strip()
            file.write(".ban " + name + "\n")

    file.close()

# helper function for list filename
def listName(count):
    return 'list' + str(count) + '.txt'

# read each existing file and collect names
def readExistingFiles(names):
    count = 1
    filename = listName(count)

    files = []

    while exists(filename):
        files.append(filename)
        count += 1
        filename = listName(count)

    for file in files:
        readFileAndCollectNames(file, names, True)
    
    return names

def writeNamesToFiles(names):
    filecount = 1
    namecount = 0
    increment = 400 # max line count for StreamElements

    # write files in increments of 400 to disk
    while namecount < len(names):
        writeListFile(listName(filecount), names[namecount:namecount+increment])
        namecount += increment
        filecount += 1

def main(argv):
    inputfile = ''

    try:
        opts, args = getopt.getopt(argv, 'hi:')
    except getopt.GetoptError:
        print('addnames.py [-i <inputfile>] [names...]')
        sys.exit()

    for opt, arg in opts:
        if opt == '-h':
            print('addnames.py -i <inputfile>')
            sys.exit()
        elif opt == '-i':
            inputfile = arg
    
    # collect names
    names = []
    readExistingFiles(names)

    # read input files if any exist
    if len(inputfile) > 0:
        readFileAndCollectNames(inputfile, names)

    # read input names and add to args
    if len(args) > 0:
        names.extend(args)

    writeNamesToFiles(names)    

if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[1:])