def add_task(tasks):
    user_confirm = input("Are you sure you want to add a new task(y/n)")
    if (user_confirm =='y'):
        task = input("Enter new task")
        tasks.append(task)
        for i in range(len(tasks)):
            print(tasks[i])
    print( tasks[i]+ " is added!\n")
    main()
        


def delte_task(tasks):
    for i in range(len(tasks)):
        print(tasks[i])
    marked = int(input("Which task would you like to mark as complete(tasks shown above)(1-5")) - 1
    tasks[" "] =  tasks.append[marked]
    print("task deleted")
    main()


def view(tasks):
    if (len(tasks) == 0):
        print("Your day is free!")
        main()
    else:
        for i in range(len(tasks)):
            print(tasks[i])
        main()

def main():
    print("Welcome!")
    print("View All Tasks(1) ")
    print("To Add new Tasks(2)")
    print("Mark Task as complete(3)")
    print("")
    tasks =['']

    user1 = int(input("Choose action # 1-5"))
    if (user1 == 1):
        view(tasks)
    if (user1 == 2):
        add_task(tasks) 
    if (user1 == 3):
        delte_task(tasks)
    else:
        print("Please enterr a vaild #")
        


if __name__ == "__main__":
    main()