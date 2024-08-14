from tkinter import*
from tkinter import messagebox

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    
    if name and phone and email and address:
        contact_list.insert(END, f"{name} - {phone} - {email} - {address}")
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0,END)
        address_entry.delete(0,END)
    else:
        messagebox.showerror("Error", "Please enter all the details")

def delete_contact():
    try:
        selected_index = contact_list.curselection()[0]
        contact_list.delete(selected_index)
    except IndexError:
        messagebox.showerror("Error", "No contact selected.")

def clear_contacts():
    contact_list.delete(0, END)

def get_selected_contact(event):
    try:
        selected_index = contact_list.curselection()[0]
        selected_contact = contact_list.get(selected_index)
        name, phone = selected_contact.split(" - ")
        name_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0,END)
        address_entry.delete(0,END)
        name_entry.insert(END, name)
        phone_entry.insert(END, phone)
        email_entry.insert(END, email)
        address_entry.insert(END, address)
    except IndexError:
        pass

root = Tk()
root.title("Contact Book") 


# Create UI elements
name_label = Label(root, text="Name:", font="arial 12")
name_label.pack()
name_entry = Entry(root,width=50)
name_entry.pack(pady=10,padx=20)

phone_label = Label(root, text="Phone:",font="arial 12")
phone_label.pack()
phone_entry = Entry(root,width=50)
phone_entry.pack(pady=10,padx=20)

email_label = Label(root, text="Email:",font="arial 12")
email_label.pack()
email_entry = Entry(root,width=50)
email_entry.pack(pady=10,padx=20)

address_label = Label(root, text="Address:",font="arial 12")
address_label.pack()
address_entry = Entry(root,width=50)
address_entry.pack(pady=10,padx=20)

add_button = Button(root, bg='black', fg='white', width=15, font='arial 12 bold', text="Add Contact", command=add_contact)
add_button.pack(padx=10,pady=10)

delete_button = Button(root, bg='black', fg='white', width=15, font='arial 12 bold', text="Delete Contact", command=delete_contact)
delete_button.pack(padx=10,pady=10)

clear_button = Button(root, bg='black', fg='white', width=15, font='arial 12 bold', text="Clear Contact", command=clear_contacts)
clear_button.pack(padx=10,pady=10)
 

contact_list = Listbox(root, bd=3, relief=RIDGE, x=10, y=120, width=100, height=26)
contact_list.pack()

contact_list.bind('<<ListboxSelect>>', get_selected_contact)

root.mainloop()