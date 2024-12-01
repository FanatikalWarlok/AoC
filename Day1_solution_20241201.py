
##PT1 take the left column and 
def Part1():
    infile = open("Day1_input_20241201.py", "r")
    left = []
    right = []
    for line in infile:
##        print(line)
        linelist = line.split()
##        print(linelist)
        left.append(int(linelist[0]))
        right.append(int(linelist[1]))
    left.sort()
    right.sort()
    sums = 0
    for i in range(len(left)):
        diff = abs(int(left[i]) - int(right[i]))
        sums = sums + diff
    print(sums)
##Part1()


##Correct answer = 1646452

def Part2():
    infile = open("Day1_input_20241201.py", "r")
    left = []
    right = []
    for line in infile:
##        print(line)
        linelist = line.split()
##        print(linelist)
        left.append(int(linelist[0]))
        right.append(int(linelist[1]))
    sim_scor = 0
    for i in range(len(left)):
        numbs_in_R = right.count(left[i])
        sim_scor = sim_scor + left[i]*numbs_in_R
    print(sim_scor)
Part2()
