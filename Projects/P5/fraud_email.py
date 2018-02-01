import email
import re

text = ''
email = ""
email_list = []
from_email = []
subject = []
body = ''
sub_mark = ""
body_start = False
email_start = False
with open("email.txt") as txt:
    for row in txt:
        if row.split(' r ')[0] == 'From':
            email_start = not email_start
            # print "found email"
            # print row
            continue
        if email_start:
            email += row
        if not email_start:
            email_list.append(email)
            email = ""
            email_start = not email_start

        head, tail = row.split(":")[0], row.split(":")[1:]
        if head == "Subject":
            sub_mark = tail
            subject.append(tail)
        if head == "From":
            match = re.findall(r'[\w\.-]+@[\w\.-]+', row)
            if match:
                from_email.append(match)
print email_list[1]
# with open("email.txt") as txt:
#     for row in txt:
#         text = text + row
#
# b = email.message_from_string(text)
# if b.is_multipart():
#     for payload in b.get_payload():
#         # if payload.is_multipart(): ...
#         print payload.get_payload()
# else:
#     print b.get_payload()