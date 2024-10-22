from tkinter import Tk, Label, Entry, Button, END, Canvas, PhotoImage
from tkinter import messagebox
import  random
import pyperclip
FONT = ('Arial', 14 )

# =================GENERATE PASSWORD==============#
# TODO: 3 GENERATE PASSWORD
def generate_password():

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
             'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


  password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]

  symbol = [random.choice(symbols) for _ in range(random.randint(2, 4))]

  number = [random.choice(numbers) for _ in range(random.randint(2, 4))]

  password_list = password_letters + symbol + number

  random.shuffle(password_list)
  my_pass = "".join(password_list)
  mypass.delete(0, END)
  mypass.insert(0, my_pass)
  pyperclip.copy(my_pass)


# =================SAVE ENTRIES===================#
# TODO: 2 SAVE ENTRIES
def save():
    website_name = website.get()
    email_name= email.get()
    mypass_name = mypass.get()

    if len(website_name) == 0 or len(email_name) == 0 or len(mypass_name) ==0:
        messagebox.showinfo(title="Input Required", message="Please Make Sure You Haven't Left Any Field Empty")
    else:

        is_correct = messagebox.askokcancel(title=website_name, message=f"There are the details entered: \nWebsite: {website_name} "
                                                           f"\nEmail: {email_name} "
                                                           f"\nPassword: {mypass_name}")

        if is_correct:
            with open("data.txt", "a") as data:
                data.write(f"{website_name} | {email_name}  |{mypass_name} \n")
                website.delete(0, END)
                mypass.delete(0, END)
# =================UI SET-UP======================#
# TODO: 1 UI SET-UP
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(row=0, column=1)

# website_label = Label(text="Website")
website_label = Label(text='Website: ', font=FONT)
website_label.grid(row=1, column=0)
website = Entry(width=35)
website.focus()
website.grid(row=1, column=1,columnspan=2)

# EMAIL AND USERNAME
email_label = Label(text='Email/Username: ', font=FONT)
email_label.grid(row=2, column=0)
email = Entry(width=35)
email.grid(row=2, column=1,columnspan=2)
email.insert(0, "jadevictor247@gmail.com")

# PASSWORD
mypass_label = Label(text='Password: ', font=FONT)
mypass_label.grid(row=3,column=0)
mypass = Entry(width=21)
mypass.grid(row=3, column=1)


# GENERATE PASSword
generate_mypass_button = Button(text='Generate Password', command=generate_password)
generate_mypass_button.grid(row=3, column=2)

# ADD
add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1,columnspan=2)


window.mainloop()