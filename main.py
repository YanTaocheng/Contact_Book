# _*_ coding:utf-8 _*_
import add_contact, delete_contact, modify_contact, query_contact


def main():
    print(
        '----------------------\nThis is a contact book, you can choose: \n1.add contact \n2.delete_contact \n3.modify contact \n4.query_contact')
    choice = input('----------------------\nWhat do you want to do(1/2/3/4):')

    with open(r'.\contact.txt', 'a') as f:
        f.write('')

    if choice == '1':
        add_contact.add_contact()

    if choice == '2':
        delete_contact.delete_contact()

    if choice == '3':
        modify_contact.modify_contact()

    if choice == '4':
        query_contact.query_contact()

    main()


if __name__ == '__main__':
    main()
