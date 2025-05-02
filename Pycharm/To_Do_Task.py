print ("Welcome to Task Manager!")

print ("1. Display tasks")

print ("2. Add new task")

print ("3. Delete task")

print ("4. Edit task")

print ("5. Exit")

task_list = []

def print_lists(value):
    c = 1
    for i in value:
        print (str(c) + ". " + i)
        c += 1
        print("\n")


def perform(val):
    global task_list
    if val == 1:
        # Display task
        if len(task_list) != 0:
            print_lists(task_list)


        else:
            print ("There are no tasks to display. Please add a task first.")


    elif val == 2:
        # Add new task

        new_val = input("Enter name of new task: ")

        print("\n")
        
        task_list += [new_val]
        print(len(task_list))
        # print_lists(task_list)

        check = input("Successfully added task! Would you like to see it? (Yes or No): ")

        if check == "Yes" or "yes":
            print_lists(task_list)

        else:
            print("Okay! \n")

    elif val == 3:
        # Delete task
        if len(task_list) != 0:
            delete_val = input("Select task to delete: ")

            print (task_list)

            task_list.remove(delete_val)

            print ("Successfully removed task!")

        else:
            print("There are no tasks to remove. Please add a task first.")

    select()





def select():
    choice = input("Select option: ")

    if 0 < int(choice) < 6:
        perform(int(choice))

    else:
        print("That is an invalid option.")
        select()

select()