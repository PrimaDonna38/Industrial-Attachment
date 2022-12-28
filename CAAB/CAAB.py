import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.tix import ComboBox

root=tk.Tk()
root.geometry("650x500")
root.title("CAAB")

def creation():
    from EmployeeCreation import runner2
    runner2()

def setup():
    from UserSetup import runner
    runner()

def deduction():
    from AllowanceDeduction import runner3
    runner3()

button1=tk.Button(root, height=3, width=50, text="Employee ID Creation", font=('Arial', 14), command=creation)
button1.pack(padx=10, pady=30)

button2=tk.Button(root, height=3, width=50, text="User Setup", font=('Arial', 14), command=setup)
button2.pack(padx=10, pady=30)

button3=tk.Button(root, height=3, width=50, text="Allowance & Deduction", font=('Arial', 14), command=deduction)
button3.pack(padx=10, pady=30)

root.mainloop()

