from tkinter import *


root = Tk()
root.title("My weekend activities")
root.geometry("500x450")


def create():
    text_info = my_text.get("1.0", END)
    print(text_info)

    txtfile = open("my_weekend_activities_txt", "w")
    txtfile.write(text_info)
    txtfile.close()

def display():
    reader = open("my_weekend_activities_txt", "r")
    activities=reader.read()
    my_text.insert(END,activities)
    reader.close()

def append():
    reader = open("my_weekend_activities_txt", "w")
    reader.write(my_text.get(1.0,END))

def clear():
    reader = open('my_weekend_activities_txt', 'r+')
    reader.truncate(0)
    my_text.delete(1.0,END)

def exit_program():
    root.destroy()



my_text = Text(root, width=40, height=10, font=10 )
my_text.pack()
my_text.place(x = 90, y = 50)

create_button = Button(root, text="Create textFile", command=create)
create_button.pack()
create_button.place(x = 50, y = 250)


display_button = Button(root, text="Display", command=display)
display_button.pack()
display_button.place(x = 180, y = 250)



append_button = Button(root, text="Append Data", command=append)
append_button.pack()
append_button.place(x = 263, y = 250)


clear_button = Button(root, text="Clear", command=clear)
clear_button.pack()
clear_button.place(x = 380, y = 250)

exit_button = Button(root, text="Exit", command=exit)
exit_button.place(x = 445, y = 250)














root.mainloop()

