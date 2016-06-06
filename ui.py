

# An example output:
# /-----------------------------------\
# |   id   |      title     |  type   |
# |--------|----------------|---------|
# |   0    | Counter strike |    fps  |
# |--------|----------------|---------|
# |   1    |       fo       |    fps  |
# \-----------------------------------/
def print_table(table, title_list):
    max_len_items = table[0][0]
    for i in range(len(table)):
        for j in range(len(title_list)):
            if len(table[i][j]) > len(max_len_items):
                max_len_items = table[i][j]
    max_len_items = len(max_len_items)
    max_len_titles = len(max(title_list, key=len))
    max_len_all = max_len_items
    if max_len_titles > max_len_items:
        max_len_all = max_len_titles
    dynamic_row_length = len(title_list)*(max_len_all+2)+(len(title_list)-2)
    print("|", "-"*dynamic_row_length, "|")
    print(("|{:^{a}}"*len(title_list)).format(*title_list, a=max_len_all+2), "|")
    for i in range(len(table)):
        print("|", "-"*dynamic_row_length, "|")
        print(("|{:^{a}}"*len(title_list)).format(*table[i], a=max_len_all+2), "|")
    print("|", "-"*dynamic_row_length, "|")

    pass


# An example output:
# Main menu:
# (1) Store manager
# (2) Human resources manager
# (3) Inventory manager
# (4) Accounting manager
# (5) Selling manager
# (6) Customer relationship management (CRM)
# (0) Exit program
#
# see the function call in main.py
def print_menu(title, list_options, exit_message):

    # your code

    pass


# see the function call in main.py
def get_inputs(list_titles, title):
    record = []

    # your code

    return record


# see the function call in main.py
def print_error_message(message):

    # your code

    pass
