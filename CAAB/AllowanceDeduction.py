import tkinter as tk
from tkinter import *
from tkinter import ttk
import robot

def run3():
    robot.run("AllowanceDeduction.robot")

def runner3():
    def get_variables():

        global variable1, variable2, variable3, variable4, variable5, variable6, variable7, variable8, variable9, variable10, variable11, variable12, variable13, variable14, variable15
        
        variable1 = header_selection.get()

        variable2 = header_selection1.get()
        
        variable3 = employee_1.get()
        
        variable4 = insurance_1.get()
        
        variable5 = fund_1.get()
        
        variable6 = gpf_1.get()
        
        variable7 = gpf_a_1.get()
        
        variable8 = tax_1.get()
        
        variable9 = rent_1.get()
        
        variable10 = maintenance_1.get()
        
        variable11 = bill_1.get()
        
        variable12 = water_1.get()
        
        variable13 = gas_1.get()
        
        variable14 = mt_1.get()
        
        variable15 = stamp_1.get()
        
        print(variable1,variable2,variable3,variable4,variable5,variable6,variable7,variable8,variable9,variable10,variable11,variable12,variable13,variable14,variable15)
        
        with open('AllowanceDeduction.txt','w') as file:

            file.write(variable1)
            file.write("\n")

            file.write(variable2)
            file.write("\n")

            file.write(variable3)
            file.write("\n")

            file.write(variable4)
            file.write("\n")

            file.write(variable5)
            file.write("\n")

            file.write(variable6)
            file.write("\n")

            file.write(variable7)
            file.write("\n")

            file.write(variable8)
            file.write("\n")

            file.write(variable9)
            file.write("\n")

            file.write(variable10)
            file.write("\n")

            file.write(variable11)
            file.write("\n")

            file.write(variable12)
            file.write("\n")

            file.write(variable13)
            file.write("\n")

            file.write(variable14)
            file.write("\n")

            file.write(variable15)
            
            run3()
            
    root3=tk.Tk()
    root3.geometry("600x670")
    root3.title("Allowance & Deduction")

    month = Label(root3,text="For the month of: ",font=('Arial',12)).grid(row = 0, column = 0, padx=10,pady=10)
    header_selection=ttk.Combobox(root3,value=['---Please Select---','Jan','Feb','Mar','Apr','May', 'Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
    header_selection.grid(row=0,column=1 )

    header_selection1=ttk.Combobox(root3, value=['---Please Select---','2023','2022'])
    header_selection1.grid(row=0,column=2,padx=10 )

    employee = Label(root3,text="Employee ID: " ,font=('Arial',12)).grid(row = 1, column = 0, padx=10,pady=10)
    employee_1 = Entry(root3,width=25)
    employee_1.insert(0,'0')
    employee_1.grid(row = 1, column = 1, padx=10, pady=10)

    insurance = Label(root3,text="Group Insurance: " ,font=('Arial',12)).grid(row = 2, column = 0, padx=10,pady=10)
    insurance_1 = Entry(root3,width=25)
    insurance_1.insert(0,'0')
    insurance_1.grid(row = 2, column = 1, padx=10, pady=10)

    fund = Label(root3,text="Benevolent Fund: " ,font=('Arial',12)).grid(row = 3, column = 0,  padx=10,pady=10)
    fund_1 = Entry(root3, width=25)
    fund_1.insert(0,'0')
    fund_1.grid(row = 3, column = 1, padx=10,pady=10)

    gpf = Label(root3,text="GPF (%): ",font=('Arial',12)).grid(row = 4, column = 0, padx=10,pady=10)
    gpf_1 = Entry(root3,width=25)
    gpf_1.insert(0,'0')
    gpf_1.grid(row = 4, column = 1, padx=10,pady=10)

    gpf_a = Label(root3,text="GPF Account No.: ",font=('Arial',12)).grid(row = 5, column = 0,  padx=10,pady=10)
    gpf_a_1 = Entry(root3,width=25)
    gpf_a_1.insert(0,'0')
    gpf_a_1.grid(row = 5, column = 1, padx=10,pady=10)

    tax = Label(root3,text="Income Tax: ",font=('Arial',12)).grid(row = 6, column = 0,  padx=10,pady=10)
    tax_1 = Entry(root3,width=25)
    tax_1.insert(0,'0')
    tax_1.grid(row = 6, column = 1, padx=10,pady=10)

    rent = Label(root3,text="House Rent: ",font=('Arial',12)).grid(row = 7, column = 0, padx=10,pady=10)
    rent_1 = Entry(root3,width=25)
    rent_1.insert(0,'0')
    rent_1.grid(row = 7, column = 1,  padx=10,pady=10)

    maintenance = Label(root3,text="House Rent (Maintenance): ",font=('Arial',12)).grid(row = 8, column = 0, padx=10,pady=10)
    maintenance_1 = Entry(root3,width=25)
    maintenance_1.insert(0,'0')
    maintenance_1.grid(row = 8, column = 1,  padx=10,pady=10)

    bill = Label(root3,text="Electricity bill: ",font=('Arial',12)).grid(row = 9, column = 0,  padx=10,pady=10)
    bill_1 = Entry(root3,width=25)
    bill_1.insert(0,'0')
    bill_1.grid(row = 9, column = 1, padx=10,pady=10)

    water = Label(root3,text="Water & Sewage: ",font=('Arial',12)).grid(row = 10, column = 0,  padx=10,pady=10)
    water_1 = Entry(root3,width=25)
    water_1.insert(0,'0')
    water_1.grid(row = 10, column = 1,  padx=10,pady=10)

    gas = Label(root3,text="Gas: ",font=('Arial',12)).grid(row = 11, column = 0, padx=10,pady=10)
    gas_1 = Entry(root3,width=25)
    gas_1.insert(0,'0')
    gas_1.grid(row = 11, column = 1, padx=10,pady=10)

    mt = Label(root3,text="MT Charge: ",font=('Arial',12)).grid(row = 12, column = 0,  padx=10,pady=10)
    mt_1 = Entry(root3,width=25)
    mt_1.insert(0,'0')
    mt_1.grid(row = 12, column = 1, padx=10,pady=10)

    stamp = Label(root3,text="Stamp Fee: ",font=('Arial',12)).grid(row = 13, column = 0, padx=10,pady=10)
    stamp_1 = Entry(root3,width=25)
    stamp_1.insert(0,'0')
    stamp_1.grid(row = 13, column = 1, padx=10,pady=10)

    button4 = Button(root3, height= 1, width=8,text='Submit', font=('Arial',12), command=get_variables)
    button4.grid(row=14, column=1, padx=10,pady=10)

    root3.mainloop()
