#/usr/bin/env python3

import requests
from tkinter import Tk
from tkinter import ttk




def populate(label):
    r = requests.get('http://localhost:8001')
    content = r.json()
    label["text"] = content["message"]


def main():
    root = Tk()
    root.title("Sample Application")
    root.geometry("500x400")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    lbl = ttk.Label(frm, text="")
    lbl.grid(column=0, row=0)
    ttk.Button(frm, text="Make API Call", command=lambda: populate(lbl)).grid(column=0, row=1)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=1)
    root.mainloop()

if __name__ == '__main__':
    main()
