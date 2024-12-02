import pandas as pandas

# df = pandas.read_csv("2024/Day1/test.dat", header=None, delimiter=r"\s+") 
df = pandas.read_csv("2024/Day1/day1.dat", header=None, delimiter=r"\s+") 

df.columns = ["left", "right"] #Add Column names

leftseries = df["left"].values
rightseries = df["right"]

lookupTable = rightseries.value_counts()

overallSimScore = 0
# For each item in the left series
for index in leftseries: 
    count = lookupTable.get(index) # Get the value from the lookup table
    if count is not None: # If value is None, overall sim score increases by 0
        simScore = (count * index)
        overallSimScore = overallSimScore + simScore
    

print("Sum of the similarity scores is {}".format(overallSimScore))



#multiply value by multiplier
# add to total 