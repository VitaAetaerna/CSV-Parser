import csv
import os
ContactsFile = open('C:/Users/Leon/Desktop/Code/Py/CSV Parser/NewContacts.txt', 'w')

with open('C:/Users/Leon/Desktop/Code/Py/CSV Parser/Contacts.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        print(
           """BEGIN:VCARD
VERSION:2.1
FN:{}
TEL;CELL:{}
END:VCARD""".format(row[5].split("Â")[0], row[12].split("Â")[0].replace(" ", ""))
        )
        print('\n')


