# _*_ coding:utf-8 _*_
import re, main


def delete_contact():
    name = input('----------------------\nWhich contact you want to delete:')
    if name == '':
        print('----------------------\nName is empty')
        delete_contact()

    else:
        try:
            count = False
            new_contact = []
            with open(r'.\contact.txt', 'r') as old_file:
                old_contact = old_file.readlines()  # 读取每一行info， 存入列表 old_contact
                for contact in old_contact:  # 找出要删除的联系人，别把其他人存入列表new_contact
                    if re.search('Name: {}   PhoneNumber'.format(name), contact):
                        count = True
                    else:
                        new_contact.append(contact)

                if count == True:
                    with open(r'.\contact.txt', 'w') as new_file:
                        new_file.writelines(new_contact)
                    print('----------------------\nDelete contact:{} successfully!'.format(name))

                else:
                    print("----------------------\nDon't have this person in contact!")

        except Exception as e:
            print(e)
