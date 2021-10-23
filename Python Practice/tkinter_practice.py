from tkinter import *
# to load all the objects from tkinter

window = Tk()
# widgets go in between

def kg_convert():
    grams = float(e1_value.get()) * 1000
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274
    
    t1.delete("1.0", END)  # Deletes the content of the Text box from start to END
    t1.insert(END, grams)  # Fill in the text box with the value of gram variable
    t2.delete("1.0", END)
    t2.insert(END, pounds)
    t3.delete("1.0", END)
    t3.insert(END, ounces)
    
e1=Label(window,text="Enter value in Kg")
e1.grid(row=0 , column=0) # The Label is placed in position 0, 0 in the window
 
b1 = Button(window, text = "Submit", command = kg_convert)

# two methods to add to window.
# b1.pack()
b1.grid(row = 0, column = 2)

e1_value = StringVar()
e1 = Entry(window, textvariable = e1_value)
e1.grid(row = 0, column = 1)

t1 = Text(window, height = 1, width = 10)
t1.grid(row = 1, column = 0)

t2 = Text(window, height = 1, width = 10)
t2.grid(row = 1, column = 1)

t3 = Text(window, height = 1, width = 10)
t3.grid(row = 1, column = 2)

# This makes sure to keep the main window open
window.mainloop()
