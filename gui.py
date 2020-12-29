from tkinter import *
# from keys import runKeys

root = Tk()

e = Entry(root, width=50)
e.grid(row=3, column=0)


def onClick():
    print("Clicked.")
    print(e.get())
    # runKeys()


myLabel1 = Label(root, text="Click me!")
btn1 = Button(root, text="test", padx=10, pady=5, command=onClick)

myLabel1.grid(row=0, column=0)
btn1.grid(row=1, column=0)

root.mainloop()
