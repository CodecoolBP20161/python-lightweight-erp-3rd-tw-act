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
    options = ["Show table", "Add new item", "Remove item", "Update item", "Year with the highest profit",
               "Average profit(per item) in a given year"]
    while True:
        ui.print_menu("Accounting submenu", options, "Go back to the main menu")
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
        elif option == "5":
            year = which_year_max(table)
            title_list = "Year with the highest profit: {0}\n".format(year)
            ui.print_table("", title_list)
        elif option == "6":
            inputs = ui.get_inputs(["Please choose a year: "], "")
            year = int(inputs[0])
            try:
                avg_profit = avg_amount(table, year)
                title_list = "Average profit(per item) in {0}: {1}\n".format(year, avg_profit)
                ui.print_table("", title_list)
            except:
                ui.print_error_message("There is no year {0} in the examined file".format(year))
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
    common.comm_add(table, title_list)
    data_manager.write_table_to_file(current_file_path + "/items.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):
    common.comm_remove(table)
    data_manager.write_table_to_file(current_file_path + "/items.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return the @table
def update(table, id_):
    title_list = ["month: ", "day: ", "year: ", "type: ", "amount: "]
    common.comm_update(table, title_list)
    data_manager.write_table_to_file(current_file_path + "/items.csv", table)
    return table


# special functions:
# ------------------

# the question: Which year has the highest profit? (profit=in-out)
# return the answer (number)
def which_year_max(table):
    list_year = [table[i][3] for i in range(len(table))]
    years = [list_year[0]]
    for i in list_year:
        if i not in years:
            years.append(i)
    profit = [0]*len(years)
    list_type = [table[i][4] for i in range(len(table))]
    list_amount = [table[i][5] for i in range(len(table))]
    for i in range(len(table)):
        for j in range(len(years)):
            if list_year[i] == years[j]:
                if list_type[i] == "in":
                    profit[j] += int(list_amount[i])
                if list_type[i] == "out":
                    profit[j] -= int(list_amount[i])
    for i in range(len(years)):
        if profit[i] == max(profit):
            return int(years[i])


# the question: What is the average (per item) profit in a given year? [(profit)/(items count) ]
# return the answer (number)
def avg_amount(table, year):
    profit = 0
    counter_year = 0
    list_year = [table[i][3] for i in range(len(table))]
    list_type = [table[i][4] for i in range(len(table))]
    list_amount = [table[i][5] for i in range(len(table))]
    for i in range(len(table)):
        if int(list_year[i]) == year:
            counter_year += 1
            if list_type[i] == "in":
                profit += int(list_amount[i])
            if list_type[i] == "out":
                profit -= int(list_amount[i])
    avg_amount = profit/counter_year
    return avg_amount
