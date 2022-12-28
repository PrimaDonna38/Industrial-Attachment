import tkinter as tk
from tkinter import *
from tkinter import ttk
import robot
from PictureUpload import runner1

def run2():
     robot.run("EmployeeCreation.robot")

def runner2():
    global picture
    picture=r'avatar.png'
    
    def get_variables():
        
        global english,bangla,year,picture
        english=e1.get()
        bangla=e2.get()
        year=header_selection.get()

        print(english,bangla)
        file= open("F:/CAAB/EmployeeCreation.txt", "w")
        file.write( english)
        file.write("\n")
        file.write(bangla)
        file.write("\n")
        file.write(year)
        file.write("\n")
        
        # from try1c import runner
        # picture=runner("x")
        file.write(picture)
        file.close()
        run2()
        

    root1=tk.Tk()
    root1.geometry("650x500")
    root1.title("Employee ID Creation")

    name_english=tk.Label(root1,font=('Arial', 12), text="Employee Name (in english)")
    name_english.grid(row=0,column=0,padx=10,pady=10)

    e1= Entry(root1, width=60, )
    e1.grid(row=0,column=1,padx=10,pady=10)


    name_bangla=tk.Label(root1, text="Employee Name (in Bengali)",font=('Arial', 12))
    name_bangla.grid(row=1,column=0,padx=10,pady=10)
    
    e2= Entry(root1, width=60)
    e2.grid(row=1,column=1,padx=10,pady=10)

    year=tk.Label(root1,font=('Arial', 12), text="Joining year")
    year.grid(row=2,column=0,padx=10,pady=10)

    TableNameX =tk.Label(root1, text="")
    TableNameX.grid(row=2, column=1,padx=10,pady=10)

    header_selection=ttk.Combobox(root1, text= "select",value=['2010','2011','2012','2013', '2014','2015','2016','2017','2018','2019','2020','2021',"2022"])
    header_selection.grid(row=2,column=1 ,padx=10,pady=10)

    def pic():
        global picture
        picture=runner1(picture)

    Image= tk.Button(root1, text="Upload Image", font=('Arial', 12) ,height=2, width=25, command=pic)
    Image.grid(row=3,column=1,padx=10,pady=10 )
    # Image.pack(padx=20, pady=50)

    submit= tk.Button(root1, text="submit", font=('Arial', 12) ,height=2, width=25, command=get_variables)
    submit.grid(row=5,column=1,padx=10,pady=10)
    # submit.pack(padx=20, pady=50)

    root1.mainloop()
