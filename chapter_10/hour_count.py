'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''

try:
    count = 0
    hours_count = {}
    name = input('Enter file name: ')
    handle = open(name)

    for line in handle:
        if line.startswith(('From:', 'From')) and not line.startswith('From:'):
            words = line.split()
            time = words[5]
            hour = time.split(':')[0]
            hours_count[hour] = hours_count.setdefault(hour, 0) + 1
    
    tuple_list = ([(key, value) for key, value in hours_count.items()])
    tuple_list.sort()

    for hours in tuple_list: 
        print(f'{hours[0]} {hours[1]}')

except FileNotFoundError:
    print(f'Can not find file named {name}')
    quit()
