import PySimpleGUI as sg
import csv

sg.theme("DarkPurple6")
sg.set_options(font="Arial 16")

layout = [  [sg.Text("Enter First Name"), sg.Push(),sg.InputText(key="-fname-")],
            [sg.Text("Enter Last Name"), sg.Push(),sg.InputText(key="-lname-")],
            [sg.Text("Enter Your Number"), sg.Push(),sg.InputText(key="-phone-")],
            [sg.Text("Enter Email"), sg.Push(),sg.InputText(key="-email-")],
            [sg.Text("Enter Address"), sg.Push(),sg.InputText(key="-address-")],
            [sg.Button("Save"),sg.Button("Cancel")],
            [sg.Text("Search By Last Name"), sg.Push(),sg.InputText(key="-searchText-")],
            [sg.Button("Search")],
            [sg.Text(key="-searchOutput-")],
        ]

#create window
window = sg.Window("Contact",layout,icon="favicon.ico")

while True:
    event ,values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancel": #if user closes window or clicks cancel
        break
    fname = values["-fname-"]
    lname = values["-lname-"]
    phone = values["-phone-"]
    email = values["-email-"]
    address = values["-address-"]
    info = [fname, lname, phone, email, address]
    if event == "Save":
        with open("info.csv",'a',newLine='') as w:
            cw = csv.writer(w)
            cw.writerow(info)
        window["-fname-"].update('')
        window["-lname-"].update('')
        window["-phone-"].update('')
        window["-email-"].update('')
        window["-address-"].update('')

    searchText = values['-searchText-']
    if event == "Search":
        with open("info.csv",'r') as r:
            cr = csv.reader(r)
            for i in cr:
                if i[1] == searchText:
                    window["-searchOutput-"].update("First Name: {i[0]}\n Last Name: {i[1]}\nPhone Number: {i[2]}\nEmail: {[3]}\nAddress: {[4]}")

window.close()


