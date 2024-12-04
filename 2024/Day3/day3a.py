# opening the file 
import re


# file_obj = open("/Users/kevincammarata/Downloads/AdventOfCode/2024/Day3/day3test.dat", "r") 
file_obj = open("/Users/kevincammarata/Downloads/AdventOfCode/2024/Day3/day3data.dat", "r") 


# reading the data from the file 
file_data = file_obj.read() 
# print(file_data)
good_mults = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)',file_data)

sum = 0
for pair in good_mults:
    first = int(pair[0])
    second = int(pair[1])
    total = first * second
    sum = sum + total
    print("{} * {} = {}".format(first, second,total))

# print(good_mults)
print("Grand Total: {}".format(sum))