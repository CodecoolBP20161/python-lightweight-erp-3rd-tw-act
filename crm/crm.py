# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# email: string
# subscribed: boolean (Is she/he subscribed to the newsletter? 1/0 = yes/not)


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
        ui.print_menu("CRM", options, "Exit program")
        inputs = ui.get_inputs(["Please choose an option: "], "")
        option = inputs[0]
        table = data_manager.get_table_from_file(current_file_path + "/customers.csv")
        id_ = "0"
        if option == "0":
            break
        elif option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            remove(table, id_)
        elif option == "4":
            update(table, id_)
        else:
            raise KeyError("There is no such option.")
        pass


# print the default table of records from the file
def show_table(table):
    title_list = ["id", "name", "email", "subscribed"]
    ui.print_table(table, title_list)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    title_list = ["name: ", "email: ", "subscribe: "]
    temp_list = []
    new_line = [common.generate_random(table)]
    for i in range(len(title_list)):
        title_list[0] = title_list[i]
        temp_list.append(ui.get_inputs(title_list, "Give me a data!"))
        new_line.append(temp_list[i][0])
    table.append(new_line)
    data_manager.write_table_to_file(current_file_path + "/customers.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):
    id_ = ui.get_inputs(["id: "], "Give me an id: ")
    for i in range(len(table)):
        if table[i][0] == id_[0]:
            del table[i]
            break
    data_manager.write_table_to_file(current_file_path + "/customers.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):
    title_list = ["name: ", "email: ", "subscribe: "]
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
    data_manager.write_table_to_file(current_file_path + "/customers.csv", table)
    return table


# special functions:
# ------------------


# the question: What is the id of the customer with the longest name ?
# return type: string (id) - if there are more than one longest name, return the first of ascending alphabetical order
def get_longest_name_id(table):
    datalines = data_manager.get_table_from_file(current_file_path + "/customers.csv")
    for i in range(1, len(datalines)):
        while datalines[i][1].lower() < datalines[i - 1][1].lower():
            datalines.insert(i - 1, datalines[i])
            del datalines[i + 1]
            i = i - 1
            if i == 0:
                break
    sort_lines = datalines
    longest_name = 0
    for i in sort_lines:
        if len(i[1]) > longest_name:
            longest_name = len(i[1])
            longest_id = i[0]
    return longest_id

# the question: Which customers has subscribed to the newsletter?
# return type: list of string (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):

    # your code

    pass
