import datetime
import json
import argparse

class TodoTasks:
    def __init__(self):
        self.tasks = self.loadFile()

        
    def addTask(self, taskTitle, completeBy):
        now = datetime.datetime.now()
        onlyDate = now.date()
        jsonValue = {
            "id": self.getNextId(),
            "taskTitle" : taskTitle,
            "taskStatus" : "PENDING",
            "createdAt" : str(onlyDate),
            "completeBy" : completeBy
        }
        self.tasks.append(jsonValue)
        self.writeToFile(self.tasks)
        self.displayTask(jsonValue)
        
    def listTasks(self):
        if not self.tasks:
           print("No tasks found")
           return
        for task in self.tasks:
           self.displayTask(task)
            
    def delById(self, delId):
        allTasks = self.tasks
        if not allTasks:
            print("No tasks to delete")
        else:
            task_found = False
            for task in allTasks:
                if task['id'] == delId:
                    self.tasks.remove(task)
                    self.writeToFile(self.tasks)
                    print(f"Deleted task {delId}")
                    task_found = True
                    break
            if not task_found:
                print(f"Task with id {delId} doesn't exist")
    
    def updateStatus(self,taskId):
        allTasks = self.tasks
        if not allTasks:
            print("No tasks to update")
        else:
            task_found = False
            for task in allTasks:
                if task['id'] == taskId:
                    task['taskStatus'] = "Completed"
                    self.writeToFile(self.tasks)
                    print(f"Updated task {taskId} status to Completed")
                    task_found = True
                    break
            if not task_found:
                print(f"Task with id {taskId} doesn't exist")
                
    def getNextId(self):
        allTasks = self.tasks
        if not allTasks:
            return 1
        else:
            max_id = 0
            for task in allTasks:
                if task['id'] > max_id:
                    max_id = task['id']
            return max_id+1
        
    def loadFile(self):
        try:
            with open("tasks.json", "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def writeToFile(self, tasks):
        try:
            with open("tasks.json","w") as f:
                json.dump(tasks, f, indent=2)
        except IOError as e:
               print(f"Error writing to file: {e}")
    
    def displayTask(self,task):
        if task["taskStatus"] == "Completed":
            print("✅", end=" ")
        else:
            print("❌", end=" ")
        print(task["id"],task["taskTitle"],task["createdAt"],task["completeBy"])
def main():
    todo = TodoTasks()

    parser = argparse.ArgumentParser(description="Todo Task Manager")
    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("due", help="Due date e.g. 2026-04-20")

    # list
    subparsers.add_parser("list")

    # delete
    del_parser = subparsers.add_parser("delete")
    del_parser.add_argument("id", type=int, help="Task ID")

    # complete
    comp_parser = subparsers.add_parser("complete")
    comp_parser.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args()

    if args.command == "add":
        todo.addTask(args.title, args.due)
    elif args.command == "list":
        todo.listTasks()
    elif args.command == "delete":
        todo.delById(args.id)
    elif args.command == "complete":
        todo.updateStatus(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
