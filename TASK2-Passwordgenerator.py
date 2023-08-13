import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length <= 0:
        password_label.config(text="Invalid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    generated_password.set(password)

def accept_password():
    user = user_entry.get()
    if user:
        accepted_passwords.append((user, generated_password.get()))
        generated_password.set("Password accepted!")

def reject_password():
    generated_password.set("")
    password_label.config(text="Password rejected")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x300")

# Create and place widgets
user_label = tk.Label(root, text="Enter User Name:")
user_label.grid(row=0, column=0, padx=10, pady=10)

user_entry = tk.Entry(root)
user_entry.grid(row=0, column=1, padx=10, pady=10)

length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=1, column=0, padx=10, pady=10)

length_entry = tk.Entry(root)
length_entry.grid(row=1, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=2, columnspan=2, padx=10, pady=10)

generated_password = tk.StringVar()
password_label = tk.Label(root, textvariable=generated_password, wraplength=400)
password_label.grid(row=3, columnspan=2, padx=10, pady=10)

accept_button = tk.Button(root, text="Accept Password", command=accept_password)
accept_button.grid(row=4, column=0, padx=10, pady=10)

reject_button = tk.Button(root, text="Reject Password", command=reject_password)
reject_button.grid(row=4, column=1, padx=10, pady=10)

accepted_passwords = []

root.mainloop()
