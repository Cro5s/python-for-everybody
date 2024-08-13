'''
What Python function would you use if you wanted to prompt the user for a file name to open?
'''

file_name = input('Enter file name: ')

try:
  file_handle = open(file_name)
except:
  print(f'Can not find file named {file_name}')
  quit()

for line in file_handle:
  print((line.rstrip().upper())) 