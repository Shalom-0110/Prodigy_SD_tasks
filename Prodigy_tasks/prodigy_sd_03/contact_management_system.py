import tkinter as tk
from tkinter import messagebox, ttk
import json
import os

# Path to the JSON file to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Initialize the contacts dictionary
contacts = load_contacts()

# Function to add a new contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone and email:
        contacts[name] = {'phone': phone, 'email': email}
        save_contacts(contacts)
        update_contacts_list()
        clear_entries()
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

# Function to update the contact list display
def update_contacts_list():
    contacts_list.delete(0, tk.END)
    for name in contacts:
        contacts_list.insert(tk.END, name)

# Function to clear input entries
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Function to delete a selected contact
def delete_contact():
    selected_contact = contacts_list.get(tk.ACTIVE)
    if selected_contact in contacts:
        del contacts[selected_contact]
        save_contacts(contacts)
        update_contacts_list()

# Function to edit a selected contact
def edit_contact():
    selected_contact = contacts_list.get(tk.ACTIVE)
    if selected_contact in contacts:
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

        name_entry.insert(0, selected_contact)
        phone_entry.insert(0, contacts[selected_contact]['phone'])
        email_entry.insert(0, contacts[selected_contact]['email'])

        add_button.config(text="Update Contact", command=update_contact)

# Function to update contact information
def update_contact():
    selected_contact = contacts_list.get(tk.ACTIVE)
    new_name = name_entry.get()
    new_phone = phone_entry.get()
    new_email = email_entry.get()

    if selected_contact in contacts:
        if new_name and new_phone and new_email:
            del contacts[selected_contact]
            contacts[new_name] = {'phone': new_phone, 'email': new_email}
            save_contacts(contacts)
            update_contacts_list()
            clear_entries()
            add_button.config(text="Add Contact", command=add_contact)
        else:
            messagebox.showwarning("Input Error", "All fields are required!")

# Setup the main window
root = tk.Tk()
root.title("Contact Management System")
root.geometry("400x500")

# Define pastel colors for aesthetic GUI
bg_color = "#FFF0F5"  # Lavender blush
button_color = "#FFB6C1"  # Light pink
entry_bg_color = "#FFC0CB"  # Pink
listbox_color = "#FFE4E1"  # Misty rose

root.config(bg=bg_color)

# Create a style for rounded buttons and entry fields
style = ttk.Style()
style.theme_use('clam')
style.configure('TButton', background=button_color, foreground='black', borderwidth=0, focuscolor='none', font=('Arial', 10))
style.configure('TEntry', fieldbackground=entry_bg_color, borderwidth=0, font=('Arial', 10))
style.map('TButton', background=[('active', button_color)])

# Create a main frame
main_frame = tk.Frame(root, bg=bg_color, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# Create and place widgets
input_frame = tk.Frame(main_frame, bg=bg_color)
input_frame.pack(fill=tk.X, pady=(0, 10))

tk.Label(input_frame, text="Name:", bg=bg_color, font=('Arial', 10)).pack(side=tk.LEFT, padx=(0, 5))
name_entry = ttk.Entry(input_frame, width=30)
name_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

input_frame2 = tk.Frame(main_frame, bg=bg_color)
input_frame2.pack(fill=tk.X, pady=(0, 10))

tk.Label(input_frame2, text="Phone:", bg=bg_color, font=('Arial', 10)).pack(side=tk.LEFT, padx=(0, 5))
phone_entry = ttk.Entry(input_frame2, width=30)
phone_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

input_frame3 = tk.Frame(main_frame, bg=bg_color)
input_frame3.pack(fill=tk.X, pady=(0, 10))

tk.Label(input_frame3, text="Email:", bg=bg_color, font=('Arial', 10)).pack(side=tk.LEFT, padx=(0, 5))
email_entry = ttk.Entry(input_frame3, width=30)
email_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)

add_button = ttk.Button(main_frame, text="Add Contact", command=add_contact, width=38)
add_button.pack(pady=(0, 10))

contacts_list = tk.Listbox(main_frame, bg=listbox_color, font=('Arial', 10), relief=tk.FLAT, borderwidth=0, highlightthickness=0)
contacts_list.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

button_frame = tk.Frame(main_frame, bg=bg_color)
button_frame.pack(fill=tk.X)

edit_button = ttk.Button(button_frame, text="Edit Contact", command=edit_contact, width=18)
edit_button.pack(side=tk.LEFT, padx=(0, 5))

delete_button = ttk.Button(button_frame, text="Delete Contact", command=delete_contact, width=18)
delete_button.pack(side=tk.RIGHT)

update_contacts_list()

# Run the application
root.mainloop()