office_tasklist = []           #first define a list

def add_task():                #define add function
    task = input("Please insert a task you want to add to your office tasklist:")
    if task:
        office_tasklist.append(task)
        print(f"The task {task} was added to your list")
    else:
        print("Your tasklist is emty.")
add_task()

def show_tasklist():                #define show tasklist fuction
    if office_tasklist == None:     # check if tasklist is empty
        print("Your tasklist is empty.") 
    else:
        for task in office_tasklist: #entre a for - loop to print the input of the user
            print("Your tasklist:")
            print(task)


def main():                             # define main function
    while True:                         # while true do loop
        print("1. Add a task.")
        print(" Show the list.")
        print(" End the programm.")
        choice = input("Please make your choice") #ask a user to make a choice
        if choice == "1":
            add_task()
        elif choice =="2":
            show_tasklist()
        elif choice == "3":
            print("Goodbye.")   
            break                       # break to end the while - loop
if __name__ == "main":                    # control function
    main()

