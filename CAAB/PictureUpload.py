import os
import PySimpleGUI as sg
import tkinter.messagebox as msgbox

def runner1(x):
    csv_address=x
    #!cur=mydb.cursor()
    working_directory = os.getcwd()
    layout = [  
                [sg.Text("Choose a file:")],
                [sg.InputText(key="-FILE_PATH-"), 
                sg.FileBrowse(initial_folder=working_directory, file_types=[("All file", "*.png")])],
                [sg.Button('Submit')]
            ]

    window = sg.Window("Upload Image", layout)
    def display_msg():
        msgbox.showinfo(title='', message='Upload Successfully')
        window.close_destroys_window
    while True:
        event, values = window.read()
        if event == "Submit":
            csv_address = values["-FILE_PATH-"]
            sg.WIN_CLOSE_ATTEMPTED_EVENT
            display_msg()
            break
        else:
            break
    return csv_address

