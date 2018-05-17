# _*_ coding:utf-8 _*_
import re


def query_contact():
    name = input('----------------------\nWhich contact you want to query?(deflaut is all):')
    with open(r'.\contact.txt', 'r') as f:
        contacts = f.readlines()
        if name == '':
            print('----------------------')
            for contact in contacts:
                print(contact)

        else:
            count = False
            for contact in contacts:
                if re.search('Name: {}   PhoneNumber'.format(name), contact):
                    count = True
                    print('----------------------\n' + contact)
                    break

            if not count:
                print("----------------------\nDont't have this contact!")
                query_contact()
