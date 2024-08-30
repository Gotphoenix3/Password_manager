from tkinter import *

font = ("Arial", 12)
data_file_path = "password_manager.txt"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def get_data_add():
    """
    This function allows us to use the ADD button to append new website, email and password to
    the data.txt file in a JSON style
    :return:
    """
    # We get the user entries at the time of clicking in add
    user_website = website_entry.get()
    user_email = email_entry.get()
    user_password = password_entry.get()
    # Count the existing entries in the file
    try:
        with open(data_file_path, "r") as file:
            lines = file.readlines()
            # Extract numbers from lines to find the highest number
            numbers = [int(line.split('Data_')[1].split(' ')[0]) for line in lines if 'Data_' in line]
            next_number = max(numbers, default=0) + 1
    except FileNotFoundError:
        next_number = 1
    # Appending the data from the window to the password_manager file
    with open(data_file_path, "a") as file:
        file.write(f"Data-{next_number} = {{\n")
        file.write(f"   Website: {user_website},\n")
        file.write(f"   Email/User: {user_email},\n")
        file.write(f"   Password: {user_password},\n")
        file.write("}\n")


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
website_entry = Entry(window, font=font, width=40)
# We call the focus function to center the cursor in the entry of the website
website_entry.focus()
email_entry = Entry(window, font=font, width=40)
# Assigning a default value to the email entry
email_entry.insert(0, "mikemartinezch15@gmail.com")
password_entry = Entry(window, font=font, width=21)

# Finally, we create the buttons.
generate_button = Button(window, text="Generate password", font=font)
add_button = Button(window, text="Add", font=font, width=39, command=get_data_add)

# Assign the widgets to the screen using grid
var_pad_x = 5
var_pad_y = 5
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
website_entry.grid(column=1, row=1, columnspan=2, padx=var_pad_x, pady=var_pad_y)
email_entry.grid(column=1, row=2, columnspan=2, padx=var_pad_x, pady=var_pad_y)
password_entry.grid(column=1, row=3, padx=var_pad_x, pady=var_pad_y)
generate_button.grid(column=2, row=3, padx=var_pad_x, pady=var_pad_y)
add_button.grid(column=1, row=4, columnspan=2, padx=var_pad_x, pady=var_pad_y)


window.mainloop()
