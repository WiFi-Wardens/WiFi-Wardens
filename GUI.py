from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk


def macFilter():
    macWindow = Toplevel(window)
    macWindow.title("MAC Filtering")
    macWindow.geometry('800x800')


def surveillance():
    survWindow = Toplevel(window)
    survWindow.title("Passive Surveillance")
    survWindow.geometry('800x800')

    s = ttk.Style()
    s.theme_use('clam')

    tree = ttk.Treeview(survWindow, column=("c1", "c2", "c3", "c4"), show='headings', height=5)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="IP")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="MAC Address")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="Device")
    tree.column("# 4", anchor=CENTER)
    tree.heading("# 4", text="Ports")

    tree.pack()

def users():
    userWindow = Toplevel(window)
    userWindow.title("Users")
    userWindow.geometry('400x400')

    btn1 = Button(userWindow, text="Authenticate",command=Add)
    #btn1.grid(column=0,row=0,sticky=NW)
    btn1.pack()

    btn2 = Button(userWindow, text="Deauthenticate",command=Remove)
    #btn2.grid(column=1,row=0,sticky=NW)
    btn2.pack()

    t = ttk.Style()
    t.theme_use('clam')

    tree = ttk.Treeview(userWindow, column=("c1","c2"), show='headings', height=5)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="IP")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="MAC Address")

    tree.pack()




def Add():

    addWindow = Toplevel(window)
    addWindow.title("Add User")
    addWindow.geometry('200x100')

    entry1 = Entry(addWindow, textvariable=name_var, font =('calibre',10,'bold'))
    entry1.pack(side=LEFT,expand=TRUE)


    bt6=Button(addWindow,text='Submit',command=submit)
    bt6.pack(side=RIGHT,expand=TRUE)


def Remove():
    addWindow = Toplevel(window)
    addWindow.title("Remove User")
    addWindow.geometry('200x100')

    entry1 = Entry(addWindow, textvariable=name_var, font =('calibre',10,'bold'))
    entry1.pack(side=LEFT,expand=TRUE)


    bt4=Button(addWindow,text='Submit',command=submit)
    bt4.pack(side=RIGHT,expand=TRUE)

def submit():
    name=name_var.get()

    name_var.set("")



    
window = Tk()


window.title("WiFi Wardens")
window.geometry('800x800')
window.configure(bg="white")
name_var= StringVar()


frame=Frame(window,width=50, height=50)
frame.grid(row=0,column=0)
frame.configure(bg="white")
image = Image.open("WW_rounded.png")
resize_image = image.resize((700,500))
img = ImageTk.PhotoImage(resize_image)

label1 = Label(image=img,borderwidth=0,highlightthickness=0)
label1.image = img
label1.place(relx=0.5,rely=0.5,anchor=CENTER)





btn1 = Button(window, text="MAC Filtering", command=macFilter)
btn1.grid(column=0,row=0,sticky=NW)

btn2 = Button(window, text="Passive Surveillance", command=surveillance)
btn2.grid(column=1,row=0,sticky=NW)

btn3 = Button(window, text="Users", command=users)
btn3.grid(column=2,row=0,sticky=NW)



window.mainloop()
