import re

text = ''
email = ""
email_dict = {}
email_list = []
from_email = []
subject = ""
body = ''
sub_mark = ""
body_start = False
email_start = False
tail = ''
counter = 0
with open("email.txt") as txt:

    for row in txt:
        counter += 1
        if counter < 200:
            if row.split(' r ')[0] == 'From':
                email_start = not email_start

            if email_start:
                email += row
                head, tail = ''.join(row.split(":")[0]), \
                             ''.join(row.split(":")[1:])
                if head == "Subject":
                    subject = tail
                    email_dict[subject] = ""
            if not email_start:
                email_dict[subject] = email
                email_list.append(email)
                email = ""
                email_start = not email_start

print email_dict