# implement commonly used functions here
import random

# generate and return a unique and random
# (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter) string
# it must be unique in the list
def generate_random(table):
    while True:
        capital_letter = random.sample(range(65, 91), 2)
        lower_case = random.sample(range(97, 123), 2)
        symbols = random.sample(range(33, 48), 2)
        random_number = random.sample(range(0, 10), 2)
        for i in range(0, len(random_number)):
            random_number[i] = str(random_number[i])
        random_list = capital_letter + lower_case + symbols
        n = 0
        mylist = random_list
        for i in random_list:
            mylist[n] = chr(i)
            n = n + 1
        mylist = mylist + random_number
        random.shuffle(mylist)
        password = "".join(mylist)
        boolean_generate = True
        for i in range(len(table)):
            if password == table[i][0]:
                boolean_generate = False
        if boolean_generate:
            return password
