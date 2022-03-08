from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import random
class Room_windows:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1100x480+185+180")
    # variable
        self.contact_var = StringVar()
        self.check_in_date_var = StringVar()
        self.check_out_date_var = StringVar()
        self.room_type_var = StringVar()
        self.available_room_var = StringVar()
        self.meal_var = StringVar()
        self.no_of_days_var = StringVar()
        self.paid_tax_var = StringVar()
        self.sub_total_var = StringVar()
        self.total_cost_var = StringVar()

        # Create Connection
        self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                            database="customer")
        self.my_cursor = self.conn.cursor()

        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 15, "bold"), bg="black",
                          fg="gold")
        lbl_title.place(x=0, y=0, width=1100, height=50)

        # ********************************* Logo Image *****************************
        img1 = Image.open(r"C:\Users\akshay\Desktop\python projects\hotellogoincustomerwindow.png")
        img1.resize((100, 50), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        lblimg1.place(x=3, y=0, width=100, height=50)

        # ******************************* Label Frame *****************
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Details", font=("times new roman",12,"bold"))
        labelframeleft.place(x=3, y=50, width=390, height=420)

        # ************************************ Labels and entries inside Label Frame **************
        # Customer Contact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact:", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)
        entry_cust_contact = ttk.Entry(labelframeleft, textvariable=self.contact_var, width=14, font=("arial", 13, "bold"),)
        entry_cust_contact.grid(row=0, column=1, sticky=W)

        # Fetch data button
        btn_fetch_data=Button(labelframeleft,command=self.Fetch_contact, text="Fetch data", font=("arial", 10, "bold"), bg="black", fg="gold"
                              , width=10)
        btn_fetch_data.place(x=290, y=3)

        # Check in date
        lbl_check_in_date = Label(labelframeleft, text="Check In Date:", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_check_in_date.grid(row=1, column=0, sticky=W)
        entry_check_in_date = ttk.Entry(labelframeleft, textvariable=self.check_in_date_var, width=25, font=("arial", 13, "bold"))
        entry_check_in_date.grid(row=1, column=1)

        # Check out date
        lbl_check_out_date = Label(labelframeleft, text="Check Out Date:", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_check_out_date.grid(row=2, column=0, sticky=W)
        entry_check_out_date = ttk.Entry(labelframeleft,  textvariable=self.check_out_date_var, width=25,font=("arial", 13, "bold"))
        entry_check_out_date.grid(row=2, column=1)

        # Room type
        lbl_room_type = Label(labelframeleft, text="Room Type:", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_room_type.grid(row=3, column=0, sticky=W)
        # Room Type combobox

        self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                            database="customer")
        self.my_cursor = self.conn.cursor()
        self.my_cursor.execute("select Room_Type from details")
        rows = self.my_cursor.fetchall()
        combo_room_type= ttk.Combobox(labelframeleft,  textvariable=self.room_type_var, font=("arial", 12, "bold"), width=23,
                                    state="readonly")
        combo_room_type['value'] = rows
        combo_room_type.current(0)
        combo_room_type.grid(row=3, column=1)

        # Available Room
        lbl_available_room = Label(labelframeleft, text="Available Room:", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_available_room.grid(row=4, column=0, sticky=W)

        self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                            database="customer")
        self.my_cursor = self.conn.cursor()
        self.my_cursor.execute("select Room_No from details")
        row = self.my_cursor.fetchall()

        combo_room_no = ttk.Combobox(labelframeleft, textvariable=self.available_room_var, font=("arial", 12, "bold"),
                                       width=23, state="readonly")
        combo_room_no['value'] = row
        combo_room_no.current(0)
        combo_room_no.grid(row=4, column=1)

        # Meal
        lbl_meal = Label(labelframeleft, text="Meal:", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_meal.grid(row=5, column=0, sticky=W)
        entry_meal = ttk.Entry(labelframeleft,  textvariable=self.meal_var, width=25, font=("arial", 13, "bold"))
        entry_meal.grid(row=5, column=1)

        # No Of Days
        lbl_no_of_days = Label(labelframeleft, text="No Of Days:", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_no_of_days.grid(row=6, column=0, sticky=W)
        entry_no_of_days = ttk.Entry(labelframeleft, textvariable=self.no_of_days_var, width=25, font=("arial", 13, "bold"))
        entry_no_of_days.grid(row=6, column=1)

        # Paid Tax
        lbl_paid_tax = Label(labelframeleft, text="Paid Tax:", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_paid_tax.grid(row=7, column=0, sticky=W)
        entry_paid_tax = ttk.Entry(labelframeleft,textvariable=self.paid_tax_var, width=25, font=("arial", 13, "bold"))
        entry_paid_tax.grid(row=7, column=1)

        # Sub Total
        lbl_sub_total = Label(labelframeleft, text="Sub Total:", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_sub_total.grid(row=8, column=0, sticky=W)
        entry_sub_total = ttk.Entry(labelframeleft,  textvariable=self.sub_total_var, width=25, font=("arial", 13, "bold"))
        entry_sub_total.grid(row=8, column=1)

        # Total Cost
        lbl_total_cost = Label(labelframeleft, text="Total Cost:", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_total_cost.grid(row=9, column=0, sticky=W)
        entry_total_cost = ttk.Entry(labelframeleft, textvariable=self.total_cost_var, width=25, font=("arial", 13, "bold"))
        entry_total_cost.grid(row=9, column=1)

    # Button bill
        btn_bill = Button(labelframeleft, command=self.Total_Cost, text="Bill", font=("arial", 13, "bold"), bg="black",
                         fg="gold", width=8)
        btn_bill.grid(row=10, column=0, padx=1,sticky=W)

        # ********************************** Button Frame ***************************
        btn_frame = Frame(labelframeleft,bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=350, width=380, height=40)

        # ******************** Create button inside Button Frame ****************
        btn_add = Button(btn_frame, command=self.Add_data, text="Add", font=("arial", 14, "bold"), bg="black",
                         fg="gold", width=7)
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, command=self.Update_data, text="Update", font=("arial", 14, "bold"), bg="black",
                            fg="gold", width=7)
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, command=self.Delete_detail, text="Delete", font=("arial", 14, "bold"), bg="black",
                            fg="gold", width=7)
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, command=self.Reset_data,text="Reset", font=("arial", 14, "bold"), bg="black",
                           fg="gold", width=7)
        btn_reset.grid(row=0, column=3, padx=1)

    # ************************************  Right Side image *************************
        img2 = Image.open(r"C:\Users\akshay\Desktop\python projects\hotelinroomwindowsleft.jpg")
        img2.resize((400, 200), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=700, y=55, width=400, height=200)

        # *************************** Table Frame *********************************
        lbl_tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Detail and Search System",
                                    font=("arial", 13, "bold"))
        lbl_tableframe.place(x=400, y=280, width=690, height=190)

        # Label Search By
        lbl_searchby = Label(lbl_tableframe, relief=RIDGE, text="Search By", fg="gold", bg="red",
                             font=("arial", 13, "bold"))
        lbl_searchby.grid(row=0, column=0, padx=2, sticky=W)
        # variable
        self.search = StringVar()
        combosearch = ttk.Combobox(lbl_tableframe,textvariable=self.search, font=("arial", 12, "bold"), width=15, state="readonly")
        combosearch['value'] = ("Contact", "Room")
        combosearch.current(0)
        combosearch.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        entry_search = Entry(lbl_tableframe, textvariable=self.txt_search, font=("arial", 14, "bold"), width=20)
        entry_search.grid(row=0, column=2)

        btn_search = Button(lbl_tableframe, command=self.Search_detail,  text="Search", bg="black", fg="gold",
                            font=("arial", 10, "bold"), width=8)
        btn_search.grid(row=0, column=3, padx=4, sticky=W)

        btn_showall = Button(lbl_tableframe, command=self.Fetch_detail, text="Show All", bg="black", fg="gold",
                             font=("arial", 10, "bold"), width=8)
        btn_showall.grid(row=0, column=4)

    # ********************************* Show Data  Table ***************************

        detailtable=Frame(lbl_tableframe, bd=2, relief=RIDGE)
        detailtable.place(x=3, y=40, width=670, height=125)

        scroll_x = ttk.Scrollbar(detailtable, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailtable, orient=VERTICAL)

        self.Roombooking_detail_Table = ttk.Treeview(detailtable, columns=("Contact","Check In Date","Check Out Date", "Room Type","Room Available",
                                             "Meal","No of Days","Paid Tax","Sub Total","Sub Cost"),
                                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Roombooking_detail_Table.xview)
        scroll_y.config(command=self.Roombooking_detail_Table.yview)

        self.Roombooking_detail_Table.heading('Contact', text="Contact")
        self.Roombooking_detail_Table.heading('Check In Date', text="Check In Date")
        self.Roombooking_detail_Table.heading('Check Out Date', text="Check Out Date" )
        self.Roombooking_detail_Table.heading('Room Type', text="Room Type")
        self.Roombooking_detail_Table.heading('Room Available', text="Room Available")
        self.Roombooking_detail_Table.heading('Meal', text="Meal")
        self.Roombooking_detail_Table.heading('No of Days', text="No of Days")
        self.Roombooking_detail_Table.heading('Paid Tax', text="Paid Tax")
        self.Roombooking_detail_Table.heading('Sub Total', text="Sub Total")
        self.Roombooking_detail_Table.heading('Sub Cost', text="Sub Cost")

        self.Roombooking_detail_Table["show"] = "headings"

        self.Roombooking_detail_Table.column('Contact', width=100)
        self.Roombooking_detail_Table.column('Check In Date', width=100)
        self.Roombooking_detail_Table.column('Check Out Date', width=100)
        self.Roombooking_detail_Table.column('Room Type', width=100)
        self.Roombooking_detail_Table.column('Room Available', width=100)
        self.Roombooking_detail_Table.column('Meal', width=100)
        self.Roombooking_detail_Table.column('No of Days', width=100)
        self.Roombooking_detail_Table.column('Paid Tax', width=100)
        self.Roombooking_detail_Table.column('Sub Total', width=100)
        self.Roombooking_detail_Table.column('Sub Cost', width=100)

        self.Roombooking_detail_Table.pack(fill=BOTH, expand=1)
        self.Fetch_detail()
        self.Roombooking_detail_Table.bind("<ButtonRelease-1>",self.Get_detail)
    # Fetch all Data
    def Fetch_contact(self):
        if self.contact_var.get() == "":
            messagebox.showerror("Error", "Please Enter Contact Number", parent=self.root)
        else:
            self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                               database="customer")
            self.my_cursor = self.conn.cursor()
            query = "select Customer_Name from customer_table where Mobile_No=%s"
            value = (self.contact_var.get(),)
            self.my_cursor.execute(query, value)
            row = self.my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "This Number Not Found", parent=self.root)
            else:
                self.conn.commit()
                self.conn.close()

                showdataframe=Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showdataframe.place(x=400, y=55, width=300, height=210)

                lblname=Label(showdataframe, text="Name", font=("arial", 12, "bold"))
                lblname.place(x=0, y=0)

                lbl = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                                    database="customer")
                self.my_cursor = self.conn.cursor()

                query = "select Gender from customer_table where Mobile_No=%s"
                value = (self.contact_var.get(),)
                self.my_cursor.execute(query, value)
                row = self.my_cursor.fetchone()
                lblname = Label(showdataframe, text="Gender", font=("arial", 12, "bold"))
                lblname.place(x=0,y=20)
                lbl = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=20)

                query = "select Mother_Name from customer_table where Mobile_No=%s"
                value = (self.contact_var.get(),)
                self.my_cursor.execute(query, value)
                row = self.my_cursor.fetchone()
                lblname = Label(showdataframe, text="Mother Name", font=("arial", 12, "bold"))
                lblname.place(x=0, y=40)
                lbl = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=40)

                query = "select Post_Code from customer_table where Mobile_No=%s"
                value = (self.contact_var.get(),)
                self.my_cursor.execute(query, value)
                row = self.my_cursor.fetchone()
                lblname = Label(showdataframe, text="Post Code", font=("arial", 12, "bold"))
                lblname.place(x=0, y=60)
                lbl = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=60)

                query = "select Ref_No from customer_table where Mobile_No=%s"
                value = (self.contact_var.get(),)
                self.my_cursor.execute(query, value)
                row = self.my_cursor.fetchone()
                lblname = Label(showdataframe, text="Ref No", font=("arial", 12, "bold"))
                lblname.place(x=0, y=80)
                lbl = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=80)

                query = "select Nationality from customer_table where Mobile_No=%s"
                value = (self.contact_var.get(),)
                self.my_cursor.execute(query, value)
                row = self.my_cursor.fetchone()
                lblname = Label(showdataframe, text="Nationality", font=("arial", 12, "bold"))
                lblname.place(x=0, y=100)
                lbl = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=100)

                query = "select Id_Type from customer_table where Mobile_No=%s"
                value = (self.contact_var.get(),)
                self.my_cursor.execute(query, value)
                row = self.my_cursor.fetchone()
                lblname = Label(showdataframe, text="Id Type", font=("arial", 12, "bold"))
                lblname.place(x=0, y=120)
                lbl = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=120)


                query = "select Id_Proof from customer_table where Mobile_No=%s"
                value = (self.contact_var.get(),)
                self.my_cursor.execute(query, value)
                row = self.my_cursor.fetchone()
                lblname = Label(showdataframe, text="Id Proof", font=("arial", 12, "bold"))
                lblname.place(x=0, y=140)
                lbl = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=140)


                query = "select Address from customer_table where Mobile_No=%s"
                value = (self.contact_var.get(),)
                self.my_cursor.execute(query, value)
                row = self.my_cursor.fetchone()
                lblname = Label(showdataframe, text="Address", font=("arial", 12, "bold"))
                lblname.place(x=0, y=160)
                lbl = Label(showdataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=160)

    def Add_data(self):
        if self.contact_var.get() == "" or self.meal_var.get() == "":
            messagebox.showerror("Error", "All Field are Required", paren=self.root)
        else:
           self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                               database="customer")
           self.my_cursor = self.conn.cursor()
           self.my_cursor.execute("insert into roombooking values(%s,%s,%s,%s,%s,%s,%s)",(
                                                            self.contact_var.get(),
                                                            self.check_in_date_var.get(),
                                                            self.check_out_date_var.get(),
                                                            self.room_type_var.get(),
                                                            self.available_room_var.get(),
                                                            self.meal_var.get(),
                                                            self.no_of_days_var.get(),
                                                            ))
           self.conn.commit()
           self.Fetch_detail()
        self.conn.close()
        messagebox.showinfo("Success", "Room Detail Added Successfully", parent=self.root)

   # Fetch data of roombooking table
    def Fetch_detail(self):
        self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                            database="customer")
        self.my_cursor = self.conn.cursor()

        self.my_cursor.execute("select * from roombooking")
        row=self.my_cursor.fetchall()
        if len(row)!=0:
            self.Roombooking_detail_Table.delete(*self.Roombooking_detail_Table.get_children())
            for i in row:
                self.Roombooking_detail_Table.insert("", END, values=i)
            self.conn.commit()
        self.conn.close()

    def Get_detail(self, event=""):
        cursor_row = self.Roombooking_detail_Table.focus()
        content = self.Roombooking_detail_Table.item(cursor_row)
        row = content["values"]
        self.contact_var.set(row[0]),
        self.check_in_date_var.set(row[1]),
        self.check_out_date_var.set(row[2]),
        self.room_type_var.set(row[3]),
        self.available_room_var.set(row[4]),
        self.meal_var.set(row[5]),
        self.no_of_days_var.set(row[6]),

    def Update_data(self):
        if self.contact_var.get=="" or self.meal_var.get()=="":
            messagebox.showerror("Error","Please Enter Contact Number", parent=self.root)
        else:
            self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                                database="customer")
            self.my_cursor = self.conn.cursor()
            self.my_cursor.execute("update roombooking set Check_In_Date=%s,Check_Out_Date=%s, Room_Type=%s,"
                                   "Available_Room=%s,Meal=%s,No_Of_Days=%s where Contact=%s",(
                                                                                 self.check_in_date_var.get(),
                                                                                 self.check_out_date_var.get(),
                                                                                 self.room_type_var.get(),
                                                                                 self.available_room_var.get(),
                                                                                 self.meal_var.get(),
                                                                                 self.no_of_days_var.get(),
                                                                                 self.contact_var.get(),
                                                                                 ))
            self.conn.commit()
            self.Fetch_detail()
            self.conn.close()
            messagebox.showinfo("Success","Room Detail Has Been Updated Successfully", parent=self.root)

    def Delete_detail(self):
        mdelete = messagebox.askyesno("Hotel Management System","Do you want Delete this customer", parent=self.root)
        if mdelete > 0:
            self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                                database="customer")
            self.my_cursor = self.conn.cursor()
            query = "delete from roombooking where Contact=%s"
            value = (self.contact_var.get(),)
            self.my_cursor.execute(query, value)
        else:
            if not mdelete:
                return
        self.conn.commit()
        self.Fetch_detail()
        self.conn.close()

    def Reset_data(self):
        self.contact_var.set(""),
        self.check_in_date_var.set(""),
        self.check_out_date_var.set(""),
        self.room_type_var.set("")
        self.available_room_var.set(""),
        self.meal_var.set(""),
        self.no_of_days_var.set(""),
        self.paid_tax_var.set(""),
        self.sub_total_var.set(""),
        self.total_cost_var.set(""),

    def Total_Cost(self):
        indate = self.check_in_date_var.get()
        outdate = self.check_out_date_var.get()
        indate = datetime.strptime(indate, "%Y/%m/%d")
        outdate = datetime.strptime(outdate, "%Y/%m/%d")

        self.no_of_days_var.set(abs(outdate-indate).days)

        if (self.meal_var.get()=="Break Fast" and self.room_type_var.get()=="Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.no_of_days_var.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f"%((q5)*0.1))
            ST = "Rs."+str("%.2f"%((q5)))
            TT= "Rs."+str("%.2f"%(q5+((q5)*0.1)))
            self.paid_tax_var.set(Tax)
            self.sub_total_var.set(ST)
            self.total_cost_var.set(TT)
        elif (self.meal_var.get()=="Lunch" and self.room_type_var.get()=="Double"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.no_of_days_var.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f"%((q5)*0.9))
            ST = "Rs."+str("%.2f"%((q5)))
            TT= "Rs."+str("%.2f"%(q5+((q5)*0.9)))
            self.paid_tax_var.set(Tax)
            self.sub_total_var.set(ST)
            self.total_cost_var.set(TT)

        elif (self.meal_var.get()=="dinner" and self.room_type_var.get()=="Laxay"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.no_of_days_var.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f"%((q5)*0.12))
            ST = "Rs."+str("%.2f"%((q5)))
            TT= "Rs."+str("%.2f"%(q5+((q5)*0.12)))
            self.paid_tax_var.set(Tax)
            self.sub_total_var.set(ST)
            self.total_cost_var.set(TT)

        elif (self.meal_var.get()=="dinner" and self.room_type_var.get()=="Tripal"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.no_of_days_var.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs."+str("%.2f"%((q5)*0.15))
            ST = "Rs."+str("%.2f"%((q5)))
            TT= "Rs."+str("%.2f"%(q5+((q5)*0.15)))
            self.paid_tax_var.set(Tax)
            self.sub_total_var.set(ST)
            self.total_cost_var.set(TT)


    # create function search system
    def Search_detail(self):
        self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                            database="customer")
        self.my_cursor = self.conn.cursor()
        query="select * from roombooking where Contact=%s AND Meal=%s"
        value=(self.contact_var.get(),self.meal_var.get(),)
        self.my_cursor=self.conn.cursor()
        self.my_cursor.execute(query, value)
        row=self.my_cursor.fetchall()
        total_row = self.my_cursor.rowcount
        if len(row) != 0:
            self.Roombooking_detail_Table.delete(*self.Roombooking_detail_Table.get_children())
            for i in row:
                self.Roombooking_detail_Table.insert("", END, values=i)
                self.conn.commit()
                print(total_row)
            self.conn.close()

if __name__=="__main__":
    root = Tk()
    room_obj = Room_windows(root)
    root.mainloop()
