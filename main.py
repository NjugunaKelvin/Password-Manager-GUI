from tkinter import *
from tkinter import messagebox
import random

# Password Generator





# Save Password
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)== 0 or len(password) == 0:
        is_ok = False
        messagebox.showinfo(title="Ooops", message="Seems like you left some field blank")
    else:
        # message box
        is_ok = messagebox.askokcancel(title="Website", message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \n Is it okay to save")

        
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")

                # clear
                website_entry.delete(0, END)
                password_entry.delete(0, END)















# UI SETUP

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="img.png")

canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "johndoe@gmail.com")

password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)


# Buttons
generate_pass_btn =Button(text="Generate Password")
generate_pass_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)



window.mainloop()