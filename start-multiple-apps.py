import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]

def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    fileName = filedialog.askopenfilename(initialdir = "/", title="Select File", filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    apps.append(fileName)
    print(fileName)
    for app in apps: 
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

canvas = tk.Canvas(root, height=400, widt=300, bg="#263D42")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.6, rely=0.1, relx=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#002d40", command=addApp)
openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5, fg="white", bg="#022400", command=runApps)
runApps.pack()

for app in apps: 
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

# After program closes, run this
with open('save.txt', 'w') as f:    # open a file, if it's null, make one. w for write 
    for app in apps:
        f.write(app + ',')