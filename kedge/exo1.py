import re
from utils import read_file, write_to_file

def validate_email(email: str):
    return re.search(
        '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',
        email
    )

for email in read_file("email.txt"):
    if validate_email(email):
        continue
    write_to_file("invalid.txt", email + "\n")

def refined_validate_email(email: str):
    return re.search(
        '^((\w|\d){6,})+[@]\w+[.]\w{2,3}$',
        email
    )

def register_account() -> tuple:
    return input("Write Account name"), input("Write Your email")

def main():
    acc, email = register_account()
    acc_expected_lght = 6

    if len(acc) < acc_expected_lght:
        print('Invalid account length, expected %s' % acc_expected_lght)
        exit(1)

    if not refined_validate_email(email):
        print('invalid email', email)
        write_to_file("refined.txt", email + "\n")

main()
