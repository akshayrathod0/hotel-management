from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import random
class Details_windows:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1150x450+125+180")

        self.floor_var = StringVar()
        self.room_no_var = StringVar()
        self.room_type_var = StringVar()

        # Create Connection
        self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                            database="customer")
        self.my_cursor = self.conn.cursor()

        lbl_title = Label(self.root, text="ROOM BOOKING DETAIL DETAILS", font=("times new roman", 15, "bold"), bg="black",
                          fg="gold")
        lbl_title.place(x=0, y=0, width=1150, height=50)

        # ********************************* Logo Image *****************************
        img1 = Image.open(r"C:\Users\akshay\Desktop\python projects\hotellogoincustomerwindow.png")
        img1.resize((100, 50), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image=self.photoimg1, bd=0, relief=RIDGE)
        lblimg1.place(x=3, y=0, width=100, height=50)


        # ******************************* Label Frame *****************
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", font=("times new roman",12,"bold"))
        labelframeleft.place(x=3, y=50, width=470, height=300)


        # ************************************ Labels and entries inside Label Frame **************

        # Floor
        lbl_floor = Label(labelframeleft, text="Floor:", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_floor.grid(row=0, column=0, sticky=W)
        entry_floor = ttk.Entry(labelframeleft,textvariable=self.floor_var, width=18, font=("arial", 13, "bold"),)
        entry_floor.grid(row=0, column=1, sticky=W)

        # Room No
        lbl_room_no = Label(labelframeleft, text="Room No:", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_room_no.grid(row=1, column=0, sticky=W)
        entry_room_no = ttk.Entry(labelframeleft,textvariable=self.room_no_var, width=18, font=("arial", 13, "bold"),)
        entry_room_no.grid(row=1, column=1, sticky=W)

        # Room Type
        lbl_room_type = Label(labelframeleft, text="Room Type:", font=("arial", 12, "bold"), padx=2, pady=4)
        lbl_room_type.grid(row=2, column=0, sticky=W)
        entry_room_type = ttk.Entry(labelframeleft,textvariable=self.room_type_var, width=18, font=("arial", 13, "bold"),)
        entry_room_type.grid(row=2, column=1, sticky=W)


        # ********************************** Button Frame ***************************
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=180, width=380, height=40)

        # ******************** Create button inside Button Frame ****************
        btn_add = Button(btn_frame, command=self.Add_details, text="Add", font=("arial", 14, "bold"), bg="black",
                         fg="gold", width=7)
        btn_add.grid(row=0, column=0, padx=1)

        btn_update = Button(btn_frame, command=self.Update_details, text="Update", font=("arial", 14, "bold"), bg="black",
                            fg="gold", width=7)
        btn_update.grid(row=0, column=1, padx=1)

        btn_delete = Button(btn_frame, command=self.Delete_detail, text="Delete", font=("arial", 14, "bold"), bg="black",
                            fg="gold", width=7)
        btn_delete.grid(row=0, column=2, padx=1)

        btn_reset = Button(btn_frame,command=self.Reset_data, text="Reset", font=("arial", 14, "bold"), bg="black",
                           fg="gold", width=7)
        btn_reset.grid(row=0, column=3, padx=1)

    # ******************************* Label Frame Right *****************
        tableframe = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add",
                                font=("times new roman", 12, "bold"))
        tableframe.place(x=500, y=50, width=470, height=300)

    # Create scroll bar
        scroll_x = ttk.Scrollbar(tableframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableframe, orient=VERTICAL)
        self.Detail_table = ttk.Treeview(tableframe, columns=("floor", "room_no", "room_type"),
                                        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Detail_table.xview)
        scroll_y.config(command=self.Detail_table.yview)

        self.Detail_table.heading("floor", text="Floor")
        self.Detail_table.heading('room_no', text="Room No")
        self.Detail_table.heading('room_type', text="Room Type" )

        self.Detail_table['show'] = "headings"

        self.Detail_table.column("floor", width=100)
        self.Detail_table.column("room_no", width=100)
        self.Detail_table.column("room_type", width=100)

        self.Detail_table.pack(fill=BOTH, expand=1)
        self.Fetch_details()
        self.Detail_table.bind("<ButtonRelease-1>", self.Get_details)

    def Add_details(self):
        if self.room_no_var.get() == "":
            messagebox.showerror("Error", "All fields are Required", parent=self.root)
        else:
            self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                                database="customer")
            self.my_cursor = self.conn.cursor()

            query = "insert into details values(%s,%s,%s)"
            value = (self.floor_var.get(), self.room_no_var.get(), self.room_type_var.get(),)
            self.my_cursor.execute(query, value)
            self.conn.commit()
            self.Fetch_details()
        self.conn.close()
        messagebox.showinfo("Success", "Room Details Added", parent=self.root)

    def Fetch_details(self):
        self.my_cursor.execute("select * from details")
        row=self.my_cursor.fetchall()
        if len(row)!=0:
            self.Detail_table.delete(*self.Detail_table.get_children())
            for i in row:
                self.Detail_table.insert("", END, values=i)
            self.conn.commit()
        self.conn.close()

    def Get_details(self, event=""):
        cursor = self.Detail_table.focus()
        content = self.Detail_table.item(cursor)
        row = content["values"]
        self.floor_var.set(row[0]),
        self.room_no_var.set(row[1]),
        self.room_type_var.set(row[2]),

    def Update_details(self):
        if self.room_no_var.get == "":
            messagebox.showerror("Error", "Please Enter Room Number", parent=self.root)
        else:
            self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                                database="customer")
            self.my_cursor = self.conn.cursor()
            self.my_cursor.execute("update details set Floor=%s, Room_Type=%s where Room_No=%s",(
                                                                                 self.floor_var.get(),
                                                                                 self.room_type_var.get(),
                                                                                 self.room_no_var.get(),

                                                                                 ))
            self.conn.commit()
            self.Fetch_details()
            self.conn.close()
            messagebox.showinfo("Success","Detail Has Been Updated", parent=self.root)

    def Delete_detail(self):
        mdelete = messagebox.askyesno("Hotel Management System","Do you want Delete this customer", parent=self.root)
        if mdelete > 0:
            self.conn = mysql.connector.connect(host="localhost", port="3307", password="3307", user="root",
                                                database="customer")
            self.my_cursor = self.conn.cursor()
            query = "delete from details where Room_No=%s"
            value = (self.room_no_var.get(),)
            self.my_cursor.execute(query, value)
        else:
            if not mdelete:
                return
        self.conn.commit()
        self.Fetch_details()
        self.conn.close()

    def Reset_data(self):
        self.floor_var.set(""),
        self.room_no_var.set(""),
        self.room_type_var.set(""),

if __name__=="__main__":
    root=Tk()
    detailpbj=Details_windows(root)
    root.mainloop()