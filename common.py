# implement commonly used functions here
import random
import string

# generate and return a unique and random
# (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter) string
# it must be unique in the list
def generate_random(table):
    while True:
        password_list = [""] * 8
        password_list[0] = random.choice(string.ascii_uppercase)
        password_list[1] = random.choice(string.ascii_uppercase)
        password_list[2] = random.choice(string.ascii_lowercase)
        password_list[3] = random.choice(string.ascii_lowercase)
        password_list[4] = random.choice(string.digits)
        password_list[5] = random.choice(string.digits)
        password_list[6] = random.choice(r"[!@#$%^&*()?]")
        password_list[7] = random.choice(r"[!@#$%^&*()?]")
        joined_item = "".join(password_list)
        boolean_generate = True
        for i in range(len(table)):
            if joined_item == table[i][0]:
                boolean_generate = False
        if boolean_generate:
            return joined_item
