# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# manufacturer: string
# price: number (dollar)
# in_stock: number


# importing everything you need
import os
from importlib.machinery import SourceFileLoader
current_file_path = os.path.dirname(os.path.abspath(__file__))
# User interface module
ui = SourceFileLoader("ui", current_file_path + "/../ui.py").load_module()
# data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# common interface module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this manager by a menu
def start():
    options = ["Show table", "Add new item", "Remove item", "Update item"]
    ui.print_menu("Store submenu", options, "Exit program")
    inputs = ui.get_inputs(["Please choose an option: "], "")
    option = inputs[0]
    table = data_manager.get_table_from_file(current_file_path + "/games.csv")
    if option == "1":
        # print("show_table")
        show_table(table)
    elif option == "2":
        print("add")
        # add(table)
    elif option == "3":
        print("remove")
        # remove(table, id_)
    elif option == "4":
        print("update")
        # update(table, id_)
    elif option == "0":
        pass
    else:
        raise KeyError("There is no such option.")

    pass


# print the default table of records from the file
def show_table(table):
    title_list = ["ID", "Title", "Manufacture", "Price", "In stock"]
    ui.print_table(table, title_list)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):

    # your code

    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):

    # your code

    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):

    # your code

    return table


# special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):

    # your code

    pass


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):

    # your code

    pass
