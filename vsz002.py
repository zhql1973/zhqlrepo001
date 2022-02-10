import tkinter as tk
import os
import shutil
from tkinter import StringVar
from tkinter import messagebox
from tkinter.filedialog import (
    askopenfilename, askopenfilenames, askdirectory, asksaveasfilename)


def getdir():
    mdir = askdirectory()
    mmdir.set(mdir)
    print(mdir)


def getfile():
    mfile = askopenfilename()
    mmfile.set(mfile)


def copyfile():
    if mmfile.get() == "":
        messagebox.showinfo(title='error', message='soure file is empty!')
        return
    if mmdir.get() == "":
        messagebox.showinfo(title='error', message='dest dir is empty!')
        return
    oldname = mmfile.get()
    print(oldname)
    netfilename = oldname.split("/")
    print(netfilename[-1])
    newname = os.path.join(mmdir.get(), netfilename[-1])
    print(newname)
    shutil.copyfile(oldname, newname)
    print(oldname, " have copied to ", newname)


root = tk.Tk()
root.title("copy file")
mdir = ""
mfile = ""
mmdir = StringVar()
mmfile = StringVar()
labela = tk.Label(root, text="please choose the file:").grid(row=0, column=1)
entrya = tk.Entry(root, width=100, textvariable=mmfile).grid(row=0, column=2)
labelb = tk.Label(root, text="please entry dir:").grid(row=1, column=1)
entryb = tk.Entry(root, width=100, textvariable=mmdir).grid(row=1, column=2)

tk.Button(root, text="get file",
          command=lambda: getfile()).grid(row=2, column=1)
tk.Button(root, text="get dir",
          command=lambda: getdir()).grid(row=2, column=2)

tk.Button(root, text="copy file",
          command=lambda: copyfile()).grid(row=2, column=3)

print("source file;", mfile, "dest dir:", mdir)

root.mainloop()
