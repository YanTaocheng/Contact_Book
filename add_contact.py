# _*_ coding:utf-8 _*_
import re, main


def add_contact():
    name = input('----------------------\nPlease enter the contact name:')
    if name == '':
        print('----------------------\nName is empty')
        add_contact()

    else:
        with open(r'.\contact.txt', 'r') as f:
            for line in f.readlines():
                if re.search('Name: {}   PhoneNumber'.format(name), line):
                    print('----------------------\nIt already has this contact!')
                    main.main()
                    break

        phone_number = input('----------------------\nPlease enter the contact Phone Number:')

        try:
            phone_number = int(phone_number)
            with open(r'.\contact.txt', 'a') as f:
                content = 'Name: {}   PhoneNumber: {}'.format(name, phone_number) + '\n'
                f.write(content)
                print('----------------------\nAdd contact: {} successfully!'.format(name))
        except Exception as e:
            print('----------------------\nPhone Number not correct!')
            add_contact()
