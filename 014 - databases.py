
#using databases with tkinter

import sqlite3 #import the database module, built in with python
from tkinter import *

root = Tk()
root.title("Tkinter & databases")
root.geometry("400x400")

#--------------------------------------------------------

#create db or connect to one
conn = sqlite3.connect('address_book.db') #connect to a given db

# create cursor, that will retrieve info from db
c = conn.cursor()

'''
#create table
# this will create a db file in the dir where the current script is stored
c.execute("""CREATE TABLE addresses(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        contact_num integer
        )""")
# this only need to be run once, after which we can just comment out
 '''

#----------------------------------------------------------------

# add items to db function
def submit():
    conn = sqlite3.connect('address_book.db') #connect to a given db
    c = conn.cursor()    # create cursor, that will retrieve info from db

    #insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :addr, :cty, :st, :c_num)",
              # create a dict for key/value pairs
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'addr': addr.get(),
                  'cty': cty.get(),
                  'st': st.get(),
                  'c_num': c_num.get()
              }
              
              )

    conn.commit()    # any changes to db, need to be committed
    conn.close()    # need to close the connection when done

    f_name.delete(0,END) # clear text boxes
    l_name.delete(0, END)
    addr.delete(0, END)
    cty.delete(0, END)
    st.delete(0, END)
    c_num.delete(0, END)

def retrieve():
    conn = sqlite3.connect('address_book.db') #connect to a given db
    c = conn.cursor()    # create cursor, that will retrieve info from db

    #query the db
    c.execute("SELECT *, oid FROM addresses") # oid is auto created by sqlite as a primary key, but we have to explicitly refer to it 
    records = c.fetchall() # fetches all records

    # loop through results 
    print_records = ''
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ': ' + str(record[2]) + ', ' + str(record[3]) + ', ' + str(record[4]) + ', ' + str(record[5]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2)
    conn.commit()    # any changes to db, need to be committed
    conn.close()    # need to close the connection when done


#----------------------------------------------------------------
#widgets:

# create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=3)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20, pady=3)

addr = Entry(root, width=30)
addr.grid(row=2, column=1, padx=20, pady=3)

cty = Entry(root, width=30)
cty.grid(row=3, column=1, padx=20, pady=3)

st = Entry(root, width=30)
st.grid(row=4, column=1, padx=20, pady=3)

c_num = Entry(root, width=30)
c_num.grid(row=5, column=1, padx=20, pady=3)

# create labels
f_name_label = Label(root, text='first name:')
f_name_label.grid(row=0, column=0, padx=2)

l_name_label = Label(root, text='last name:')
l_name_label.grid(row=1, column=0, padx=2)

addr_label = Label(root, text='address:')
addr_label.grid(row=2, column=0, padx=2)

cty_label = Label(root, text='city:')
cty_label.grid(row=3, column=0, padx=2)

st_label = Label(root, text='state:')
st_label.grid(row=4, column=0, padx=2)

c_num_label = Label(root, text='contact number:')
c_num_label.grid(row=5, column=0, padx=2)


# create submit button
submit_button = Button(root, text="add record to database", command=submit)
submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

#create query button
query_button = Button(root, text="retrieve record from database", command=retrieve)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=83)



#-------------------------------------------------------------

# any changes to db, need to be committed
conn.commit()

# need to close the connection when done
conn.close()

root.mainloop()