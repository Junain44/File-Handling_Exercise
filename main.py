from tkinter import *


root = Tk()
root.title("My weekend activities")
root.geometry("500x450")


my_text = Text(root, width=40, height=10, font=10)
my_text.pack()
my_text.place(x = 90, y = 50)


create_button = Button(root, text="Create textFile", command="open_txt")
create_button.pack()
create_button.place(x = 50, y = 250)


display_button = Button(root, text="Display", command="display_txt")
display_button.pack()
display_button.place(x = 180, y = 250)

def append_data():

append_button = Button(root, text="Append Data", command=open)
append_button.pack()
append_button.place(x = 263, y = 250)

def clear_all_txt():
    my_text.delete('1.0', 'end')
clear_button = Button(root, text="Clear", command=clear_all_txt)
clear_button.pack()
clear_button.place(x = 380, y = 250)

def exit_program():
    root.destroy()
exit_button = Button(root, text="Exit", command=exit)
exit_button.place(x = 445, y = 250)














root.mainloop()

