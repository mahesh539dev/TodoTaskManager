import datetime
import json
class todoTasks:
    now = datetime.datetime.now()
    onlyDate = now.date()
    def __init__(self):
        self.tasks = self.loadFile()

        
    def addTask(self, taskTitle, completeBy):
        jsonValue = {
            "id": self.getNextId(),
            "taskTitle" : taskTitle,
            "taskStatus" : "PENDING",
            "createdAt" : str(self.onlyDate),
            "completeBy" : completeBy
        }
        self.tasks.append(jsonValue)
        self.writeToFile(self.tasks)
        self.__str__(jsonValue)
    
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
            max = 0
            for task in allTasks:
                if task['id'] > max:
                    max = task['id']
            return max+1
        
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
        except:
            print("Error occured while writing") 
    def __del__(self):
    # Close file when object is destroyed
        if hasattr(self, 'file'):
            self.file.close()
    
    def __str__(self,task):
        if task["taskStatus"] == "Completed":
            print("✅", end=" ")
        else:
            print("❌", end=" ")
        print(task["id"],task["taskTitle"],task["createdAt"],task["completeBy"])
todo = todoTasks()
print(todo.addTask("Buy groceries", "2026-04-20"))
todo.delById(2)
todo.updateStatus(5)