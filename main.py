items = []
selection = 1
while selection != 0:
    print("Type one of the following actions:")
    print('"Add" - to add a new item.')
    print('"Show" - to show all the items.')
    print('"Complete" - to mark an item as complete/done.')
    print('"Exit" - to exit the program.')
    user_input = input("--> ")
    user_input = user_input.strip().capitalize()
    match user_input:
        case "Add":
            item = input("Add a new item: ") + "\n"
            file = open("todos.txt", "r")
            todos = file.readlines()
            todos.append(item)
            file.close()

            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "Show":
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                item_with_index = f'{index+1}. {item}'
                print(item_with_index.replace("\n", ""))
        case "Edit":
            print("Please enter the index number of the item.")
            item_index = int(input("---> "))
            item_index_reduced = item_index - 1
            print("Please enter the new info.")
            new_item = input("---> ")
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()
            todos[item_index_reduced] = new_item + "\n"
            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "Complete":
            print("Please enter the index number of the item.")
            item_index = int(input("---> "))
            item_index_reduced = item_index - 1
            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()
            todos.pop(item_index_reduced)
            file = open("todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "Exit":
            break
        case _:
            print("Action unknown, please select from  the list provided.")
