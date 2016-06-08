# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# manufacturer: string
# purchase_date: number (year)
# durability: number (year)


# importing everything you need
import os
import datetime
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
    options = ["Show table", "Add new item", "Remove item", "Update item", "Available tools",
               "The average durability time for each manufacturer"]
    while True:
        ui.print_menu("Tool Manager submenu", options, "Back to Main Menu")
        inputs = ui.get_inputs(["Please choose an option: "], "")
        option = inputs[0]
        table = data_manager.get_table_from_file(current_file_path + "/tools.csv")
        id_ = "0"
        if option == "1":
            show_table(table)
        elif option == "2":
            add(table)
        elif option == "3":
            remove(table, id_)
        elif option == "4":
            update(table, id_)
        elif option == "5":
            available_tools = get_available_tools(table)
            title_list = ["id", "name", "manufacturer", "purchase_date"]
            ui.print_table(available_tools, title_list)
        elif option == "6":
            avg = get_average_durability_by_manufacturers(table)
            avg_table = list(set(avg.items()))
            title_list = ["manufacturer", "average"]
            ui.print_table(avg_table, title_list)
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
        pass


# print the default table of records from the file
def show_table(table):
    title_list = ["id", "name", "manufacturer", "purchase_date", "durability"]
    ui.print_table(table, title_list)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    title_list = ["name: ", "manufacturer: ", "purchase_date: ", "durability: "]
    temp_list = []
    new_line = [common.generate_random(table)]
    for i in range(len(title_list)):
        title_list[0] = title_list[i]
        temp_list.append(ui.get_inputs(title_list, "Give me a data!"))
        new_line.append(temp_list[i][0])
    table.append(new_line)
    data_manager.write_table_to_file(current_file_path + "/tools.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):
    id_ = ui.get_inputs(["id: "], "Give me an id: ")
    for i in range(len(table)):
        if table[i][0] == id_[0]:
            del table[i]
            break
    data_manager.write_table_to_file(current_file_path + "/tools.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):
    title_list = ["name: ", "manufacturer: ", "purchase_date: ", "durability: "]
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
    data_manager.write_table_to_file(current_file_path + "/tools.csv", table)
    return table


# special functions:
# ------------------

# the question: Which items has not yet exceeded their durability ?
# return type: list of lists (the inner list contains the whole row with their actual data types)
def get_available_tools(table):
    title_list = ["id", "name", "manufacturer", "purchase_date", "durability"]
    actual_year = datetime.datetime.now().year
    table_available_tools = []
    for i in range(len(table)):
        if int(table[i][3]) + int(table[i][4]) >= actual_year:
            table_available_tools.append(table[i])
    for i in range(len(table_available_tools)):
        table_available_tools[i][3] = int(table_available_tools[i][3])
        table_available_tools[i][4] = int(table_available_tools[i][4])
    return table_available_tools


# the question: What are the average durability time for each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [avg] }
def get_average_durability_by_manufacturers(table):
    list_manufacturer = [table[i][2] for i in range(len(table))]
    list_durability = [table[i][4] for i in range(len(table))]
    count_manufacturer = [0] * len(list_manufacturer)
    count_durability = [0] * len(list_manufacturer)
    dict_average_by_manufacturer = {}
    for i in range(len(list_manufacturer)):
        for j in range(len(list_manufacturer)):
            if list_manufacturer[j] == list_manufacturer[i] and list_manufacturer[j] not in list_manufacturer[0:j]:
                count_manufacturer[j] += 1
                count_durability[j] = int(count_durability[j]) + int(list_durability[i])
    for i in range(len(count_manufacturer)):
        if count_manufacturer[i] != 0:
            dict_average_by_manufacturer[list_manufacturer[i]] = count_durability[i]/count_manufacturer[i]
    return dict_average_by_manufacturer
