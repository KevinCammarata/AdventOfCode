def isSafe(numbers,safetyDampener):
    # numbers = line.split()
    safe=True
    unsafeIndex=0
    direction = ""
    for i in range(1,len(numbers)):
        first = int(numbers[i-1])
        second = int(numbers[i])
        diff = abs(second-first)
        if(diff < 1 or diff > 3): 
            safe = False 
            # break 
        # if(diff > 3):
        #     safe = False
        #     # break  
        if(second > first):
            if direction=="decrease":
                safe = False
                # break 
            direction="increase"
        elif(first > second):
            if direction=="increase":
                safe = False
                # break 
            # elif direction=="":
            direction="decrease"
        if not safe:
            unsafeIndex = i-1
            break
        # if not safe, trigger the safety dampener, pop the offending number, and recall isSafe
    if not safetyDampener and not safe:
        # print("Line {} is not safe.  Removing {} at index {} and retrying".format(numbers, numbers[unsafeIndex], unsafeIndex))
        numbers.pop(unsafeIndex)
        # print("Retrying with line {}".format(numbers))
        safe = isSafe(numbers, True)
    if safetyDampener:
        if safe: 
            print("After triggering safetyDampener, this line is {}".format(safe))
    return safe

# opening the file 
file_obj = open("/Users/kevincammarata/Downloads/AdventOfCode/2024/Day2/day2data.dat", "r") 

# reading the data from the file 
file_data = file_obj.read() 

# splitting the file data into lines 
lines = file_data.splitlines() 
safeCount=0
unsafeCount=0
for line in lines:
    numbers = line.split()
    safe = isSafe(numbers,False)
    if safe:
        safeCount = safeCount + 1
    elif not safe:
        unsafeCount = unsafeCount + 1
    # print(line)
    # print("Is Safe: {}".format(safe))
print("Count of safe lines: {}".format(safeCount))
print("Count of unsafe lines: {}".format(unsafeCount))
file_obj.close() 

