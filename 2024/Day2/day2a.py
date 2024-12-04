def isSafe(line):
    numbers = line.split()
    direction = ""
    for i in range(1,len(numbers)):
        first = int(numbers[i-1])
        second = int(numbers[i])
        diff = abs(second-first)
        if(diff < 1): 
            return False  
        if(diff > 3):
            return False
        if(second > first):
            if direction=="decrease":
                return False
            elif direction=="":
                direction="increase"
        
        if(first > second):
            if direction=="increase":
                return False
            elif direction=="":
                direction="decrease"
    return True


# opening the file 
file_obj = open("/Users/kevincammarata/Downloads/AdventOfCode/2024/Day2/day2data.dat", "r") 

# reading the data from the file 
file_data = file_obj.read() 

# splitting the file data into lines 
lines = file_data.splitlines() 
safeCount=0
for line in lines:
    safe = isSafe(line)
    if safe:
        safeCount = safeCount + 1
    print(line)
    print("Is Safe: {}".format(safe))
print("Count of safe lines: {}".format(safeCount))
file_obj.close() 

