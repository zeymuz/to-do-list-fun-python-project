# TO DO LIST 

print("TO DO LIST")
user_input = input("would you like to | VIEW | ADD | REMOVE | EXIT | your list?").lower()

to_do_list = open("text.txt", "r")


# ADDS ITEMS TO THE TO DO LIST
while user_input == "add":
    add = input("what would you like to add to your list,\ntype stop to exit\n").lower()

    #IF USER INPUT IS STOP IT QUITS THE LIST AND IT SHOWS IT AS WELL
    if add == "stop":
        print(to_do_list.read())
        print("restart the program to reuse list please")
        break

    #
    else:
        file = open("text.txt", "a")
        file.write(add + "\n")
        file.close
        print(to_do_list.read())
        

# VIEWS ITEMS FROM THE TO DO LIST 
while user_input == "view":
    file = open("text.txt", "a")
    print(to_do_list.read())
    file.close
    print("to run program again press: ctrl+alt+a ")
    break


#REMOVES ITEMS FROM THE TO DO LIST
while user_input == "remove":
    
    
    print(to_do_list.read())
    text_to_remove = input("Enter the text you want to remove type STOP to quit program: ").lower()

    #RUNS THROUGH THE TEXT.TXT FILE AND REMOVES SPECIFIED ITEMS
    with open("text.txt", 'r+', encoding='utf-8') as file:
        content = file.read().replace(text_to_remove, '')
        file.seek(0)
        file.write(content)
        file.truncate()

        print(f"Removed all occurrences of '{text_to_remove}' from {"text.txt"}.")

#IF TEXT TO REMOVE IS STOP, IT STOPS THE PROGRAM
    if text_to_remove == "stop":
        print(to_do_list.read())
        print("to run program again press: crtl+alt+a ")
        break
        

#EXITS THE PROGRAM
while user_input == "exit":
    print("to run program again press ctrl+alt+a      bye bye!!")
    break
