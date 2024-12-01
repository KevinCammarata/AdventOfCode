import pandas as pandas

# df = pandas.read_csv("2024/Day1/test.dat", header=None, delimiter=r"\s+") 
df = pandas.read_csv("2024/Day1/day1.dat", header=None, delimiter=r"\s+") 

df.columns = ["left", "right"] #Add Column names

leftseries = df["left"]
rightseries = df["right"]

# print(leftseries)
# print(rightseries)

leftsorted = leftseries.sort_values().array
rightsorted = rightseries.sort_values().array

diff = sum(abs(leftsorted - rightsorted))

print(diff)



# total = diff.sum()

# print(total)

# total = abs(leftsum - rightsum)d
# print("|{} - {}| = {}".format(leftsum, rightsum, total))
