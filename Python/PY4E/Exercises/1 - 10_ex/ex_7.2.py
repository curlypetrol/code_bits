"""
Autograder: Exercise 7.2 Files

7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

Desired Output
Average spam confidence: 0.7507185185185187

"""

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)


sc = None
spam_conf = []

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    sc = float(line[20:]) # Desired float starts at index 20
    spam_conf.append(sc)

    
tot_conf = 0

for x in spam_conf: # For loop to execute sum() function as it is not accepted in this exercise
    tot_conf += x
    
avg_conf = tot_conf/len(spam_conf)
    
print("Average spam confidence:", avg_conf)