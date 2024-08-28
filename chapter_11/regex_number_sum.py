'''
Finding Numbers in a Haystack

In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.

Handling The Data

The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+'
and then converting the extracted strings to integers and summing up the integers.
'''
import re
# One liner solution
# print( sum( [ int(num) for num in re.findall(r'\d+\.?\d*', open('regex_sum.txt').read()) ] ) )

sum = 0
file_name = input('Enter file name: ')

try:
    with open(file_name, 'r') as handle:
        for line in handle:
            number_strings = re.findall(r'\d+\.?\d*', line)

            for num in number_strings:
                sum += int(num)

except FileNotFoundError:
    print(f'Can not find file named {file_name}')
    quit()

print(sum)