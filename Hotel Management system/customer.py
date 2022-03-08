from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
import mysql.connector
import random
class Cust_windows:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1100x480+185+180")

    # Create Connection
        self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307",user="root", database="customer")
        self.my_cursor=self.conn.cursor()
    #  ************************************ Variables ************************
        self.Ref_var = StringVar()
        x = random.randint(1000, 10000)
        self.Ref_var.set(x)

        self.Cust_name_var = StringVar()
        self.Mother_name_var = StringVar()
        self.Gender_var = StringVar()
        self.Postcode_var = StringVar()
        self.Mobile_no_var = StringVar()
        self.Email_var = StringVar()
        self.Nationality_var = StringVar()
        self.Id_type_var = StringVar()
        self.Id_no_var = StringVar()
        self.Address_var = StringVar()


        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 15, "bold"),bg="black",fg="gold")
        lbl_title.place(x=0, y=0, width=1100, height=50)

       # ********************************* Logo Image *****************************
        img1 = Image.open(r"C:\Users\akshay\Desktop\python projects\hotellogoincustomerwindow.png")
        img1.resize((100, 50), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        lblimg1.place(x=3, y=0, width=100, height=50)

        # ******************************* Label Frame *****************
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman",12,"bold"))
        labelframeleft.place(x=3, y=50, width=390, height=420)

        # ************************************ Labels and entries inside Label Frame **************
    # Customer Refrence
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(labelframeleft, textvariable=self.Ref_var, width=25, font=("arial", 13, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1)

    # Customer Name
        lbl_cust_name = Label(labelframeleft, text="Customer Name", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_cust_name.grid(row=1, column=0, sticky=W)
        entry_name = ttk.Entry(labelframeleft, textvariable=self.Cust_name_var, width=25, font=("arial", 13, "bold"))
        entry_name.grid(row=1, column=1)

    #Mother Name
        lbl_mot_name = Label(labelframeleft, text="Mother Name", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_mot_name.grid(row=2, column=0, sticky=W)
        entry_mot_name = ttk.Entry(labelframeleft, textvariable=self.Mother_name_var, width=25, font=("arial", 13, "bold"))
        entry_mot_name.grid(row=2, column=1)

    # Gender
        lbl_natinality = Label(labelframeleft, text="Gender", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_natinality.grid(row=3, column=0, sticky=W)
    # gender combobox
        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.Gender_var, font=("arial", 12, "bold"), width=23, state="readonly")
        combo_gender['value'] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)


    # Post Code
        lbl_post_code = Label(labelframeleft, text="PostCode", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_post_code.grid(row=4, column=0, sticky=W)
        entry_post_code = ttk.Entry(labelframeleft, textvariable=self.Postcode_var, width=25, font=("arial", 13, "bold"))
        entry_post_code.grid(row=4, column=1)

    # Mobile Number
        lbl_mob_num = Label(labelframeleft, text="Mobile Number", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_mob_num.grid(row=5, column=0, sticky=W)
        entry_mob_num = ttk.Entry(labelframeleft, textvariable=self.Mobile_no_var, width=25, font=("arial", 13, "bold"))
        entry_mob_num.grid(row=5, column=1)

    # Email
        lbl_email = Label(labelframeleft, text="Email", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_email.grid(row=6, column=0, sticky=W)
        entry_email = ttk.Entry(labelframeleft, textvariable=self.Email_var,width=25, font=("arial", 13, "bold"))
        entry_email.grid(row=6, column=1)

    # Nationality
        lbl_natinality = Label(labelframeleft, text="Nationality", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_natinality.grid(row=7, column=0, sticky=W)
    # Combobox nationality
        combo_nationality = ttk.Combobox(labelframeleft, textvariable=self.Nationality_var, font=("arial", 12, "bold"), width=23, state="readonly")
        combo_nationality['value'] = ("Indian", "American", "French", "British")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

    # Idproof type combobox
        lbl_idproof = Label(labelframeleft, text="Id Proof Type", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_idproof.grid(row=8, column=0, sticky=W)
    # idprooftype  combobox
        combo_idproof = ttk.Combobox(labelframeleft, textvariable=self.Id_type_var, font=("arial", 12, "bold"), width=23, state="readonly")
        combo_idproof['value'] = ("Aadhar Card", "Pan Card", "Voter Id", "Driving License")
        combo_idproof.current(0)
        combo_idproof.grid(row=8, column=1)


    # Id Number
        lbl_id_no = Label(labelframeleft, text="Id No", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_id_no.grid(row=9, column=0, sticky=W)
        entry_id_no = ttk.Entry(labelframeleft, textvariable=self.Id_no_var, width=25, font=("arial", 13, "bold"))
        entry_id_no.grid(row=9, column=1)

    # Address
        lbl_address = Label(labelframeleft, text="Address", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_address.grid(row=10, column=0, sticky=W)
        entry_address = ttk.Entry(labelframeleft, textvariable=self.Address_var, width=25, font=("arial", 13, "bold"))
        entry_address.grid(row=10, column=1)

    # ********************************** Button Frame ***************************
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=350, width=380, height=40)

    # ******************** Create button inside Button Frame ****************
        btn_add = Button(btn_frame, command=self.Add_data, text="Add", font=("arial", 13, "bold"), bg="black", fg="gold", width=8, bd=4)
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, command=self.Update_data, text="Update", font=("arial", 13, "bold"), bg="black", fg="gold", width=8, bd=4)
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, command=self.mdelete, text="Delete", font=("arial", 13, "bold"), bg="black", fg="gold", width=8, bd=4)
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame, command=self.Reset_data, text="Reset", font=("arial", 13, "bold"), bg="black", fg="gold", width=8, bd=4)
        btn_reset.grid(row=0, column=3, padx=1)

    # *************************** Table Frame *********************************
        lbl_tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Detail And Search System", font=("arial", 13, "bold"))
        lbl_tableframe.place(x=400, y=50, width=690, height=420)

    # Label Search By
        lbl_searchby = Label(lbl_tableframe, relief=RIDGE, text="Search By", fg="gold", bg="red", font=("arial", 13, "bold"))
        lbl_searchby.grid(row=0, column=0, padx=2, sticky=W)

    #    variable
        self.search_var = StringVar()
        combosearch = ttk.Combobox(lbl_tableframe, textvariable=self.search_var, font=("arial", 12, "bold"), width=15, state="readonly")
        combosearch['value'] = ("Mobile_No","Ref_No")
        combosearch.current(0)
        combosearch.grid(row=0, column=1, padx=2)

    # variable
        self.txt_search_var = StringVar()
        entry_search = Entry(lbl_tableframe, textvariable=self.txt_search_var,  font=("arial", 14, "bold"), width=20)
        entry_search.grid(row=0, column=2)

        btn_search = Button(lbl_tableframe, command=self.Search, text="Search", bd=4, bg="black", fg="gold", font=("arial", 12, "bold"), width=8)
        btn_search.grid(row=0, column=3, padx=4, sticky=W)

        btn_showall = Button(lbl_tableframe, command=self.Fetch_data, text="Show All", bd=4, bg="black", fg="gold",  font=("arial", 12, "bold"), width=8)
        btn_showall.grid(row=0, column=4)

    # ********************************* Show Data  Table ***************************

        detailtable=Frame(lbl_tableframe, bd=2, relief=RIDGE)
        detailtable.place(x=3, y=50, width=680, height=340)

        scroll_x = ttk.Scrollbar(detailtable, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(detailtable, orient=VERTICAL)

        self.Cust_detail_Table = ttk.Treeview(detailtable, columns=("Ref No","Customer Name","Mother Name", "Gender","Post Code",
                                             "Mobile No","Email","Nationality","Id Proof Type","Id No","Address"),
                                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_detail_Table.xview)
        scroll_y.config(command=self.Cust_detail_Table.yview)

        self.Cust_detail_Table.heading('Ref No', text="Refrence No")
        self.Cust_detail_Table.heading('Customer Name', text="Customer Name")
        self.Cust_detail_Table.heading('Mother Name', text="Mother Name" )
        self.Cust_detail_Table.heading('Gender', text="Gender")
        self.Cust_detail_Table.heading('Post Code', text="Post Code")
        self.Cust_detail_Table.heading('Mobile No', text="Mobile No")
        self.Cust_detail_Table.heading('Email', text="Email")
        self.Cust_detail_Table.heading('Nationality', text="Nationality")
        self.Cust_detail_Table.heading('Id Proof Type', text="Id Proof Type")
        self.Cust_detail_Table.heading('Id No', text="Id No")
        self.Cust_detail_Table.heading('Address', text="Address")

        self.Cust_detail_Table["show"] = "headings"

        self.Cust_detail_Table.column('Ref No', width=100)
        self.Cust_detail_Table.column('Customer Name', width=100)
        self.Cust_detail_Table.column('Mother Name', width=100)
        self.Cust_detail_Table.column('Gender', width=100)
        self.Cust_detail_Table.column('Post Code', width=100)
        self.Cust_detail_Table.column('Mobile No', width=100)
        self.Cust_detail_Table.column('Email', width=100)
        self.Cust_detail_Table.column('Nationality', width=100)
        self.Cust_detail_Table.column('Id Proof Type', width=100)
        self.Cust_detail_Table.column('Id No', width=100)
        self.Cust_detail_Table.column('Address', width=100)


        self.Cust_detail_Table.pack(fill=BOTH, expand=1)
        self.Fetch_data()
        self.Cust_detail_Table.bind("<ButtonRelease-1>", self.Get_cursor)

    # Insert data to the customer database
    def Add_data(self):
        if self.Mobile_no_var.get()=="" or self.Mother_name_var.get()=="":
            messagebox.showerror("Error","All Field Are Compulsory", parent=self.root)
        else:
            try:
                self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                                    database="customer")
                self.my_cursor = self.conn.cursor()
                self.my_cursor.execute("insert into customer_table values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                    self.Ref_var.get(),
                                                                    self.Cust_name_var.get(),
                                                                    self.Mother_name_var.get(),
                                                                    self.Gender_var.get(),
                                                                    self.Postcode_var.get(),
                                                                    self.Mobile_no_var.get(),
                                                                    self.Email_var.get(),
                                                                    self.Nationality_var.get(),
                                                                    self.Id_type_var.get(),
                                                                    self.Id_no_var.get(),
                                                                    self.Address_var.get(),
                                                                     ))
                self.conn.commit()
                self.Fetch_data()
                self.conn.close()
                messagebox.showinfo("Success","Customer Has Been Added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something Went wrong:{str(es)}", parent=self.root)

    def Fetch_data(self):

        self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                            database="customer")
        self.my_cursor = self.conn.cursor()
        self.my_cursor.execute("select * from customer_table")
        rows = self.my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_detail_Table.delete(*self.Cust_detail_Table.get_children())
            for i in rows:
                self.Cust_detail_Table.insert("", END, values=i)
        self.conn.commit()
        self.conn.close()

    def Get_cursor(self, event=""):
        cursor_row = self.Cust_detail_Table.focus()
        content = self.Cust_detail_Table.item(cursor_row)
        row = content["values"]

        self.Ref_var.set(row[0]),
        self.Cust_name_var.set(row[1]),
        self.Mother_name_var.set(row[2]),
        self.Gender_var.set(row[3]),
        self.Postcode_var.set(row[4]),
        self.Mobile_no_var.set(row[5]),
        self.Email_var.set(row[6]),
        self.Nationality_var.set(row[7]),
        self.Id_type_var.set(row[8]),
        self.Id_no_var.set(row[9]),
        self.Address_var.set(row[10]),

    def Update_data(self):
        if self.Mobile_no_var.get=="" or self.Postcode_var.get()=="":
            messagebox.showerror("Error","Please Enter Mobile Number", parent=self.root)
        else:
            self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                                database="customer")
            self.my_cursor = self.conn.cursor()
            self.my_cursor.execute("update customer_table set Customer_Name=%s, Mother_Name=%s, Gender=%s,"
                                   "Post_Code=%s, Mobile_No=%s,Email=%s, Nationality=%s,Id_Type=%s, Id_Proof=%s"
                                   ",Address=%s where Ref_No=%s ",(
                                                                                 self.Cust_name_var.get(),
                                                                                 self.Mother_name_var.get(),
                                                                                 self.Gender_var.get(),
                                                                                 self.Postcode_var.get(),
                                                                                 self.Mobile_no_var.get(),
                                                                                 self.Email_var.get(),
                                                                                 self.Nationality_var.get(),
                                                                                 self.Id_type_var.get(),
                                                                                 self.Id_no_var.get(),
                                                                                 self.Address_var.get(),
                                                                                 self.Ref_var.get(),

                                                                                 ))
            self.conn.commit()
            self.Fetch_data()
            self.conn.close()
            messagebox.showinfo("Success","Customer Detail Has Been Updated Successfully", parent=self.root)

    def mdelete(self):
        mdelete=messagebox.askyesno("Hotel Management System","Do you want Delete this customer", parent=self.root)
        if mdelete>0:
            self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                                database="customer")
            self.my_cursor = self.conn.cursor()
            query="delete from customer_table where Ref_No=%s"
            value=(self.Ref_var.get(),)
            self.my_cursor.execute(query, value)
        else:
            if not mdelete:
                return
        self.conn.commit()
        self.Fetch_data()
        self.conn.close()

    def Reset_data(self):
        #self.Ref_var.set(""),
        self.Cust_name_var.set(""),
        self.Mother_name_var.set(""),
       # self.Gender_var.set(""),
        self.Postcode_var.set("")
        self.Mobile_no_var.set(""),
        self.Email_var.set(""),
        #self.Nationality_var.set(""),
        #self.Id_type_var.set(""),
        self.Id_no_var.set(""),
        self.Address_var.set(""),

    def Search(self):

        self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                            database="customer")
        self.my_cursor = self.conn.cursor()

        query="select * from customer_table where Mobile_No=%s AND Ref_No=%s"
        value=(self.Mobile_no_var.get(),self.Ref_var.get(),)
        self.my_cursor=self.conn.cursor()
        self.my_cursor.execute(query, value)
        row=self.my_cursor.fetchall()
        total_row = self.my_cursor.rowcount
        if len(row)!= 0:
            self.Cust_detail_Table.delete(*self.Cust_detail_Table.get_children())
            for i in row:
                self.Cust_detail_Table.insert("", END, values=i)
            self.conn.commit()
            print(total_row)
        self.conn.close()





if __name__ == "__main__":
    root = Tk()
    obj = Cust_windows(root)
    root.mainloop()