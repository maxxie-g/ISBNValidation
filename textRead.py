# TODO: Make it a web applet using HTML5, CSS, and JS???


# List of Vars needed for the algorithm
import os
rawList = []                    # List of raw ISBN vales
isbnList = []                   # List of cleaned ISBN values
isbnString = ""                 # An individual ISBN Value
isbnInt = []                    # List for the individual ints of an ISBN
weight = 10                     # Used to calculate the sum
weightedSum = []                # List for holding the weighted isbnInts


# Used to check for and eventually delete the output file
if os.path.exists("output.txt"):
    os.remove("output.txt")
else:
    print("The file will be created.")

# Opens the .txt file and transfers the data into Lists of Strings
# Removes dashes and new line characters

f = open("./isbnTest.txt","r")    # Opens .txt file for further analysis

while(True):
    line = f.readline()
    dashLine = line.replace("-","")
    newLine = dashLine.replace("\n","")
    if not line:
        break
    isbnList.append(newLine)
    rawList.append(line.replace("\n",""))

f.close()

# Calculates the validity of ISBN values by:
# 1. Multiplying each digit by its associated weight
# 2. Summing the products
# 3. Taking the modulus of 11
# At the end a check is made to see if the modulo returned is 0

output = open("output.txt", "a")

for i in range(len(isbnList)):
    isbnString = isbnList[i]
    for x in range(len(isbnString)):
        if isbnString[x] == 'X':
            weightedSum.append(10 * (weight - x))
        else:
            weightedSum.append(int(isbnString[x]) * (weight - x))
    if sum(weightedSum) % 11 == 0:
        print("ISBN '" + rawList[i] + "' is valid.")
        output.write("ISBN '" + rawList[i] + "' is valid.\n")
    else:
        print("ISBN '" + rawList[i] + "' is not valid.")
        output.write("ISBN '" + rawList[i] + "' is not valid.\n")
    weightedSum = []

output.close()