from tkinter import *
from tkinter import ttk 

root = Tk()
root.title("ToDo")

mainFrame = ttk.Frame(root, padding= "3 3 12 12")
mainFrame.grid(column= 0, row = 0, sticky= (N,W,E,S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)


taskAdd = ttk.Entry(mainFrame)
taskAdd.grid(column= 1, row= 1, sticky=(W))

def taskText():
    taskContainer = Frame(mainFrame)
    taskContainer.grid(sticky=(W))

    
    taskTxt = ttk.Label(taskContainer,text= taskAdd.get())
    taskTxt.grid(sticky=(W))

    taskDoneButton = ttk.Button(taskContainer, command= taskContainer.destroy, text= "Task Complete")
    taskDoneButton.grid(sticky=(W), padx= 10)

taskAddButton = ttk.Button(mainFrame,command = taskText, text= "AddTask")
taskAddButton.grid(column= 2, row = 1,sticky=(W))
mainFrame.mainloop()
