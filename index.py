# Imports
from tkinter import *
import sqlite3
from PIL import ImageTk, Image
import os
import tkinter.font

root = tkinter.Tk()
root.title('phone-book')
# icon for the app
# icon file should be in the same project directory
root.iconbitmap('phonebook.ico')
root.geometry('350x650')
# databse name is phonebook.db
conn = sqlite3.connect('phonebook.db')
c = conn.cursor()
# creating a table in a database, execute it only once
'''
c.execute(
    """CREATE TABLE addresses(first_name text, last_name text, phone_number integer, email_id varchar, addresses text, city text, state text, zipcode integer)""")
    '''
# labels for entry widgets for root
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=1, column=4, padx=25, pady=25)
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=2, column=4, padx=25, pady=25)
phone_number_label = Label(root, text="Phone Number")
phone_number_label.grid(row=3, column=4, padx=25, pady=25)
email_id_label = Label(root, text="Email")
email_id_label.grid(row=4, column=4, padx=25, pady=25)
address_label = Label(root, text="Address")
address_label.grid(row=5, column=4, padx=25, pady=25)
city_label = Label(root, text="city")
city_label.grid(row=6, column=4, padx=25, pady=25)
state_label = Label(root, text="State")
state_label.grid(row=7, column=4, padx=25, pady=25)
zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row=8, column=4, padx=25, pady=25)
# entry (Input) widgets for root
f_name = Entry(root, width=30)
f_name.grid(row=1, column=5)
l_name = Entry(root, width=30)
l_name.grid(row=2, column=5)
phone_number = Entry(root, width=30)
phone_number.grid(row=3, column=5)
email_id = Entry(root, width=30)
email_id.grid(row=4, column=5)
address = Entry(root, width=30)
address.grid(row=5, column=5)
city = Entry(root, width=30)
city.grid(row=6, column=5)
state = Entry(root, width=30)
state.grid(row=7, column=5)
zipcode = Entry(root, width=30)
zipcode.grid(row=8, column=5)


# deleting data from the database (function)
def delete():
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    # delete data from tables
    c.execute("DELETE FROM addresses WHERE oid = " + delete_box.get())
    delete_box.delete(0, END)
    conn.commit()
    conn.close()


# submitting data to database (function)
def submit():
    # creating the connection
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    # insert data into tables
    c.execute(
        "INSERT INTO addresses VALUES(:f_name, :l_name, :phone_number, :email_id, :address, :city, :state, :zipcode)",
        {'f_name': f_name.get(),
         'l_name': l_name.get(),
         'phone_number': phone_number.get(),
         'email_id': email_id.get(),
         'address': address.get(),
         'city': city.get(),
         'state': state.get(),
         'zipcode': zipcode.get()
         })
    # clearing the boxes, on pressing add record button
    f_name.delete(0, END)
    l_name.delete(0, END)
    phone_number.delete(0, END)
    email_id.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)
    # closing the connection
    conn.commit()
    conn.close()


# creating add record button
submit_btn = Button(root, text="add record", command=submit)
submit_btn.grid(row=20, column=3, columnspan=2, pady=20, padx=20)


# fetching data from the database (function)
def query():
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    # fetching data from tables
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # below line is used to print data into close but not to window
    #  print(records)
    print_records = ''
    for record in records:
        # printing data into text window
        print_records += "ID : " + str(record[8]) + ", " + "First Name : " + str(
            record[0]) + ", " + "Last Name : " + str(
            record[1]) + ", " + "Phone Number : " + str(record[2]) + ", " + "Email : " + str(
            record[3]) + ", " + "\n" + "Address : " + str(record[4]) + ", " + "City : " + str(
            record[5]) + ", " + "State : " + str(record[6]) + ", " + "Zipcode : " + str(record[7]) + "\n" + "\n"
    return print_records
    # topLevel window is shown up when we press "show records" button
    top = Toplevel(root)
    # "show records" label
    query_label = Label(top, text="print_records")
    query_label.grid(row=25, column=2, columnspan=2)
    conn.commit()
    conn.close()


# creating a show records button
query_btn = Button(root, text="show records", command=lambda: (text.delete(1.0, END), text.insert(END, query())))
query_btn.grid(row=20, column=5, columnspan=2, pady=20, padx=20)
top = Toplevel(root)


# updating data from the database (function)
def update():
    # labels for topLevel window
    f_name_label_editor = Label(top, text="First Name")
    f_name_label_editor.place(relx=0.3, rely=0.4, anchor=NE)
    l_name_label_editor = Label(top, text="Last Name")
    l_name_label_editor.place(relx=0.3, rely=0.5, anchor=NE)
    phone_number_label_editor = Label(top, text="Phone Number")
    phone_number_label_editor.place(relx=0.3, rely=0.6, anchor=NE)
    email_id_label_editor = Label(top, text="Email")
    email_id_label_editor.place(relx=0.3, rely=0.7, anchor=NE)
    address_label_editor = Label(top, text="Address")
    address_label_editor.place(relx=0.6, rely=0.4, anchor=NE)
    city_label_editor = Label(top, text="city")
    city_label_editor.place(relx=0.6, rely=0.5, anchor=NE)
    state_label_editor = Label(top, text="State")
    state_label_editor.place(relx=0.6, rely=0.6, anchor=NE)
    zipcode_label_editor = Label(top, text="zipcode")
    zipcode_label_editor.place(relx=0.6, rely=0.7, anchor=NE)
    # global variables
    global f_name_editor
    global l_name_editor
    global phone_number_editor
    global email_id_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    # entry (input) widgets for topLevel window
    f_name_editor = Entry(top, width=30)
    f_name_editor.place(relx=0.5, rely=0.4, anchor=NE)
    l_name_editor = Entry(top, width=30)
    l_name_editor.place(relx=0.5, rely=0.5, anchor=NE)
    phone_number_editor = Entry(top, width=30)
    phone_number_editor.place(relx=0.5, rely=0.6, anchor=NE)
    email_id_editor = Entry(top, width=30)
    email_id_editor.place(relx=0.5, rely=0.7, anchor=NE)
    address_editor = Entry(top, width=30)
    address_editor.place(relx=0.8, rely=0.4, anchor=NE)
    city_editor = Entry(top, width=30)
    city_editor.place(relx=0.8, rely=0.5, anchor=NE)
    state_editor = Entry(top, width=30)
    state_editor.place(relx=0.8, rely=0.6, anchor=NE)
    zipcode_editor = Entry(top, width=30)
    zipcode_editor.place(relx=0.8, rely=0.7, anchor=NE)
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    record_id = delete_box.get()
    # updating data from tables
    c.execute(
        "SELECT first_name, last_name, phone_number, email_id, addresses, city, state, zipcode FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    for record in records:
        # Inserting data that is fetched from database into input fields
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        phone_number_editor.insert(0, record[2])
        email_id_editor.insert(0, record[3])
        address_editor.insert(0, record[4])
        city_editor.insert(0, record[5])
        state_editor.insert(0, record[6])
        zipcode_editor.insert(0, record[7])
    conn.commit()
    conn.close()


# saving data after updating (function)
def save():
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    record_id = delete_box.get()
    # updating data from the database after updating
    c.execute(
        """UPDATE addresses SET first_name = :first,last_name = :last,phone_number = :phone,email_id = :email,addresses = :addresses,city = :city,state = :state,zipcode = :zipcode WHERE oid = :oid""",
        {
            'first': f_name_editor.get(),
            'last': l_name_editor.get(),
            'phone': phone_number_editor.get(),
            'email': email_id_editor.get(),
            'addresses': address_editor.get(),
            'city': city_editor.get(),
            'state': state_editor.get(),
            'zipcode': zipcode_editor.get(),
            'oid': record_id
        })
    f_name_editor.delete(0, END)
    l_name_editor.delete(0, END)
    phone_number_editor.delete(0, END)
    email_id_editor.delete(0, END)
    address_editor.delete(0, END)
    city_editor.delete(0, END)
    state_editor.delete(0, END)
    zipcode_editor.delete(0, END)
    conn.commit()
    conn.close()


# searching data in the database by using id
def search():
    conn = sqlite3.connect('phonebook.db')
    c = conn.cursor()
    record_id = delete_box.get()
    # fetching data from the database for displaying it in text widget
    c.execute(
        "SELECT first_name, last_name, phone_number, email_id, addresses, city, state, zipcode FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += "First Name : " + str(
            record[0]) + ", " + "Last Name : " + str(
            record[1]) + ", " + "Phone Number : " + str(record[2]) + ", " + "Email : " + str(
            record[3]) + ", " + "\n" + "Address : " + str(record[4]) + ", " + "City : " + str(
            record[5]) + ", " + "State : " + str(record[6]) + ", " + "Zipcode : " + str(record[7]) + "\n" + "\n"
    return print_records
    conn.commit()
    conn.close()


# global variable
global email_id_editor

# delete box label
delete_box_label = Label(top, text="ID Number")
delete_box_label.place(anchor=NW, relx=0, rely=0.5)
# entry (input) widget
delete_box = Entry(top, width=30)
delete_box.place(anchor=NW, relx=0.1, rely=0.5)
# delete button widget
delete_btn = Button(top, text="Delete Records", command=delete)
delete_btn.place(anchor=NE, relx=0.9, rely=0.7)
update_btn = Button(top, text="Fetch Record", command=update)
update_btn.place(relx=0.9, rely=0.4, anchor=NE)
save_btn = Button(top, text="Update Record", command=save)
save_btn.place(relx=0.9, rely=0.5, anchor=NE)
# search button
search_btn = Button(top, text="Search Records", command=lambda: (text.delete(1.0, END), text.insert(END, search())))
search_btn.place(relx=0.9, rely=0.6, anchor=NE)
# show all records button
show_all_records = Button(top, text="Show All Records",
                          command=lambda: (text.delete(1.0, END), text.insert(END, query())))
show_all_records.place(relx=0.6, rely=0.8, anchor=NE)
# textbox
top.geometry("1500x1500")
# icon for app
top.iconbitmap('phonebook.ico')
# text widget for topLevel window
text = Text(top, height=10, width=200)
text.grid(row=0, column=0)
# closing topLevel window
top.mainloop()
conn.commit()
conn.close()
# closing main window
root.mainloop()
