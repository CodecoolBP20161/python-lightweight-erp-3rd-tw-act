# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# month: number
# day: number
# year: number
# type: string (in = income, out = outcome)
# amount: number (dollar)


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
    while True:
        ui.print_menu("Accounting submenu", options, "Exit program")
        inputs = ui.get_inputs(["Please choose an option: "], "")
        option = inputs[0]
        table = data_manager.get_table_from_file(current_file_path + "/items.csv")
        id_ = "0"
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            remove(table, id_)
        elif option == "4":
            update(table, id_)
        # elif option == 5:
        # elif option == 6:
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
        # you code

        pass


# print the default table of records from the file
def show_table(table):
    title_list = ["id", "month", "day", "year", "type", "amount"]
    ui.print_table(table, title_list)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    title_list = ["month: ", "day: ", "year: ", "type: ", "amount: "]
    temp_list = []
    new_line = [common.generate_random(table)]
    for i in range(len(title_list)):
        title_list[0] = title_list[i]
        temp_list.append(ui.get_inputs(title_list, "Give me a data!"))
        new_line.append(temp_list[i][0])
    table.append(new_line)
    data_manager.write_table_to_file(current_file_path + "/items.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):
    id_ = ui.get_inputs(["id: "], "Give me an id: ")
    for i in range(len(table)):
        if table[i][0] == id_[0]:
            del table[i]
            break
    data_manager.write_table_to_file(current_file_path + "/items.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return the @table
def update(table, id_):
    title_list = ["month: ", "day: ", "year: ", "type: ", "amount: "]
    temp_list = []
    id_ = ui.get_inputs(["id: "], "Give me an id: ")
    new_line = []
    new_line.append(id_[0])
    for i in range(len(title_list)):
        title_list[0] = title_list[i]
        temp_list.append(ui.get_inputs(title_list, "Give me a data!"))
        new_line.append(temp_list[i][0])
    for i in range(len(table)):
        if table[i][0] == id_[0]:
            table[i] = new_line
    data_manager.write_table_to_file(current_file_path + "/items.csv", table)
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out) (2015 or 2016)
# return the answer (number)
def which_year_max(table):

    # your code

    pass


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):

    # your code

    pass
