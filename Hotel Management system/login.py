from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import random
from hotel import HotelManagementSystem
from register import Register_windows
from customer import Cust_windows
from room import Room_windows
from details import Details_windows
def main():
    root = Tk()
    app = Login_windows(root)
    root.mainloop()

class Login_windows:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1280x800+0+0")

    #variable

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
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\akshay\Desktop\python projects\background image2.jpg")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # **************** Create frame for login window *****************************
        frame = Frame(self.root, bg="black")
        frame.place(x=450, y=120, width=350, height=450)

        # ********************************* Logo Image *****************************
        img1 = Image.open(r"C:\Users\akshay\Desktop\python projects\user.png")
        img1.resize((100, 80), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1 = Label(self.root, image=self.photoimg1, borderwidth=0, bg="black",relief=RIDGE)
        lblimg1.place(x=570, y=140, width=100, height=80)

        get_str=Label(frame, text="Get Started", font=("times new roman",20,"bold"), fg="white", bg="black")
        get_str.place(x=100, y=140)

        # Label
        lbl_username=Label(frame, text="Username",font=("times new roman",15,"bold"),bg="black", fg="white",pady=6)
        lbl_username.place(x=100, y=180)

        self.entry_username = ttk.Entry(frame, font=("times new roman",15,"bold"),width=25)
        self.entry_username.place(x=40, y=215)

        # Label
        lbl_password=Label(frame, text="Password",font=("times new roman",15,"bold"),bg="black", fg="white",pady=6)
        lbl_password.place(x=100, y=258)

        self.entry_password = ttk.Entry(frame, font=("times new roman",15,"bold"),width=25)
        self.entry_password.place(x=40, y=291)


        img2=Image.open(r"C:\Users\akshay\Desktop\python projects\usernamelogo.png")
        img2.resize((40,40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(image=self.photoimg2, borderwidth=0, bg="black",relief=RIDGE)
        lblimg2.place(x=500, y=290, width=40, height=40)


        img3=Image.open(r"C:\Users\akshay\Desktop\python projects\password logo.png")
        img3.resize((40,40), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(image=self.photoimg3, borderwidth=0, bg="black",relief=RIDGE)
        lblimg3.place(x=500, y=367, width=40, height=40)

    # Login Button
        btn_login=Button(frame,command=self.login, text="Login", font=("times new roman", 15, "bold"), activeforeground="white", activebackground="red", bd=3, relief=RIDGE, bg="red", fg="white")
        btn_login.place(x=100, y=330, width=100, height=35)

    # Register button
        btn_login=Button(frame,command=self.Register_windows, text="New User Register", font=("times new roman", 10, "bold"), activeforeground="white",borderwidth=0,  activebackground="black", relief=RIDGE, bg="black", fg="white")
        btn_login.place(x=20, y=370, width=170)

    # Forgot Pasword
        btn_login=Button(frame, command=self.forgot_password, text="Forgot Password", font=("times new roman", 10, "bold"), activeforeground="white", borderwidth=0, activebackground="black", relief=RIDGE, bg="black", fg="white")
        btn_login.place(x=20, y=390, width=160)

    def Register_windows(self):
        self.new_window = Toplevel(self.root)
        self.app = Register_windows(self.new_window)

    # login function
    def login(self):
        if (self.entry_username.get()=="" or self.entry_password.get()==""):
            messagebox.showerror("Error", "All Fields Required",parent=self.root)
        else:
            self.conn = mysql.connector.connect(host="localhost",user="root",port="3307",password="3307",database="customer")
            self.my_cursor=self.conn.cursor()
            self.my_cursor.execute("select * from register where Email=%s and Passwd=%s",(
                                                                                   self.entry_username.get(),
                                                                                   self.entry_password.get(),
                                                                                        ))
            row = self.my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Invalid Username and Passwd", parent=self.root)
            else:
                open_main = messagebox.askyesno("YesNo", "Access Only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            self.conn.commit()
            self.conn.close()


    # new user registration function

    def register_user(self):
        if self.fname_var.get()=='' or self.lname_var.get()=='' or self.selectsecurityq_var.get()=='Select':
            messagebox.showerror('Error','All Fields are Required',parent=self.root2)
        elif self.password_var.get()!=self.confpass_var.get():
            messagebox.showerror('Error','Password & conform Password not match',parent=self.root2)
        elif self.check_var.get()==0:
            messagebox.showinfo("Error", "Please Accept Tearms and Condition",parent=self.root2)
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
                messagebox.showinfo("Success", "Register Successfully", parent=self.root2)
                self.root2.destroy()

    # ******************** Reset password **************************
    def reset_password(self):
        if self.securityques_combo.get() == "Select":
            messagebox.showerror("Error", "Select Security question", parent=self.root2)
        elif self.securityans_entry.get() == "":
            messagebox.showerror("Error", "Please Enter The Answer", parent=self.root2)
        elif self.new_password_entry.get() == "":
            messagebox.showerror("Error", "Please Enter The New Password", parent=self.root2)
        else:
            self.conn = mysql.connector.connect(host="localhost", user="root", port="3307", password="3307",
                                                database="customer")
            self.my_cursor = self.conn.cursor()
            query = "select * from register where Email=%s and SecurityQ=%s and SecuriyA=%s"
            value = (self.entry_username.get(),
                     self.securityques_combo.get(),
                     self.securityans_entry.get(),)
            self.my_cursor.execute(query, value)
            row = self.my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter the Correct answer",parent=self.root2)
            else:
                query="update register set Passwd=%s where Email=%s"
                value=(self.new_password_entry.get(),self.entry_username.get())
                self.my_cursor.execute(query, value)

                self.conn.commit()
                self.conn.close()
                messagebox.showinfo("Success", "Your Password has been Change, Please login with new password", parent=self.root2)
                self.root2.destroy()

    # ************************** Forgot password windows *********************

    def forgot_password(self):
        if self.entry_username.get() == "":
            messagebox.showerror("Error", "Please Enter The Email Address to Reset password", parent=self.root)
        else:
            self.conn = mysql.connector.connect(host="localhost", user="root", port="3307", password="3307",
                                                database="customer")
            self.my_cursor = self.conn.cursor()
            query = "select * from register where Email=%s"
            value = (self.entry_username.get(),)
            self.my_cursor.execute(query, value)
            row = self.my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Please enter valid username")
            else:
                self.conn.close()
                self.root2= Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("350x450+450+120")

                lbl1=Label(self.root2, text="Forgot Password",font=("times new roman", 15, "bold"), bg="white", fg="red")
                lbl1.place(x=0, y=10, relwidth=1)

                securityques_lbl = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"),
                                          fg="black")
                securityques_lbl.place(x=50, y=60)

                self.securityques_combo = ttk.Combobox(self.root2,font=("times new roman", 15, "bold"), state="readonly")
                self.securityques_combo["values"] = ("Select", "Your Birth Place", "Your Girlfriend Name", "Your Pet Name")
                self.securityques_combo.place(x=50, y=90)
                self.securityques_combo.current(0)

                securityans_lbl = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), fg="black")
                securityans_lbl.place(x=50, y=140)
                self.securityans_entry = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.securityans_entry.place(x=50, y=170, width=250)


                new_password_lbl = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), fg="black")
                new_password_lbl.place(x=50, y=220)
                self.new_password_entry = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.new_password_entry.place(x=50, y=250, width=250)




                btn = Button(self.root2, command=self.reset_password, text="Reset", font=("times new roman", 15, "bold"),bg="green", fg="white",
                             activebackground="green", activeforeground="white")
                btn.place(x=100, y=290, width=100)


if __name__=="__main__":
    main()