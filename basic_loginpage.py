from tkinter import *

count = 3
def submit():
    global count
    if username.get() == "Dhruv123" and password.get() == "Keychain":
        print("Username and password accepted")
    else:
        count -= 1
        print("Username or password is wrong")
        print("You have " + str(count) + " tries remaining")
        if (count == 0):
            username.config(state=DISABLED)
            password.config(state=DISABLED)
            submit_button.config(state=DISABLED)
            delete_button.config(state=DISABLED)
def delete_button():
    username.delete(0, END)
    password.delete(0, END)

window = Tk()

window.geometry("400x400")

window.title("Login page")

label = Label(window, text="Login page",
              font=("Arial", 25, 'bold'),
              bg="black",
              fg="white")
label.pack()

header = Label(window, text="Enter user and password",
              font=("Arial", 25, 'bold'),
              bg="black",
              fg="white")
header.place(x=30, y=200)

username = Entry(window,
                 font=("Arial", 25, 'bold'),
                 relief=RAISED)
username.place(x=30, y=270)

password = Entry(window,
                 font=("Arial", 25, 'bold'),
                 relief=RAISED,
                 show="*")
password.place(x=30, y=350)

submit_button = Button(window,
                 text="Submit",
                 font=("Arial", 15, 'bold'),
                 relief=RAISED,
                 command=submit)
submit_button.place(x=30, y=450)

delete_button = Button(window,
                 text="Delete",
                 font=("Arial", 15, 'bold'),
                 relief=RAISED,
                 command=delete_button)
delete_button.place(x=150, y=450)

window.mainloop()