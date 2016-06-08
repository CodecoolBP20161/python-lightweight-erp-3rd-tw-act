# data structure:
# id: string
#     Unique and random generated (at least 2 special char()expect: ';'), 2 number, 2 lower and 2 upper case letter)
# name: string
# birth_date: number (year)


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
    options = ["Show table", "Add new item", "Remove item", "Update item", "Oldest person",
               "Person closest to the average age"]
    while True:
        ui.print_menu("Human Resource submenu", options, "Back to Main menu")
        inputs = ui.get_inputs(["Please choose an option: "], "")
        option = inputs[0]
        table = data_manager.get_table_from_file(current_file_path + "/persons.csv")
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
            oldest_persons = get_oldest_person(table)
            title_list = "Oldest persons are:"
            ui.print_table("", title_list)
            for i in range(len(oldest_persons)):
                persons_list = oldest_persons[i]
                ui.print_table("", persons_list)
            ui.print_table("", "\n")
        elif option == "6":
            closest_persons = get_persons_closest_to_average(table)
            title_list = "Persons closest to the average age:"
            ui.print_table("", title_list)
            for i in range(len(closest_persons)):
                persons_list = closest_persons[i]
                ui.print_table("", persons_list)
            ui.print_table("", "\n")
        elif option == "0":
            break
        else:
            raise KeyError("There is no such option.")
        pass


# print the default table of records from the file
def show_table(table):
    title_list = ["id", "name", "birth date"]
    ui.print_table(table, title_list)
    pass


# Ask a new record as an input from the user than add it to @table, than return @table
def add(table):
    title_list = ["name: ", "birth date: "]
    temp_list = []
    new_line = [common.generate_random(table)]
    for i in range(len(title_list)):
        title_list[0] = title_list[i]
        temp_list.append(ui.get_inputs(title_list, "Give me a data!"))
        new_line.append(temp_list[i][0])
    table.append(new_line)
    data_manager.write_table_to_file(current_file_path + "/persons.csv", table)
    return table


# Remove the record having the id @id_ from the @list, than return @table
def remove(table, id_):
    id_ = ui.get_inputs(["id: "], "Give me an id: ")
    for i in range(len(table)):
        if table[i][0] == id_[0]:
            del table[i]
            break
    data_manager.write_table_to_file(current_file_path + "/persons.csv", table)
    return table


# Update the record in @table having the id @id_ by asking the new data from the user,
# than return @table
def update(table, id_):
    title_list = ["name: ", "birth date: "]
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
    data_manager.write_table_to_file(current_file_path + "/persons.csv", table)
    return table


# special functions:
# ------------------

# the question: Who is the oldest person ?
# return type: list of strings (name or names if there are two more with the same value)
def get_oldest_person(table):
    oldest_year = table[0][2]
    oldest = [table[0][1]]
    for i in range(len(table)):
        if int(table[i][2]) < int(oldest_year):
            oldest_year = table[i][2]
            oldest = [table[i][1]]
        elif int(table[i][2]) == int(oldest_year):
            oldest.append(table[i][1])
    return oldest


# the question: Who is the closest to the average age ?
# return type: list of strings (name or names if there are two more with the same value)
def get_persons_closest_to_average(table):
    sum_year = 0
    for i in range(len(table)):
        sum_year = sum_year + int(table[i][2])
    average = int(sum_year/len(table))
    smallest_difference = abs(average - int(table[0][2]))
    closest_person = [table[0][1]]
    for i in range(len(table)):
        if abs(average - int(table[i][2])) < int(smallest_difference):
            closest_person = [table[i][1]]
            smallest_difference = abs(average - int(table[i][2]))
        elif abs(average - int(table[i][2])) == int(smallest_difference):
            closest_person.append(table[i][1])
    return closest_person
