from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import random
class Register_windows:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1280x800+0+0")

    # variables
        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.contno_var = StringVar()
        self.email_var = StringVar()
        self.selectsecurityq_var = StringVar()
        self.securityans_var = StringVar()
        self.password_var = StringVar()
        self.confpass_var = StringVar()
        self.check_var = IntVar()
    # ********************************* Background Image *****************************
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\akshay\Desktop\python projects\background image1.jpg")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

    # ********************************* Left side image Image *****************************
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\akshay\Desktop\python projects\leftsideinhotel1.jpg")

        lbl_bg1 = Label(self.root, image=self.bg)
        lbl_bg1.place(x=50, y=80, width=700, height=550)

    # ************************* main frame *************************

        frame = Frame(self.root, bg="white")
        frame.place(x=500, y=80, width=700, height=550)

        register = Label(frame, text="REGISTER HERE", font=("times new roman",20,"bold"),bg="white",fg="darkgreen" )
        register.place(x=20,y=20)

    # *********************** Labels and Entries ************************************
        fname = Label(frame, text="First Name", font=("times new roman",15,"bold"),bg="white", fg="black")
        fname.place(x=50, y=100)
        self.fname_entry = ttk.Entry(frame, textvariable=self.fname_var,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        lname_lbl = Label(frame, text="Last Name", font=("times new roman",15,"bold"),bg="white", fg="black")
        lname_lbl.place(x=350, y=100)
        self.lname_entry = ttk.Entry(frame,  textvariable=self.lname_var,font=("times new roman",15,"bold"))
        self.lname_entry.place(x=350, y=130, width=250)

        contno_lbl = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contno_lbl.place(x=50, y=180)
        self.contno_entry = ttk.Entry(frame,  textvariable=self.contno_var, font=("times new roman", 15, "bold"))
        self.contno_entry.place(x=50, y=210, width=250)

        email_lbl = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email_lbl.place(x=350, y=180)
        self.email_entry = ttk.Entry(frame,  textvariable=self.email_var, font=("times new roman", 15, "bold"))
        self.email_entry.place(x=350, y=210, width=250)

        securityques_lbl = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
        securityques_lbl.place(x=50, y=260)

        self.securityques_combo = ttk.Combobox(frame,  textvariable=self.selectsecurityq_var, font=("times new roman", 15, "bold"), state="readonly")
        self.securityques_combo["values"]=("Select","Your Birth Place","Your Girlfriend Name", "Your Pet Name")
        self.securityques_combo.place(x=50, y=290)
        self.securityques_combo.current(0)

        securityans_lbl = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        securityans_lbl.place(x=350, y=260)
        self.securityans_entry = ttk.Entry(frame,  textvariable=self.securityans_var, font=("times new roman", 15, "bold"))
        self.securityans_entry.place(x=350, y=290, width=250)


        password_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        password_lbl.place(x=50, y=340)
        self.password_entry = ttk.Entry(frame,  textvariable=self.password_var, font=("times new roman", 15, "bold"))
        self.password_entry.place(x=50, y=370, width=250)

        confpassword_lbl = Label(frame, text="Conform Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confpassword_lbl.place(x=350, y=340)
        self.confpassword_entry = ttk.Entry(frame,  textvariable=self.confpass_var, font=("times new roman", 15, "bold"))
        self.confpassword_entry.place(x=350, y=370, width=250)
    # **************************** Check Button *******************************
        check_btn = Checkbutton(frame, variable=self.check_var, text="I Agree The Terms & Conditions", font=("times new roman", 12, "bold")
                                , onvalue=1, offvalue=0)
        check_btn.place(x=50, y=420)

    # image for create register and login button
        img1 = Image.open(r"C:\Users\akshay\Desktop\python projects\register button.jpg")
        img1.resize((200, 50), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_btn1 = Button(self.root, command=self.register_user, image=self.photoimg1, bd=0, relief=RIDGE)
        lbl_btn1.place(x=530, y=550, width=200, height=50)

        img2 = Image.open(r"C:\Users\akshay\Desktop\python projects\login button.jpg")
        img2.resize((200, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_btn2 = Button(self.root, command=self.login_destroy, image=self.photoimg2, bd=0, relief=RIDGE)
        lbl_btn2.place(x=850, y=550, width=200, height=50)


    # function on register button

    def register_user(self):
        if self.fname_var.get()=='' or self.lname_var.get()=='' or self.selectsecurityq_var.get()=='Select':
            messagebox.showerror('Error','All Fields are Required',parent=self.root)
        elif self.password_var.get()!=self.confpass_var.get():
            messagebox.showerror('Error','Password & conform Password not match', parent=self.root)
        elif self.check_var.get()==0:
            messagebox.showinfo("Error", "Please Accept Tearms and Condition",parent=self.root)
        else:
            self.conn = mysql.connector.connect(host="localhost",user="root",port="3307",password="3307",database="customer")
            self.my_cursor=self.conn.cursor()
            self.my_cursor.execute("select * from register where email=%s",(
                                                                    self.email_var.get(),
                                                                      ))
            row = self.my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error", "User already exist , Please try another email", parent=self.root)
            else:
                query = "insert into register values(%s,%s,%s,%s,%s,%s,%s)"
                value = (self.fname_var.get(),
                         self.lname_var.get(),
                         self.contno_var.get(),
                         self.email_var.get(),
                         self.selectsecurityq_var.get(),
                         self.securityans_var.get(),
                         self.password_var.get(),)
                self.my_cursor.execute(query, value)
                self.conn.commit()
                self.conn.close()
                messagebox.showinfo("Success", "Register Successfully", parent=self.root)

    # function on login button

    def login_destroy(self):
        self.root.destroy()




if __name__=="__main__":
    root = Tk()
    registerobj = Register_windows(root)
    root.mainloop()
