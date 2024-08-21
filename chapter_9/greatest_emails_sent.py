'''
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

try:
    email_sent_count = dict()
    name = input('Enter file: ')

    with open(name) as handle:
        for line in handle:
            if line.startswith(('From:', 'From')) and not line.startswith('From:'):
                words = line.split()
                email_sent_count[words[1]] = email_sent_count.setdefault(words[1], 0) + 1

except FileNotFoundError:
    print(f'Can not find file named {name}')
    quit()
max_email = max(email_sent_count, key=email_sent_count.get)
max_count = email_sent_count[max_email]

print(f'{max_email} {max_count}')