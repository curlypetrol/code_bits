"""
Autograder: Exercise 6.5 Strings

6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
Convert the extracted value to a floating point number and print it out.

Desired Output
0.8475

"""

text = "X-DSPAM-Confidence:    0.8475"

x = text.find('0')
y = text.find('5')

print(float(text[x:y+1]))