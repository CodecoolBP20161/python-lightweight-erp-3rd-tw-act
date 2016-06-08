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
# Data manager module
data_manager = SourceFileLoader("data_manager", current_file_path + "/../data_manager.py").load_module()
# Common interface module
common = SourceFileLoader("common", current_file_path + "/../common.py").load_module()


# start this manager by a menu
def start():
    options = ["Show table", "Add new item", "Remove item", "Update item", "Different kind of games(per manufacturer)",
               "Average amount of games in stock(per manufacturer)"]
    while True:
        ui.print_menu("Store submenu", options, "Back to Main menu")
        inputs = ui.get_inputs(["Please choose an option: "], "")
        option = inputs[0]
        table = data_manager.get_table_from_file(current_file_path + "/games.csv")
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
            dict_games_kind = get_counts_by_manufacturers(table)
            dict_games_kind_table = list(set(dict_games_kind.items()))
            title_list = ["manufacturer", "count"]
            ui.print_table(dict_games_kind_table, title_list)
        elif option == "6":
            inputs = ui.get_inputs(["Please choose a manufacturer: "], "")
            manufacturer = inputs[0]
            try:
                avg_amount = get_average_by_manufacturer(table, manufacturer)
                title_list = "Average amount of games in stock by {0}: {1}".format(manufacturer, avg_amount)
                ui.print_table("", title_list)
            except:
                ui.print_error_message("There is no manufacturer named {0} in the examined file".format(manufacturer))
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
        pass


# Print the default table of records from the file
def show_table(table):
    title_list = ["ID", "Title", "Manufacture", "Price", "In stock"]
    ui.print_table(table, title_list)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    title_list = ["Title: ", "Manufacture: ", "Price: ", "In stock: "]
    common.comm_add(table, title_list)
    data_manager.write_table_to_file(current_file_path + "/games.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):
    common.comm_remove(table)
    data_manager.write_table_to_file(current_file_path + "/games.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):
    title_list = ["Title: ", "Manufacture: ", "Price: ", "In stock: "]
    common.comm_update(table, title_list)
    data_manager.write_table_to_file(current_file_path + "/games.csv", table)
    return table


# Special functions:
# ------------------

# the question: How many different kinds of game are available of each manufacturer?
# return type: a dictionary with this structure: { [manufacturer] : [count] }
def get_counts_by_manufacturers(table):
    data = {}
    for i in range(len(table)):
        stat = table[i][2] in data
        if stat is not True:
            data[table[i][2]] = 1
        else:
            data[table[i][2]] += 1
    return data


# the question: What is the average amount of games in stock of a given manufacturer?
# return type: number
def get_average_by_manufacturer(table, manufacturer):
    all_stock = 0
    count = 0
    for i in range(len(table)):
        if manufacturer == table[i][2]:
            all_stock += int(table[i][4])
            count += 1
    res = all_stock/count
    return res
