from tkinter import *
from tkinter.messagebox import *
import pymysql
from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from datetime import date

def f1():
	adst.deiconify()
	root.withdraw()
      
def f2():
	root.deiconify()
	adst.withdraw()
	
def f3():
	adbk.deiconify()
	root.withdraw()

def f4():
	root.deiconify()
	adbk.withdraw()
      
def f5():
    viis.deiconify()
    root.withdraw()

def f6():
    root.deiconify()
    viis.withdraw()

def f7():
    viun.deiconify()
    root.withdraw()

def f8():
    root.deiconify()
    viun.withdraw()

def f9():
     rebk.deiconify()
     root.withdraw()

def f10():
    root.deiconify()
    rebk.withdraw()

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="AviRaj",
    database="sms"
)

def updateIssuedStatus(bid):
    sql = f"update books set `issued?` = 1 where books.book_id = {bid}"
    try:
        mycursor.execute(sql)
    except Exception as e:
        mydb.rollback()
        showerror("Error" , f"Error occured:{e}") 
        

def updateReturnStatus(bid):
    sql = f"update books set `issued?` = 0 where books.book_id = {bid}"
    try:
        mycursor.execute(sql)
    except Exception as e:
        mydb.rollback()
        showerror("Error" , f"Error occured:{e}") 
    

mycursor = mydb.cursor()



def returnBook():
    id_value = res.get()
    # print(id_value)
    sql1 = f"Select book_issued from students where id = {id_value}"
    sql = f"Delete from students where students.id =  {id_value}"
    result = mycursor.execute(sql1)
    issued_book_id = mycursor.fetchone()[0]
    mycursor.execute(sql)
    updateReturnStatus(issued_book_id)
    mydb.commit()
    showinfo("Success" , "Book Returned Successfully")

# add students
        
def add_student():
    id_value = id.get()
    name_value = name.get()
    class_value = sclass.get()
    branch_value = branch.get()
    book_issued_value = book_issued.get()
    issue_date_value = date.today()

    sql = "INSERT INTO students(id, name, class, branch, book_issued , issued_date) VALUES (%s, %s, %s, %s, %s ,%s)"
    val = (id_value , name_value , class_value , branch_value , book_issued_value , issue_date_value)
    mycursor.execute(sql, val )
    updateIssuedStatus(book_issued_value)
    
    mydb.commit()
    showinfo("Success", "Student added successfully.")
	

# ADD BOOKS
    
def add_books():
    # Retrieve values from Entry widgets
    book_id_value = book_id_entry.get()
    name_value = name_entry.get()
    publisher_name_value = publisher_name_entry.get()
    issued_value = issued_entry.get()

    sql = "INSERT INTO books (book_id, name, publisher_name , `issued?`) VALUES (%s, %s, %s , %s)"
    val = (book_id_value, name_value, publisher_name_value , issued_value)
    
    try:

        mycursor.execute(sql, val)
        mydb.commit()
        showinfo("Success", "Book added successfully")
    except Exception as e:
        mydb.rollback()
        showerror("Error", f"Error occurred: {e}")


# view issued books

def viis():
    viis.deiconify()
    root.withdraw()
    stdata.delete(1.0, END)
    sql1 = "SELECT students.id, students.name, students.class, students.branch, books.name, students.issued_date FROM students INNER JOIN books on students.book_issued = books.book_id where books.`issued?` = 1"
    try:
        mycursor.execute(sql1)
        # print(result)

        data = mycursor.fetchall()
        # print(data)
        
        for d in data:
             stdata.insert(END, f"Student ID: {d[0]}\nStudent Name: {d[1]}\nClass: {d[2]}\nBranch: {d[3]}\nBook Name: {d[4]}\nIssued Date: {d[5]}\n\n")
    except Exception as e:
         mydb.rollback()
         showerror("Error", f"Error Occurred: {e}")



# view unissued boooks

def viun():
    viun.deiconify()
    root.withdraw()
    stdata1.delete(1.0,END)
    sql2 = "select * from books where books.`issued?` = 0"
    try:
        mycursor.execute(sql2)
        data = mycursor.fetchall()
        for d in data:
             stdata1.insert(END ,f"Book Id : {d[0]}\nBook Name : {d[1]}\nBook Publisher : {d[2]}")
    except Exception as e:
         mydb.rollback()
         showerror("Error" , f"Error Occured : {e}")

      


# L . M . S
root = Tk()
root.title("Library Management System")
root.geometry("700x700+500+100")
root.configure(background="#a8dadc")

lbl1 = Label(root , text = ("Hello!"), font = ("Times New Roman" , 30))
lbl1.pack(pady = 10)

adds = Button(root , text = "ADD STUDENT" , font = ("Times New Roman" , 20) , command = f1)
adds.pack(pady = 20)

addb = Button(root , text = "ADD BOOKS" , font = ("Times New Roman" , 20) , command = f3)
addb.pack(pady = 20)

viis = Button(root , text = "VIEW ISSUED BOOKS" , font = ("Times New Roman" , 20) , command = viis)
viis.pack(pady = 20)

viun = Button(root , text = "VIEW UNISSUED BOOKS" , font = ("Times New Roman" , 20) , command = viun)
viun.pack(pady = 20)

returnBook = Button(root , text = "Return Book" , font = ("Times New Roman" , 20) , command = f9)
returnBook.pack(pady = 20)



# ADD STUDENT

adst = Toplevel(root)
adst.title("ADD STUDENT")
adst.geometry("700x700+500+100")
adst.configure(background="#a8dadc")
adst.withdraw()

id_label = Label(adst, text="Enter the student library card number", font=("Times New Roman", 16))
id_label.pack(pady=5)
id = Entry(adst, font=("Times New Roman", 16))
id.pack(pady=5)

name_label = Label(adst, text="Enter the student name", font=("Times New Roman", 16))
name_label.pack(pady=5)
name = Entry(adst, font=("Times New Roman", 16))
name.pack(pady=5)

class_label = Label(adst, text="Enter the student class", font=("Times New Roman", 16))
class_label.pack(pady=5)
sclass = Entry(adst, font=("Times New Roman", 16))
sclass.pack(pady=5)

branch_label = Label(adst, text="Enter the student branch", font=("Times New Roman", 16))
branch_label.pack(pady=5)
branch = Entry(adst, font=("Times New Roman", 16))
branch.pack(pady=5)

book_issued_label = Label(adst, text="Enter the id of book issued", font=("Times New Roman", 16))
book_issued_label.pack(pady=5)
book_issued = Entry(adst, font=("Times New Roman", 16))
book_issued.pack(pady=5)

# issue_date_label = Label(adst, text="Enter the issue date of book", font=("Times New Roman", 16))
# issue_date_label.pack(pady=5)
# issue_date = Entry(adst, font=("Times New Roman", 16))
# issue_date.pack(pady=5)

submit_button = Button(adst, text="Submit", font=("Times New Roman", 16), command=add_student)
submit_button.pack(pady=10)

back_button = Button(adst, text="Back", font=("Times New Roman", 16), command = f2)
back_button.pack(pady=10)



# ADD BOOKS 

adbk = Toplevel(root)
adbk.title("ADD BOOKS")
adbk.geometry("700x700+500+100")
adbk.configure(background="#a8dadc")
adbk.withdraw()


book_id_label = Label(adbk, text="Enter the id of book", font=("Times New Roman", 16))
book_id_label.pack(pady=10)
book_id_entry = Entry(adbk, font=("Times New Roman", 16))
book_id_entry.pack()

name_label = Label(adbk, text="Enter the name of book", font=("Times New Roman", 16))
name_label.pack(pady=20)
name_entry = Entry(adbk, font=("Times New Roman", 16))
name_entry.pack(pady=10)

publisher_name_label = Label(adbk, text="Enter the name of Book Publisher", font=("Times New Roman", 16))
publisher_name_label.pack(pady=20)
publisher_name_entry = Entry(adbk, font=("Times New Roman", 16))
publisher_name_entry.pack(pady=10)

issued_label = Label(adbk, text="Is the book issued?", font=("Times New Roman", 16))
issued_label.pack(pady=20)
issued_entry = Entry(adbk, font=("Times New Roman", 16))
issued_entry.pack(pady=10)

submit = Button(adbk , text = "Submit" ,  font=("Times New Roman", 16) , command = add_books)
submit.pack(pady = 20)

back_button = Button(adbk, text="Back", font=("Times New Roman", 16), command = f4)
back_button.pack(pady=10)


# view issued books

viis=Toplevel(root)
viis.title("View Issued Books")
viis.geometry("700x700+500+100")
viis.configure(background="#a8dadc")
viis.withdraw()

stdata=ScrolledText(viis,width=45, height=25)
btnvback=Button(viis,text="Back", font=("Times New Roman",18,"bold"),command=f6)

stdata.pack(pady=5)
btnvback.pack(pady=5)

# view unissued books
viun=Toplevel(root)
viun.title("View Student")
viun.geometry("700x700+500+100")
viun.configure(background="#a8dadc")
viun.withdraw()

stdata1=ScrolledText(viun,width=45, height=25)
btnvback=Button(viun,text="Back", font=("Times New Roman",18,"bold"),command=f8)

stdata1.pack(pady=5)
btnvback.pack(pady=5)

# return book

rebk = Toplevel(root)
rebk.title("Return Book")
rebk.geometry("600x600+500+100")
rebk.configure(background="#a8dadc")
rebk.withdraw()


res_label = Label(rebk , text = "Enter the id of student" , font = ("Times New Roman" , 18 , "bold"))
res_label.pack(pady = 10)

res = Entry(rebk , font = ("Times New Roman" , 18 , "bold"))
res.pack(pady = 10)

# reb_label = Label(rebk , text = "Enter the id of book returned" , font = ("Times New Roman" , 18 , "bold"))
# reb_label.pack(pady = 10)

# reb = Entry(rebk , font = ("Times New Roman" , 18 , "bold"))
# reb.pack(pady = 10)

returnSubmit = Button(rebk , text = "Submit" , font = ("Times New Roman" , 18 , "bold") , command = returnBook)
returnSubmit.pack(pady = 10)


back = Button(rebk , text = "Back" , font = ("Times New Roman" , 18 , "bold") , command = f10)
back.pack(pady = 10)

root.mainloop()