'''
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using
the split() method. The program should build a list of words. For each word on each line check to see if the word
is already in the list and if not append it to the list. When the program completes, sort and print the resulting words
in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt
'''

file_name = input('Enter file name: ')
words = list()

try:
    with open(file_name) as file_handle:
        for line in file_handle:
            for word in line.split():
                if word not in words:
                    words.append(word)
except FileNotFoundError:
    print(f'Can not find file named {file_name}')
    quit()

words.sort()
print(words)