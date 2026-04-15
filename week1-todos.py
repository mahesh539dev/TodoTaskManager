import datetime
import json
class TodoTasks:
    parser = argparse.ArgumentParser(description="Values for adding tasks")
    parser.add_argument("taskTitle", help="Title of the task") 
    parser.add_argument("completeBy", help="Task due date") 

    def __init__(self):
        self.tasks = self.loadFile()

        
    def addTask(self, taskTitle, completeBy):
        now = datetime.datetime.now()
        onlyDate = now.date()
        jsonValue = {
            "id": self.getNextId(),
            "taskTitle" : taskTitle,
            "taskStatus" : "PENDING",
            "createdAt" : str(self.onlyDate),
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
        except IOError as e:
               print(f"Error writing to file: {e}")
    
    def displayTask(self,task):
        if task["taskStatus"] == "Completed":
            print("✅", end=" ")
        else:
            print("❌", end=" ")
        print(task["id"],task["taskTitle"],task["createdAt"],task["completeBy"])
