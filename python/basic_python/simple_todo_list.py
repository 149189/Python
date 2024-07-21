#Create a program where users can add, view, and delete tasks in a to-do list

def add(todo_list):
    task =input("What do you want to add: ")
    todo_list.append(task)
    print(f"'{task}'has been updated")

def view(todo_list):
    if not todo_list:
        print("Todo list is empty.")
    else:
        print("Your todo-list is :")
        for index,task in enumerate(todo_list,start=1):
            print(f"{index}.{task}")

def delete(todo_list):
    view(todo_list)
    if todo_list:
        try:
            task_num = int(input("Enter the number of task you want to delete"))
            if 1<= task_num<=len(todo_list):
                removed_task = todo_list.pop(task_num-1)
                print(f"'{removed_task}' has been removed from the list.")
            else:
                print("Invalid task number")
        except ValueError:
             print("please enter a valid number.")           
                                           

def main():
    todo_list = []

    while True:
        print("Welcome to our Todo list\n")
        print("What would you like to do?\n")
        print("1.Add\n2.View\n3.Delete\n4.Quit")

        try:
            num = int(input("Choose a number that you want to execute: "))
            if num == 1:
                add(todo_list)
            elif num==2:
                view(todo_list)
            elif num==3:
                delete(todo_list)
            elif num==4:
                print("Quiting...")
                break
            else:
                print("Choose valid number!")
        except ValueError:
               print("Choose valid number!")                    

if __name__=="__main__":
    main()

    
