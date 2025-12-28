from random import choices, choice, shuffle
import argparse
import string


def password_generator(length = 12, uppercase = False, lowercase = False, digit = False, special = False):
    if length < 8:
        raise ValueError("Password should contain at least 8 characters")
    password = ""
    to_choose = ''
    weight = []
    if lowercase:
        to_choose += string.ascii_lowercase
        password += choice(string.ascii_lowercase)
        if not uppercase:
            weight.extend([2] * len(string.ascii_lowercase))
        else:
            weight.extend([1.5] * len(string.ascii_lowercase))

    if uppercase:
        to_choose += string.ascii_uppercase
        password += choice(string.ascii_uppercase)
        if not lowercase:
            weight.extend([2] * len(string.ascii_lowercase))
        else:
            weight.extend([1.5] * len(string.ascii_lowercase))

    if digit:
        to_choose += string.digits
        password += choice(string.digits)
        weight.extend([2] * len(string.digits))

    if special:
        to_choose += string.punctuation
        password += choice(string.punctuation)
        weight.extend([1] * len(string.punctuation))

    if not to_choose:
        raise ValueError("At least one character type must be selected")
    password += "".join(choices(to_choose, weights=weight, k=length - len(password)))

    password = list(password)
    shuffle(password)
    return "".join(password)


parser = argparse.ArgumentParser(description="Password generator")
parser.add_argument("length", type=int, help="Length of the expected password")
parser.add_argument("-u", action="store_true", help="Include UPPER CASE symbols")
parser.add_argument("-l", action="store_true", help="Include lower case symbols")
parser.add_argument("-d", action="store_true", help="Include digits")
parser.add_argument("-s", action="store_true", help="Include special symbols")

args = parser.parse_args()

print(password_generator(
    length=args.length,
    uppercase=args.u,
    lowercase=args.l,
    digit=args.d,
    special=args.s
))