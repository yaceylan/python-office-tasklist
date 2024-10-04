office_tasklist = []           #first define a list

def add_task():                #define add function
    task = input("Please insert a task you want to add to your office tasklist:")
    if task:
        office_tasklist.append(task)
        print(f"The task {task} was added to your list")
    else:
        print("Your tasklist is emty.")
add_task()


# def main():                             #define a main function
 # while True:
 #if
 
faelligkeitsdatum = input("Bitte geben Sie das Fälligkeitsdatum im Format TT.MM.JJJJ ein: ")
print("Das eingegebene Fälligkeitsdatum ist:", faelligkeitsdatum)
