from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
# We create the main window where the system is going to be located
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Create the password image using canvas function and put in on the window
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=logo_image)
canvas.grid()


window.mainloop()
