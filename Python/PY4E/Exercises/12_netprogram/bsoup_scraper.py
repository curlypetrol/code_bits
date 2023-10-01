"""

Scraping Numbers from HTML using BeautifulSoup - Network Programming

In this assignment you will write a Python program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read the HTML from the data files below, 
and parse the data, extracting numbers and compute the sum of the numbers in the file.

We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1850923.html (Sum ends with 18)

You do not need to save these files to your folder since your program will read the data directly from the URL. Note: Each student will have a distinct data url for the 
assignment - so only use your own data url for analysis.

Data Format
The file is a table of names and comment counts. 

You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
Look at the sample code provided. It shows how to find all of a certain kind of tag, loop through the tags and extract the various aspects of the tags.
You need to adjust this code to look for span tags and pull out the text content of the span tag, convert them to integers and add them up to complete the assignment.

ANSWER:

Count: 50
Sum: 2318


"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

nums = []

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    tag = tag.contents[0]
    nums.append(tag)

ints = []

for num in nums:
    num = int(num)
    ints.append(num)

print('Count:', len(ints))
print('Sum:',sum(ints))
    