from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_windows
from room import Room_windows
from details import Details_windows
class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1270x800+0+0")

        # **************** First image *************************

        img1=Image.open(r"C:\Users\akshay\Desktop\python projects\backgroundhotelupperside.jpg")
        img1.resize((1300, 110), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg1= Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=0, width=1300, height=110)

        # **************** Second image *************************

        img2 = Image.open(r"C:\Users\akshay\Desktop\python projects\hotellogo.png")
        img2.resize((185, 110), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=0, width=185, height=110)

    # ******************* Title **************************
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 30, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=110, width=1270, height=40)

    # **************************** Main Frame ***************************
        main_frame=Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=150, width=1270, height=640)

    # ******************************* Menu ***********************************
        lbl_menu = Label(main_frame, text="Menu", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=185)

     # **************************** Button Frame ***************************
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=40, width=185, height=150)

        cut_btn = Button(btn_frame, command=self.cust_detail, text="CUSTOMER     ", width=18, font=("times new roman", 13, "bold"), bd=0, bg="black", fg="gold", relief=RIDGE, cursor="hand1")
        cut_btn.grid(row=0, column=0, pady=3)

        cut_btn = Button(btn_frame, command=self.roombooking_detail, text="ROOM     ", width=18, font=("times new roman", 13, "bold"), bd=0, bg="black", fg="gold", relief=RIDGE, cursor="hand1")
        cut_btn.grid(row=1, column=0, pady=3)

        cut_btn = Button(btn_frame,command=self.details_roombooking, text="DETAIL     ", width=18, font=("times new roman", 13, "bold"), bd=0, bg="black", fg="gold", relief=RIDGE, cursor="hand1")
        cut_btn.grid(row=2, column=0, pady=3)

        cut_btn = Button(btn_frame, text="REPORT     ", width=18, font=("times new roman", 13, "bold"), bd=0, bg="black", fg="gold", relief=RIDGE, cursor="hand1")
        cut_btn.grid(row=3, column=0, pady=3)

        cut_btn = Button(btn_frame, text="LOGOUT     ", width=18, font=("times new roman", 13, "bold"), bd=0, bg="black", fg="gold", relief=RIDGE, cursor="hand1")
        cut_btn.grid(row=4, column=0, pady=3)

    # ***************************** Right Side Image *****************************
        img3 = Image.open(r"C:\Users\akshay\Desktop\python projects\backgroundhotelimage.jpg")
        img3.resize((1200, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg3.place(x=180, y=0, width=1200, height=590)

    # ******************************** Left Side Image ***************************
        img4 = Image.open(r"C:\Users\akshay\Desktop\python projects\leftsideinhotel1.jpg")
        img4.resize((185, 182), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg4 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg4.place(x=0, y=180, width=185, height=182)

        img5 = Image.open(r"C:\Users\akshay\Desktop\python projects\leftsideinhotel.jpg")
        img5.resize((185, 183), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg5 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg5.place(x=0, y=345, width=185, height=183)

    def cust_detail(self):
        self.new_windows = Toplevel(self.root)
        self.app=Cust_windows(self.new_windows)

    def roombooking_detail(self):
        self.new_windows = Toplevel(self.root)
        self.app = Room_windows(self.new_windows)

    def details_roombooking(self):
        self.new_windows = Toplevel(self.root)
        self.app = Details_windows(self.new_windows)
if __name__=="__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()


