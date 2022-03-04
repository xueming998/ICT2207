from tkinter import *
from tkinter import filedialog, messagebox, ttk
import tkinter as tk
#import general

def drop_inside_list_box(event):
    pass

def drop_inside_textbox(event):
    pass

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

# Creating the frame for the tabs
my_frame1 = Frame(my_notebook, width=1000, height=1000, bg="light blue")

my_frame1.pack(fill="both", expand=1)

# Tabs
my_notebook.add(my_frame1, text="Ofuscation Anaylzer")

# Treeview Widget in tab1
tv1 = ttk.Treeview(my_frame1)
tv1.place(relheight=1, relwidth=1)


treescrolly = tk.Scrollbar(tv1, orient="vertical", command=tv1.yview)
treescrollx = tk.Scrollbar(tv1, orient="horizontal", command=tv1.xview)
tv1.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom", fill="x")
treescrolly.pack(side="right", fill="y")

#SECOND BOX
tv2 = ttk.Treeview(my_frame1)
tv2.place(relheight=1, relwidth=0.5)

treescrolly = tk.Scrollbar(tv2, orient="vertical", command=tv2.yview)
treescrollx = tk.Scrollbar(tv2, orient="horizontal", command=tv2.xview)
tv2.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set)
treescrollx.pack(side="bottom", fill="x")
treescrolly.pack(side="right", fill="y")


# buttons in tab1
buttonBrowse = Button(root, text="Upload File ", fg="white", bg="black")
buttonBrowse.place(relx=0.73)

buttonSearch = Button(root, text="Compare File", fg="white", bg="black")
buttonSearch.place(relx=0.83)

buttonQuit = Button(root, text="Quit", command=_quit)
buttonQuit.place(relx=0.95)
root.mainloop()