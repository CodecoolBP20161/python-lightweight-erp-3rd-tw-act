# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# title: string
# price: number (the actual selling price in $)
# month: number
# day: number
# year: number
# month,year and day combined gives the date the purchase was made


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
    options = ["Show table", "Add new item", "Remove item", "Update item", "Lowest price item",
               "Items sold between dates"]
    while True:
        ui.print_menu("Selling submenu", options, "Back to Main menu")
        inputs = ui.get_inputs(["Please choose an option: "], "")
        option = inputs[0]
        table = data_manager.get_table_from_file(current_file_path + "/sellings.csv")
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
            lowest_price_item = get_lowest_price_item_id(table)
            title_list = "Lowest price item: {0}\n".format(lowest_price_item)
            ui.print_table("", title_list)
        elif option == "6":
            try:
                inputs_from = ui.get_inputs(["Items from this date in this (form:day-month-year) "], "")
                date_from_list = inputs_from[0].split("-")
                day_from = date_from_list[0]
                month_from = date_from_list[1]
                year_from = date_from_list[2]
                inputs_to = ui.get_inputs(["Items to this date (form:day-month-year) "], "")
                date_to_list = inputs_to[0].split("-")
                day_to = date_to_list[0]
                month_to = date_to_list[1]
                year_to = date_to_list[2]
                title_list = ["id", "title", "price", "month", "day", "year"]
                items_sold_table = get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
                ui.print_table(items_sold_table, title_list)
            except:
                ui.print_error_message("This date form is not accepted")
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
        pass


# print the default table of records from the file
def show_table(table):
    title_list = ["id", "title", "price", "month", "day", "year"]
    ui.print_table(table, title_list)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    title_list = ["title: ", "price: ", "month: ", "day: ", "year: "]
    temp_list = []
    new_line = [common.generate_random(table)]
    for i in range(len(title_list)):
        title_list[0] = title_list[i]
        temp_list.append(ui.get_inputs(title_list, "Give me a data!"))
        new_line.append(temp_list[i][0])
    table.append(new_line)
    data_manager.write_table_to_file(current_file_path + "/sellings.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):
    id_ = ui.get_inputs(["id: "], "Give me an id: ")
    for i in range(len(table)):
        if table[i][0] == id_[0]:
            del table[i]
            break
    data_manager.write_table_to_file(current_file_path + "/sellings.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):
    title_list = ["title: ", "price: ", "month: ", "day: ", "year: "]
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
    data_manager.write_table_to_file(current_file_path + "/sellings.csv", table)
    return table


# special functions:
# ------------------
# the question: What is the id of the item that sold for the lowest price ?
# return type: string (id)
# if there are more than one with the lowest price, return the first of descending alphabetical order


def get_lowest_price_item_id(table):
    for i in range(1, len(table)):
        while table[i][1].lower() < table[i - 1][1].lower():
            table.insert(i - 1, table[i])
            del table[i + 1]
            i = i - 1
            if i == 0:
                break
    sort_lines = table
    first_price = table[0][2]
    first_price_id = table[0][0]
    for i in range(len(sort_lines)):
        if int(first_price) > int(sort_lines[i][2]):
            first_price = sort_lines[i][2]
            first_price_id = sort_lines[i][0]

    return first_price_id


# the question: Which items are sold between two given dates ? (from_date < birth_date < to_date)
# return type: list of lists (the filtered table)
def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    date_from = int(str(year_from) + str(month_from) + str(day_from))
    date_to = int(str(year_to) + str(month_to) + str(day_to))
    results = []
    for line in table:
        date_today = int(str(line[5]) + str(line[3]) + str(line[4]))
        if (date_today > date_from) and (date_today < date_to):
            results.append(line)
    return results
