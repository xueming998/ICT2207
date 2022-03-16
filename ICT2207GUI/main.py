from tkinter import *
from tkinter import filedialog, messagebox, ttk
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import scrolledtext
#import general


def _quit():
    root.quit()  # stops mainloop
    root.destroy()

# Creating GUI
root = Tk()
root.title("Ofuscation Anaylzer")
root.geometry("700x700")
# Using notebook as mainframe
my_notebook = ttk.Notebook(root)
my_notebook.pack(pady=7)

def mutliple_yview(*args):
    txt1.yview(*args)
    txt2.yview(*args)

def mutliple_xview(*args):
    txt1.xview(*args)
    txt2.xview(*args)

my_frame1 = Frame(my_notebook)
hor_scroll = Scrollbar(my_frame1, orient='horizontal')
hor_scroll.pack(side=BOTTOM, fill=X)
text_scroll = Scrollbar(my_frame1)
text_scroll.pack(side=RIGHT, fill=Y)

my_frame1.pack(fill="both", expand=1)

# Tabs
my_notebook.add(my_frame1, text="File")

txt1 = Text(my_frame1, width=100, height=15, yscrollcommand=text_scroll.set
            , wrap="none", xscrollcommand=hor_scroll.set)
txt1.pack(pady=0)
#SECOND textbox
txt2= Text(my_frame1, width=100, height=15, yscrollcommand=text_scroll.set
            ,wrap="none", xscrollcommand=hor_scroll.set)
txt2.pack(pady=10)

text_scroll.config(command=mutliple_yview)
hor_scroll.config(command=mutliple_xview)
def openFile():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/",
        title="Open Text file",
        filetypes=(("Text Files", "*.txt"),("SMALI Files", "*.smali"),)
    )
    path.insert(END, tf)
    tf = open(tf, 'r')
    data = tf.read()
    txt1.insert(END, data)
    txt2.insert(END, data)
    tf.close()


path = Entry(root)
path.pack( expand=True, fill=X, padx=0.3)

#ws.mainloop()


# buttons in tab1
buttonBrowse = Button(root, text="Upload File ", fg="white", bg="black" ,command=openFile)
buttonBrowse.place(relx=0.73)

buttonSearch = Button(root, text="Compare File", fg="white", bg="black")
buttonSearch.place(relx=0.83)

buttonQuit = Button(root, text="Quit", command=_quit)
buttonQuit.place(relx=0.95)
root.mainloop()


