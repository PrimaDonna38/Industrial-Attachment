import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
from tkinter.tix import ComboBox
import robot

def run():
    robot.run("UserSetup.robot")

def runner():
    def get_variables():
        global var1, var2, var3, var4, var5

        var1 = user_id_input.get()

        var2 = password_input.get()

        var3 = confirm_pass_input.get()

        var4 = group_input.get()

        var5 = branch_input.get()


        print(var1, var2, var3, var4, var5)

        file=open("UserSetup.txt", "w")

        file.write(var1)
        file.write('\n')

        file.write(var2)
        file.write('\n')

        file.write(var3)
        file.write('\n')

        file.write(var4)
        file.write('\n')

        file.write(var5)

        file.close()
        run()

    set=tk.Tk()
    set.geometry("630x400")
    set.title("User Setup")

    user_id = Label(set, text = "User ID", font=("Arial", 14))
    user_id.grid(row = 0, column = 0, padx=10, pady=10)  
    
    user_id_input = Entry(set, width= 60)
    user_id_input.grid(row = 0, column = 1, padx=10, pady=10)  

    password = Label(set, text = "Password", font=("Arial", 14))
    password.grid(row = 1, column = 0, padx=10, pady=10)  
    
    password_input = Entry(set, width= 60)
    password_input.insert(0, '123456')
    password_input.grid(row = 1, column = 1, padx=10, pady=10)

    confirm_pass = Label(set, text = "Confirm Password", font=("Arial", 14))
    confirm_pass.grid(row = 2, column = 0, padx=10, pady=10)  
    
    confirm_pass_input = Entry(set, width= 60)
    confirm_pass_input.insert(0, '123456')
    confirm_pass_input.grid(row = 2, column = 1, padx=10, pady=10)

    group = Label(set, text = "User Group", font=("Arial", 14))
    group.grid(row = 3, column = 0, padx=10, pady=10)  
    
    group_input = ttk.Combobox(set, width= 60, value=['Select','001 : Administrator',
    '002 : Audit','003 : Branch user','004 : Accountant','005 : CATC group','007 : Aero Billing',
    '008 : Cargo Scanning User Group','009 : Lease Setup (Commercial)','010 : Super Administrator',
    '011 : Meter Reader','012 : Meter Reviewer','013 : Meter Approver','014 : Utility Biller',
    '015 : Training & Go/Personal Info./HR Leave','016 : GPF User','017 : Utility Residential',
    '018 : Others Branch User HQ Access Permission','019 : U-R Meter Reader',
    '020 : U-R Meter Reviewer','021 : U-R Meter Approver','022 : Payroll- HSIA',
    '023 : HR Admin + Training & GO','024 : ACR','025 : Lease Setup (Residential',
    '026 : HR/Payroll Report','027 : Water Bill Group','028 : Employee Personal Information Group',
    '029 : Member Group','030 : Landing & Takeoff/Overflying','101 : Barishal Airport',
    '102 : CEMSU Group','103 : Embarkation User Group','104 : Store & Inventory User',
    '105 : HSIA:Admin','111 : AERO BILLING ADMIN','119 : Admin/Payroll',
    '222 : Admin.HR(Personal Info)','800 : Terminal Building','521 : Director Finance',
    '801 : Cargo','802 : RADAR','803 : NavAids','950 : Landing & Take Off',
    '980 : Cargo Scanning Admin Group','981 : Utility Billing','983 : Lease Revenue',
    '984 : HSIA Billing Collection','985 : Pension module user','986 : LAW SECTION',
    '987 : EM ADMIN','989 : ATS ADMIN','990 : ATS','991 : Director Reader',
    '992 : COM/APP/Store User','993 : COM User','994 : Accounting & Payroll',
    '995 : Embarkation & Landing & Take Off','999 : TEST'])

    group_input.current(0)
    group_input.grid(row=3, column=1, padx=10, pady=10)
    
    branch = Label(set, text = "Default Branch", font=("Arial", 14))
    branch.grid(row = 4, column = 0, padx=10, pady=10)  
    
    branch_input = ttk.Combobox(set, width= 60, value=['Select','0000 - CONSOLIDATED CAAB',
    '0001 - HEAD QUARTERS','0002 - Central Engineering Maintenance and Stores Unit',
    '0003 - EM CIRCLE','0004 - CIVIL CIRCLE','0005 - P & DQS CIRCLE','0006 - Civil Aviation Academy',
    '0007 - Hazrat Shahjalal International Airport','0008 - Shah Amanat International Airport',
    '0009 - Osmani International Airport','0010 - Shah Makhdum Airport','0011 - Barishal Airport',
    '0012 - Ishwardi Airport',"0013 - Cox's Bazar Airport",'0014 - Jashore Airport',
    '0015 - Saidpur Airport','0016 - Shamshernagar Airport (STOL)','0017 - THAKURGAON',
    '0018 - MONGLA & BOGRA','0019 - LALMONIRHAT','0020 - COMILLA','0021 - KHANJAHAN ALI',
    '0022 - Bangabandhu Airport'])
    
    branch_input.current(0)
    branch_input.grid(row=4, column=1, padx=10, pady=10)

    submit = Button(set, text = "Submit", command= get_variables, font=("Arial", 14)).grid(row = 5, column = 1, padx=10, pady=10)

    set.mainloop() 