# _*_ coding:utf-8 _*_
import re


def modify_contact():
    name = input('----------------------\nWhich contact you want to modify?(Name):')
    if name == '':
        print('----------------------\nName is empty')
        modify_contact()

    else:
        try:
            with open(r'.\contact.txt', 'r') as f:
                contacts = f.readlines()
                count = False
                new_conatcts = []
                for contact in contacts:
                    if re.search('Name: {}   PhoneNumber'.format(name), contact):
                        count = True
                        info = input('----------------------\nEnter the modify info(Name,Number):')
                        name1, phone_number = re.split(r',', info)
                        contact = 'Name: {}   PhoneNumber: {}\n'.format(name1, phone_number)

                    new_conatcts.append(contact)

                if not count:
                    print("----------------------\nDont't have this contact!")

                else:
                    with open(r'.\contact.txt', 'w') as f:
                        f.writelines(new_conatcts)
                        print("----------------------\nModify contact successfully!")

        except Exception as e:
            print(e)
