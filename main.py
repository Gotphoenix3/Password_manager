from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

font = ("Arial", 12)
data_file_path = "password_manager.txt"


# ---------------------------- SEARCH FUNCTION ------------------------------------#
def find_password():
    """
    This function allows the user to search of r a website in the json file
    """
    # Variable to save the website the user enter to search
    lookup_website = website_entry.get()
    # Error message when the input is empty
    if lookup_website == "":
        messagebox.showerror(title="Error", message="Can not search for a Null string.")
    else:
        try:
            with open("data.json", "r") as data_file:
                try:
                    website_information = json.load(data_file)[lookup_website]
                    website_message = (f"Website information:\nEmail: {website_information["email"]}\nPassword: "
                                       f"{website_information["password"]}")
                    messagebox.showinfo(title=f"{lookup_website.title()} data.", message=website_message)
                except KeyError:
                    messagebox.showerror(title="Error: 404 Key Error", message=f"{lookup_website} has no information.")
        # Handling error in case the file json is not created or found
        except FileNotFoundError:
            # Error message: file not found
            file_not_found_answer = messagebox.askokcancel(title="Error: File not found", message=f"The "
                                                                                                  f"file you are "
                                                                                                  f"looking for is not "
                                                                                                  f"created.\nDo you "
                                                                                                  f"want to create it "
                                                                                                  f"(Ok)?")
            if file_not_found_answer:
                with open("data.json", "w") as _:
                    pass
        # Handling error in case the file has no entries
        except ValueError:
            messagebox.showerror(title=f"Error: Value Error", message="File data.json has no entries")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    """
    Allows to create a random password for the user assigned to the 'generate password' button
    """
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_entry.insert(0, "")
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)
    # Here we create the final password string and copy to the GUI
    password = "".join(password_list)
    # Update the password so each time we click 'generate password' it does not append to the generated before
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    # Making the password be copied to the clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_data_add():
    """
    This function allows us to use the ADD button to append new website, email and password to
    the data.txt file in a JSON style
    """
    # We get the user entries at the time of clicking in add
    user_website = website_entry.get()
    user_email = email_entry.get()
    user_password = password_entry.get()
    new_data = {
        user_website: {
            "email": user_email,
            "password": user_password,
        }
    }

    # We validate the user input, if there is empty spaces then pop up an error message
    if user_website == "" or user_email == "" or user_password == "":
        messagebox.showerror(title="Error", message="Please fill all the camps :c")
    else:
        # Pop up message when clicking the Add button.
        # valid_answer = messagebox.askokcancel(title=user_website, message=f"These are the details entered:"
        #                                                                   f" \nEmail: {user_email} \n"
        #                                                                   f"Password: {user_password} \n"
        #                                                                   f"Is it okay to save?")
        # if valid_answer:
        try:
            with open("data.json", "r") as data_file:
                # Json dump is used to write a new json entry in a file
                # json.dump(new_data, data_file, indent=4)

                # Json load is used to read json from a file
                # data = json.load(data_file)
                # print(data)

                # json update is used to update a json
                data = json.load(data_file)  # Reading the old data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)  # Updating the old data with the new data

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)  # Saving the updated data
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
# We create the main window where the system is going to be located
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Create the password image using canvas function and put in on the window using grid
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=logo_image)
canvas.grid(column=1, row=0)

# Creating the widgets of the window, first the Labels
website_label = Label(window, text="               Website: ", font=font)
email_label = Label(window, text=" Email/Username:", font=font)
password_label = Label(window, text="            Password: ", font=font)

# Now we create the user entry labels.
website_entry = Entry(window, font=font, width=21)
# We call the focus function to center the cursor in the entry of the website
website_entry.focus()
email_entry = Entry(window, font=font, width=40)
# Assigning a default value to the email entry
email_entry.insert(0, "mikemartinezch15@gmail.com")
password_entry = Entry(window, font=font, width=21)

# Finally, we create the buttons.
generate_button = Button(window, text="Generate password", font=font, command=generate_password)
add_button = Button(window, text="Add", font=font, width=39, command=get_data_add)

# Creating the search button
search_button = Button(window, text="Search", font=font, width=16, command=find_password)

# Assign the widgets to the screen using grid
var_pad_x = 5
var_pad_y = 5
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
website_entry.grid(column=1, row=1, padx=var_pad_x, pady=var_pad_y)
email_entry.grid(column=1, row=2, columnspan=2, padx=var_pad_x, pady=var_pad_y)
password_entry.grid(column=1, row=3, padx=var_pad_x, pady=var_pad_y)
generate_button.grid(column=2, row=3, padx=var_pad_x, pady=var_pad_y)
add_button.grid(column=1, row=4, columnspan=2, padx=var_pad_x, pady=var_pad_y)
search_button.grid(column=2, row=1)

window.mainloop()
