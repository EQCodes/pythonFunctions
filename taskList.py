
tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]

print("Welcome to your terrific task planner!")

# 1. Print a list of uncompleted tasks
def getUncompleted(list):
    uncompletedTasks = []
    for task in list:
        if task["completed"] == False:
            uncompletedTasks.append(task["description"])
    return (str("The tasks you have still to complete are: ") + ', '.join(uncompletedTasks))
print(getUncompleted(tasks))

# 2. Print a list of completed tasks
def getCompleted(list):
    completedTasks = []
    for task in list:
        if task["completed"] == True:
            completedTasks.append(task["description"])
    return (str("The tasks you have completed are: ") + ', '.join(completedTasks))
print(getCompleted(tasks))

# 3. Print a list of all task descriptions
def displayTasks(list):
    allTasks = []
    for task in list:
        allTasks.append(task["description"])
    return (str("This is your full list of tasks: ") + ', '.join(allTasks))
print(displayTasks(tasks))

# 4. Print a list of tasks that take less than 20 minutes to complete
def getWeeTasks(list, time):
    weeTasks = []
    for task in list:
        if task["time_taken"] < time:
            weeTasks.append(task["description"])
    return str("The tasks that take less than ") + str(time) + str(" minutes are: ") + ', '.join(weeTasks)
print(getWeeTasks(tasks, 20))

# 5. Print any task with a given description
def getFaveTask(list, faveTask):
    for task in list:
        if task["description"] == faveTask:
            return (str("The best task to do is: ") + task["description"])
print(getFaveTask(tasks, "Walk Dog"))

# 6. Given a description update that task to mark it as complete.
def markComplete(list, completedTask):
    for task in list:
        if task["description"] == completedTask:
            task["completed"] = True
            return f'Well done, the completed status of {task["description"]} is now {task["completed"]}'

print(markComplete(tasks, "Wash Dishes"))

# 7. Add a task to the list
def addTask(list, taskName, taskStatus, taskDuration):
    list.append(
        {'description': taskName,
         'completed': taskStatus,
         'time_taken': taskDuration}
    )
    return f"Woo, you added {list[-1]['description']} to the list of tasks!"

print(addTask(tasks, "Hoovering", False, 20))


