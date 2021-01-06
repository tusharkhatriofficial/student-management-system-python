from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import mysql.connector

font = "gabriola"
font2 = "Imprint MT Shadow"
# colour = "#121212"
colour = "#302F2E"
btn_colour = "#393737"
btn_textcolour = "white"




class ConnectorDB:

    def __init__(self, root):
        self.root = root
        titlespace = " "
        self.root.wm_iconbitmap('assets/1.ico')
        self.root.configure(bg=colour)
        self.root.title(102 * titlespace + "Developersonline")
        self.root.geometry("779x616+300+0")
        self.root.resizable(width=False, height=False)


        MainFrame = Frame(self.root, width=770, height=700, relief=RIDGE, bg=colour)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width=770, height=100, relief=RIDGE, bg=colour)
        TitleFrame.grid(row=0, column=0)
        TopFrame3= Frame(MainFrame, width=770, height=500, relief=RIDGE, bg=colour)
        TopFrame3.grid(row=1, column=0)

        LeftFrame = Frame(TopFrame3, width=770, height=400, padx=2, bg=colour, relief=RIDGE)
        LeftFrame.pack(side=LEFT)

        LeftFrame1= Frame(LeftFrame, width=600, height=100, padx=2, pady=4, relief=RIDGE, bg=colour)
        LeftFrame1.pack(side=TOP, padx=0, pady=0)

        RightFrame1= Frame(TopFrame3,width=100, height=400, padx=2, bg=colour, relief=RIDGE)
        RightFrame1.pack(side=LEFT)

        RightFrame1a= Frame(RightFrame1,width=90, height=300, padx=2, pady=2, relief=RIDGE, bg=colour)
        RightFrame1a.pack(side=TOP)
        #=========================================variables declaration=========================================================
        StudentId= StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        Address = StringVar()
        Gender = StringVar()
        Mobile = StringVar()

        #==========================================Function declaration===========================================================
        def iExit():
            iExit = tkinter.messagebox.askyesno("Student Management System", "Do you want to exit ?")
            if iExit>0:
                root.destroy()
                return
        def Clear():
            self.entStudentId.delete(0, END)
            self.entFirstName.delete(0, END)
            self.entLastName.delete(0, END)
            self.entAddress.delete(0, END)
            Gender.set("")
            self.entMobile.delete(0, END)


        def displayData():
            mycon = mysql.connector.connect(host="localhost", user="root", passwd="Clashofclans@320",
                                            database="testing")
            cursor = mycon.cursor()
            cursor.execute("SELECT * from testing_table")
            result = cursor.fetchall()
            if len(result) != 0:
                self.student_records.delete(*self.student_records.get_children())
                for row in result:
                    self.student_records.insert('', END, values=row)
            # cursor.commit()
            cursor.close()

        def addData():
            if StudentId.get() == "" or Firstname.get() == "" or Lastname.get() == "":
                tkinter.messagebox.showerror("Student Management System", "All field are mandatory")
            else:
                mycon = mysql.connector.connect(host="localhost", user="root", passwd="Clashofclans@320", database="testing")
                cursor = mycon.cursor()
                if mycon.is_connected():
                    cursor.execute("insert into testing_table values(%s,%s,%s,%s,%s,%s)", (
                        StudentId.get(),
                        Firstname.get(),
                        Lastname.get(),
                        Address.get(),
                        Gender.get(),
                        Mobile.get(),
                    ))
                    mycon.commit()
                    mycon.close()
                    displayData()
                else:
                    tkinter.messagebox.showwarning("Student Management System", "Problem connecting to the database")

        def studentInfo(ev):
            viewInfo = self.student_records.focus()
            learnerData = self.student_records.item(viewInfo)
            row = learnerData['values']
            StudentId.set(row[0])
            Firstname.set(row[1])
            Lastname.set(row[2])
            Address.set(row[3])
            Gender.set(row[4])
            Mobile.set(row[5])
        def update():
            mycon = mysql.connector.connect(host="localhost", user="root", passwd="Clashofclans@320",
                                            database="testing")
            cursor = mycon.cursor()
            if mycon.is_connected():
                cursor.execute("UPDATE Testing_table SET firstname=%s,lastname=%s,address=%s,gender=%s,mobile=%s WHERE stdid=%s", (

                    Firstname.get(),
                    Lastname.get(),
                    Address.get(),
                    Gender.get(),
                    Mobile.get(),
                    StudentId.get()
                ))
                mycon.commit()
                mycon.close()
                displayData()
                tkinter.messagebox.showwarning("Student Management System", "Record updated sucessfully")
        def delete():

            mycon = mysql.connector.connect(host="localhost", user="root", passwd="Clashofclans@320",
                                            database="testing")
            cursor = mycon.cursor()
            # cursor.execute("DELETE from Testing_table WHERE stdid=%s",StudentId.get())
            cursor.execute(
                "DELETE from Testing_table WHERE stdid={}".format(StudentId.get())
            )

            mycon.commit()
            mycon.close()
            displayData()
            tkinter.messagebox.showwarning("Student Management System", "Record deleted")

        def search():
            try:
                mycon = mysql.connector.connect(host="localhost", user="root", passwd="Clashofclans@320",
                                                database="testing")
                cursor = mycon.cursor()
                # cursor.execute("DELETE from Testing_table WHERE stdid=%s",StudentId.get())
                cursor.execute(
                    "SELECT * from Testing_table WHERE stdid={}".format(StudentId.get())
                )
                row = cursor.fetchone()

                StudentId.set(row[0])
                Firstname.set(row[1])
                Lastname.set(row[2])
                Address.set(row[3])
                Gender.set(row[4])
                Mobile.set(row[5])

                mycon.commit()
            except:
                tkinter.messagebox.showwarning("Student Management System", "Record Searched")
            mycon.close()
        #=========================================================================================================================
        self.lbltitle=Label(TitleFrame, font=(font, 35, 'bold'), text="Student Management System", bd=7, foreground="white", bg=colour)
        self.lbltitle.grid(row=0, column=0, padx=132)
        #=====================================================================================================
        self.lblStudentId = Label(LeftFrame1, font=(font, 12, 'bold'), text="Admission Number", bg=colour, foreground="white")
        self.lblStudentId.grid(row=1, column=0, sticky=W, padx=5)
        self.entStudentId = Entry(LeftFrame1, font=(font2, 12, 'bold'), width=44, justify='left', textvariable=StudentId, bd=5)
        self.entStudentId.grid(row=1, column=1, sticky=W, padx=5)

        self.lblFirstName = Label(LeftFrame1, font=(font, 12, 'bold'), text="First Name", bg=colour, foreground="white")
        self.lblFirstName.grid(row=2, column=0, sticky=W, padx=5)
        self.entFirstName = Entry(LeftFrame1, font=(font2, 12, 'bold'), bd=5, width=44, justify='left', textvariable=Firstname)
        self.entFirstName.grid(row=2, column=1, sticky=W, padx=5)

        self.lblLastName = Label(LeftFrame1, font=(font, 12, 'bold'), text="Last Name", bg=colour, foreground="white")
        self.lblLastName.grid(row=3, column=0, sticky=W, padx=5)
        self.entLastName = Entry(LeftFrame1, font=(font2, 12, 'bold'), bd=5, width=44, justify='left', textvariable=Lastname)
        self.entLastName.grid(row=3, column=1, sticky=W, padx=5)

        self.lblAddress = Label(LeftFrame1, font=(font, 12, 'bold'), text="Address", bg=colour, foreground="white")
        self.lblAddress.grid(row=4, column=0, sticky=W, padx=5)
        self.entAddress = Entry(LeftFrame1, font=(font2, 12, 'bold'), bd=5, width=44, justify='left', textvariable=Address)
        self.entAddress.grid(row=4, column=1, sticky=W, padx=5)

        self.lblGender = Label(LeftFrame1, font=(font, 12, 'bold'), text="Gender", bg=colour, foreground="white")
        self.lblGender.grid(row=5, column=0, sticky=W, padx=5)
        self.cboGender = ttk.Combobox(LeftFrame1, font=(font2, 12, 'bold'), width=43, state="readonly", textvariable=Gender)
        self.cboGender["values"] = ('', 'Male', 'Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=5, column=1, sticky=W, padx=5)

        self.lblMobile = Label(LeftFrame1, font=(font, 12, 'bold'), text="Mobile", bg=colour, foreground="white")
        self.lblMobile.grid(row=6, column=0, sticky=W, padx=5)
        self.entMobile = Entry(LeftFrame1, font=(font2, 12, 'bold'), bd=5, width=44, justify='left', textvariable=Mobile)
        self.entMobile.grid(row=6, column=1, sticky=W, padx=5)
        #===========================================================Table TreeView============================================================

        scroll_Y = Scrollbar(LeftFrame, orient=VERTICAL)
        self.student_records=ttk.Treeview(LeftFrame, height='12', columns=("stdid", "firstname", "lastname", "address",
        "gender", "mobile"), yscrollcommand = scroll_Y.set)
        scroll_Y.pack(side= RIGHT, fill=Y)

        self.student_records.heading("stdid", text="Student Id")
        self.student_records.heading("firstname", text="First Name")
        self.student_records.heading("lastname", text="Last Name")
        self.student_records.heading("address", text="Address")
        self.student_records.heading("gender", text="Gender")
        self.student_records.heading("mobile", text="Mobile")

        self.student_records['show'] = 'headings'

        self.student_records.column("stdid", width="70")
        self.student_records.column("firstname", width="100")
        self.student_records.column("lastname", width="100")
        self.student_records.column("address", width="100")
        self.student_records.column("gender", width="70")
        self.student_records.column("mobile", width="70")

        self.student_records.pack(fill=BOTH, expand=1)
        self.student_records.bind("<ButtonRelease-1>", studentInfo)
        # displayData()

        #=======================================================================================================================
        self.btnAddNew = Button(RightFrame1a, font=(font2, 16, 'bold'), text="Add New", pady=1, padx=24, #button1
                              width=7, height=2, command=addData, bg=btn_colour, foreground=btn_textcolour).grid(row=0, column=0, padx=1)
        self.btnDisplay = Button(RightFrame1a, font=(font2, 16, 'bold'), text="Display", pady=1, padx=24, #button2
                                width=7, height=2, command=displayData, bg=btn_colour, foreground=btn_textcolour).grid(row=1, column=0, padx=1)
        self.btnUpdate = Button(RightFrame1a, font=(font2, 16, 'bold'), text="Update", pady=1, padx=24, #button2
                                width=7, height=2, command=update, bg=btn_colour, foreground=btn_textcolour).grid(row=2, column=0, padx=1)
        self.btnDelete = Button(RightFrame1a, font=(font2, 16, 'bold'), text="Delete", pady=1, padx=24, #button4
                                width=7, height=2, command=delete, bg=btn_colour, foreground=btn_textcolour).grid(row=3, column=0, padx=1)
        self.btnSearch = Button(RightFrame1a, font=(font2, 16, 'bold'), text="Search", pady=1, padx=24, #button5
                                width=7, height=2, command=search, bg=btn_colour, foreground=btn_textcolour).grid(row=4, column=0, padx=1)
        self.btnClear = Button(RightFrame1a, font=(font2, 16, 'bold'), text="Clear", pady=1, padx=24, #button6
                                width=7, height=2, command=Clear, bg=btn_colour, foreground=btn_textcolour).grid(row=5, column=0, padx=1)
        self.btnExit = Button(RightFrame1a, font=(font2, 16, 'bold'), text="Exit", pady=1, padx=24, #button7
                                width=7, height=2, command=iExit, bg=btn_colour, foreground=btn_textcolour).grid(row=6, column=0, padx=1)




        #=======================================================================================================================


if __name__=='__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()
