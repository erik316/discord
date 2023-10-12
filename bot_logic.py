import random

def gen_pass(pass_length):
    elements = "1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,./<>?"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password