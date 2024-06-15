import tkinter as tk
from tkinter import font as tkfont
import os
from tkinter import *
# from tkinter import messagebox
# top = Tk()

# for linking all the windows
class Main(tk.Tk):
    bgr="images.png"
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Calibri', size=20, weight="bold")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.bgr=tk.PhotoImage(file="images.png")
        self.frames = {}
        for F in (basepage,MainWindow,PMSforAdministrator,PMSforOperator,PMSforTicketor,PMSforCashier,LoginforAdministrator,RegisterforAdmintrator,AdministratorWindow,Customer,RegisterforCashier,RegisterforTicketor,RegisterforOperator,LoginforTicketor,LoginforOperator,LoginforOperator,LoginforCashier,OperatorWindow,TicketorWindow,CashierWindow):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MainWindow")
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
class basepage(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)

        label_bkgr=tk.Label(self,image=controller.bgr)
        label_bkgr.place(relx=0.5,rely=0.5,anchor=CENTER)
# main window of the library management
class MainWindow(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller) ### This Code to be copied in every Class. and bg code removed
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System")  # Title for Window
        self.controller.state('zoomed')  # Making full screen
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('italic', 60,'bold'))
        HeadingLabel1.pack()

        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)

        HeadingLabel2 = tk.Label(self, text="Welcome to the Parking System!", font=('Calibri', 30,'bold')).pack(pady=50)
        user1_Button = tk.Button(self, text='Administrator',font=('italic', 15),background='#BEBEBE',
                                command=lambda: controller.show_frame("PMSforAdministrator"),relief='raised', borderwidth=3, width=30, height=2).pack(pady=5)
        # command=lambda:LibraryManagementSystem.login()
        user2_Button = tk.Button(self, text='Operator',
                                 command=lambda: controller.show_frame("PMSforOperator"),background='#BEBEBE',font=('italic', 15),
                                 relief='raised', borderwidth=3, width=30, height=2).pack(pady=5)  # Creating a register button
        user3_Button = tk.Button(self, text='Ticketor',
                                 command=lambda: controller.show_frame("PMSforTicketor"),background='#BEBEBE',font=('italic', 15),
                                 relief='raised', borderwidth=3, width=30, height=2).pack(pady=5)
        user3_Button = tk.Button(self, text='Cashier',
                                 command=lambda: controller.show_frame("PMSforCashier"),background='#BEBEBE',font=('italic', 15),
                                 relief='raised', borderwidth=3, width=30, height=2).pack(pady=5)
        Exit_Button = tk.Button(self, text="Exit", command=controller.destroy,font = ('bold'),relief="raised", background = '#722F37',borderwidth=3, width=30,
                                height=2).pack(pady=5)
        # Empty_Space = tk.Label(self, text='', font=('Helvetica', 13), fg='white', bg='#65428C')
        # Empty_Space.pack(fill='both', expand=True) #coloring half if the screen
# window for student login and registeration fo student
class PMSforAdministrator(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('italic', 60, 'bold'))
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Administrator', font=('italic', 30, 'bold'))
        HeadingLabel2.pack(pady=80)
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)

        login_Button = tk.Button(self, text='Login', command=lambda: controller.show_frame("LoginforAdministrator"),background='#BEBEBE',font=('italic', 15),
                                 relief='raised', borderwidth=2, width=30, height=2)
        login_Button.pack(pady=10)

        Register_Button = tk.Button(self, text='Register', command=lambda: controller.show_frame("RegisterforAdmintrator"),font=('italic', 15),background='#BEBEBE', relief='raised',borderwidth=3, width=30, height=2).pack(pady=10)

        Back_Button = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainWindow"), relief="raised",font=('italic', 15), borderwidth=3, width=30,background='#BEBEBE',
                                height=2).pack(pady=10)
# main window for Employees
class PMSforOperator(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('italic', 60, 'bold'))
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Operator', font=('italic', 30, 'bold'))
        HeadingLabel2.pack(pady=80)
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        login_Button = tk.Button(self, text='Login', command=lambda: controller.show_frame("LoginforOperator"),
                                 background='#BEBEBE', font=('italic', 15),
                                 relief='raised', borderwidth=2, width=30, height=2)
        login_Button.pack(pady=10)

        Register_Button = tk.Button(self, text='Register',
                                    command=lambda: controller.show_frame("RegisterforAdmintrator"),
                                    font=('italic', 15), background='#BEBEBE', relief='raised', borderwidth=3, width=30,
                                    height=2).pack(pady=10)

        Back_Button = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainWindow"), relief="raised",
                                font=('italic', 15), borderwidth=3, width=30, background='#BEBEBE',
                                height=2).pack(pady=10)

class PMSforTicketor(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('italic', 60, 'bold'))
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Ticketor', font=('italic', 30, 'bold'))
        HeadingLabel2.pack(pady=80)
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        login_Button = tk.Button(self, text='Login', command=lambda: controller.show_frame("LoginforTicketor"),
                                 background='#BEBEBE', font=('italic', 15),
                                 relief='raised', borderwidth=2, width=30, height=2)
        login_Button.pack(pady=10)

        Register_Button = tk.Button(self, text='Register',
                                    command=lambda: controller.show_frame("RegisterforAdmintrator"),
                                    font=('italic', 15), background='#BEBEBE', relief='raised', borderwidth=3, width=30,
                                    height=2).pack(pady=10)

        Back_Button = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainWindow"), relief="raised",
                                font=('italic', 15), borderwidth=3, width=30, background='#BEBEBE',
                                height=2).pack(pady=10)

class PMSforCashier(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Library Management System")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('italic', 60, 'bold'))
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Cashier', font=('italic', 30, 'bold'))
        HeadingLabel2.pack(pady=80)
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        login_Button = tk.Button(self, text='Login', command=lambda: controller.show_frame("LoginforCashier"),
                                 background='#BEBEBE', font=('italic', 15),
                                 relief='raised', borderwidth=2, width=30, height=2)
        login_Button.pack(pady=10)

        Register_Button = tk.Button(self, text='Register',
                                    command=lambda: controller.show_frame("RegisterforCashier"),
                                    font=('italic', 15), background='#BEBEBE', relief='raised', borderwidth=3, width=30,
                                    height=2).pack(pady=10)

        Back_Button = tk.Button(self, text="Back", command=lambda: controller.show_frame("MainWindow"), relief="raised",
                                font=('italic', 15), borderwidth=3, width=30, background='#BEBEBE',
                                height=2).pack(pady=10)

class RegisterforAdmintrator(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.Name = ''
        self.ID = ''
        self.MobileNo = ''
        self.Gender = ''
        self.DOB = ''
        self.Address = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMs.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Administrator Registration", font=('italic', 40, 'bold'))
        HeadingLabel2 = tk.Label(self, text="Enter Details Below To Register!", font=('italic', 25, 'bold'),
                                 fg='#111111')
        HeadingLabel2.pack(pady=50)
        Name_verify = tk.StringVar()
        ID_verify = tk.StringVar()
        MobileNo_verify = tk.StringVar()
        Gender_verify = tk.StringVar()
        DOB_verify = tk.StringVar()
        Address_verify = tk.StringVar()
        password_verify = tk.StringVar()
        here = os.path.dirname(os.path.realpath(__file__))
        subdir = "Users"
        filepath = os.path.join(here, subdir)
        files = os.listdir()
        if subdir in files:
            pass
        else:
            os.mkdir(os.path.join(here, subdir))
        def register_Administrator():
            name = Name_verify.get()
            ID = ID_verify.get()
            MobileNo = MobileNo_verify.get()
            Gender = Gender_verify.get()
            DOB = DOB_verify.get()
            Address = Address_verify.get()
            password = password_verify.get()
            if ID == '1' or ID == '2' or ID == '3':  # Student Roll No.
                try:
                    f = open(filepath + '\\' + ID, 'a+')
                    f.write(name + "\n")
                    f.write(ID + "\n")
                    f.write(MobileNo + "\n")
                    f.write(Gender + "\n")
                    f.write(DOB + "\n")
                    f.write(Address + "\n")
                    f.write(password)
                    f.close()
                    tk.Label(self, text='Student has been successfully Registered!', fg='#00ff00', bg='#358597',
                             font=('Calibri', 18)).pack()
                except IOError:
                    print('Invalid Path!')
            else:
                tk.Label(self, text="Register yourself again!", fg="red", font=("Calibri", 18)).pack()
        tk.Label(self, text="Name", font=('Calibri', 15), fg='#111111' ).pack()
        # Name
        self.name = tk.Entry(self, textvariable=Name_verify,font=('italic', 15), width=22).pack()
        tk.Label(self, text="Administrator ID", font=('Calibri', 15), fg='#111111' ).pack()
        # Customer ID
        self.ID = tk.Entry(self, textvariable=ID_verify, font=('italic', 15), width=22).pack()
        # PAssword
        tk.Label(self, text="Password", font=('Calibri', 15), fg='#111111').pack()
        # Customer ID
        self.ID = tk.Entry(self, textvariable=password_verify, font=('italic', 15), width=22).pack()
        tk.Label(self, text="Mobile No", font=('Calibri', 15), fg='#111111').pack()
        # Customer Mobile No
        self.MobileNo = tk.Entry(self, textvariable=MobileNo_verify, font=('italic', 15), width=22).pack()
        tk.Label(self, text="Gender", font=('Calibri', 15), fg='#111111').pack()
        # Customer Gender
        self.gender = tk.Entry(self, textvariable=Gender_verify, font=('italic', 15), width=22).pack()
        tk.Label(self, text="DOB", font=('Calibri', 15), fg='#111111' ).pack()
        # Customer DOB
        self.DOB = tk.Entry(self, textvariable=DOB_verify, font=('italic', 15), width=22).pack()
        tk.Label(self, text="Address", font=('Calibri', 15), fg='#111111' ).pack()
        # Customer Address
        self.gender = tk.Entry(self, textvariable=Address_verify, font=('italic', 15), width=22).pack()
        Register_Button = tk.Button(self, text='Register', background='#BEBEBE',font = ('italic'),command=RegisterforAdmintrator, relief='raised', borderwidth=3,
                                    width=30, height=2).pack(pady=10)
        Back_Button = tk.Button(self, text='Back', background='#9B1003',font = ('italic'), command=lambda: controller.show_frame("PMSforAdministrator"),
                                relief='raised', borderwidth=3, width=30, height=2).pack(pady=10)

class RegisterforOperator(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.Name = ''
        self.ID = ''
        self.MobileNo = ''
        self.Gender = ''
        self.DOB = ''
        self.Address = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMs.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Administrator Registration", font=('italic', 40, 'bold'))
        HeadingLabel2 = tk.Label(self, text="Enter Details Below To Register!", font=('italic', 25, 'bold'),
                                 fg='#111111')
        HeadingLabel2.pack(pady=50)
        Name_verify = tk.StringVar()
        ID_verify = tk.StringVar()
        MobileNo_verify = tk.StringVar()
        Gender_verify = tk.StringVar()
        DOB_verify = tk.StringVar()
        Address_verify = tk.StringVar()
        password_verify = tk.StringVar()
        here = os.path.dirname(os.path.realpath(__file__))
        subdir = "Users"
        filepath = os.path.join(here, subdir)
        files = os.listdir()
        if subdir in files:
            pass
        else:
            os.mkdir(os.path.join(here, subdir))
        def register_Administrator():
            name = Name_verify.get()
            ID = ID_verify.get()
            MobileNo = MobileNo_verify.get()
            Gender = Gender_verify.get()
            DOB = DOB_verify.get()
            Address = Address_verify.get()
            password = password_verify.get()
            if ID == '1' or ID == '2' or ID == '3':  # Student Roll No.
                try:
                    f = open(filepath + '\\' + ID, 'a+')
                    f.write(name + "\n")
                    f.write(ID + "\n")
                    f.write(MobileNo + "\n")
                    f.write(Gender + "\n")
                    f.write(DOB + "\n")
                    f.write(Address + "\n")
                    f.write(password)
                    f.close()
                    tk.Label(self, text='Student has been successfully Registered!', fg='#00ff00', bg='#358597',
                             font=('Calibri', 18)).pack()
                except IOError:
                    print('Invalid Path!')
            else:
                tk.Label(self, text="Register yourself again!", fg="red", font=("Calibri", 18)).pack()
        tk.Label(self, text="Name", font=('Calibri', 15), fg='#111111' ).pack()
        # Name
        self.name = tk.Entry(self, textvariable=Name_verify,font=('italic', 15), width=22).pack()
        tk.Label(self, text="Operator ID", font=('Calibri', 15), fg='#111111' ).pack()
        # Customer ID
        self.ID = tk.Entry(self, textvariable=ID_verify, font=('italic', 15), width=22).pack()
        # PAssword
        tk.Label(self, text="Password", font=('Calibri', 15), fg='#111111').pack()
        # Customer ID
        self.ID = tk.Entry(self, textvariable=password_verify, font=('italic', 15), width=22).pack()
        tk.Label(self, text="Mobile No", font=('Calibri', 15), fg='#111111').pack()
        # Customer Mobile No
        self.MobileNo = tk.Entry(self, textvariable=MobileNo_verify, font=('italic', 15), width=22).pack()
        tk.Label(self, text="Gender", font=('Calibri', 15), fg='#111111').pack()
        # Customer Gender
        self.gender = tk.Entry(self, textvariable=Gender_verify, font=('italic', 15), width=22).pack()
        tk.Label(self, text="DOB", font=('Calibri', 15), fg='#111111' ).pack()
        # Customer DOB
        self.DOB = tk.Entry(self, textvariable=DOB_verify, font=('italic', 15), width=22).pack()
        tk.Label(self, text="Address", font=('Calibri', 15), fg='#111111' ).pack()
        # Customer Address
        self.gender = tk.Entry(self, textvariable=Address_verify, font=('italic', 15), width=22).pack()
        Register_Button = tk.Button(self, text='Register', background='#BEBEBE',font = ('italic'),command=RegisterforOperator, relief='raised', borderwidth=3,
                                    width=30, height=2).pack(pady=10)
        Back_Button = tk.Button(self, text='Back', background='#9B1003',font = ('italic'), command=lambda: controller.show_frame("PMSforOperator"),
                                relief='raised', borderwidth=3, width=30, height=2).pack(pady=10)

class RegisterforTicketor(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.Name = ''
        self.ID = ''
        self.MobileNo = ''
        self.Gender = ''
        self.DOB = ''
        self.Address = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMs.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Administrator Registration", font=('italic', 40, 'bold'))
        HeadingLabel2 = tk.Label(self, text="Enter Details Below To Register!", font=('italic', 25, 'bold'),
                                 fg='#111111')
        HeadingLabel2.pack(pady=50)
        Name_verify = tk.StringVar()
        ID_verify = tk.StringVar()
        MobileNo_verify = tk.StringVar()
        Gender_verify = tk.StringVar()
        DOB_verify = tk.StringVar()
        Address_verify = tk.StringVar()
        password_verify = tk.StringVar()
        here = os.path.dirname(os.path.realpath(__file__))
        subdir = "Users"
        filepath = os.path.join(here, subdir)
        files = os.listdir()
        if subdir in files:
            pass
        else:
            os.mkdir(os.path.join(here, subdir))
        def register_Administrator():
            name = Name_verify.get()
            ID = ID_verify.get()
            MobileNo = MobileNo_verify.get()
            Gender = Gender_verify.get()
            DOB = DOB_verify.get()
            Address = Address_verify.get()
            password = password_verify.get()
            if ID == '1' or ID == '2' or ID == '3':  # Student Roll No.
                try:
                    f = open(filepath + '\\' + ID, 'a+')
                    f.write(name + "\n")
                    f.write(ID + "\n")
                    f.write(MobileNo + "\n")
                    f.write(Gender + "\n")
                    f.write(DOB + "\n")
                    f.write(Address + "\n")
                    f.write(password)
                    f.close()
                    tk.Label(self, text='Student has been successfully Registered!', fg='#00ff00', bg='#358597',
                             font=('Calibri', 18)).pack()
                except IOError:
                    print('Invalid Path!')
            else:
                tk.Label(self, text="Register yourself again!", fg="red", font=("Calibri", 18)).pack()
        tk.Label(self, text="Name", font=('Calibri', 15), fg='#111111' ).pack()
        # Name
        self.name = tk.Entry(self, textvariable=Name_verify,font=('italic', 15), width=22).pack()
        tk.Label(self, text="ID", font=('Calibri', 15), fg='#111111' ).pack()
        # Customer ID
        self.ID = tk.Entry(self, textvariable=ID_verify, font=('italic', 15), width=22).pack()
        # PAssword
        tk.Label(self, text="Password", font=('Calibri', 15), fg='#111111').pack()
        # Customer ID
        self.ID = tk.Entry(self, textvariable=password_verify, font=('italic', 15), width=22).pack()
        tk.Label(self, text="Mobile No", font=('Calibri', 15), fg='#111111').pack()
        # Customer Mobile No
        self.MobileNo = tk.Entry(self, textvariable=MobileNo_verify, font=('italic', 15), width=22).pack()
        tk.Label(self, text="Gender", font=('Calibri', 15), fg='#111111').pack()
        # Customer Gender
        self.gender = tk.Entry(self, textvariable=Gender_verify, font=('italic', 15), width=22).pack()
        tk.Label(self, text="DOB", font=('Calibri', 15), fg='#111111' ).pack()
        # Customer DOB
        self.DOB = tk.Entry(self, textvariable=DOB_verify, font=('italic', 15), width=22).pack()
        tk.Label(self, text="Address", font=('Calibri', 15), fg='#111111' ).pack()
        # Customer Address
        self.gender = tk.Entry(self, textvariable=Address_verify, font=('italic', 15), width=22).pack()
        Register_Button = tk.Button(self, text='Register', background='#BEBEBE',font = ('italic'),command=RegisterforTicketor, relief='raised', borderwidth=3,
                                    width=30, height=2).pack(pady=10)
        Back_Button = tk.Button(self, text='Back', background='#9B1003',font = ('italic'), command=lambda: controller.show_frame("PMSforTicketor"),
                                relief='raised', borderwidth=3, width=30, height=2).pack(pady=10)

class RegisterforCashier(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.Name = ''
        self.ID = ''
        self.MobileNo = ''
        self.Gender = ''
        self.DOB = ''
        self.Address = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMs.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Administrator Registration", font=('italic', 40, 'bold'))
        HeadingLabel2 = tk.Label(self, text="Enter Details Below To Register!", font=('italic', 25, 'bold'),
                                 fg='#111111')
        HeadingLabel2.pack(pady=50)
        Name_verify = tk.StringVar()
        ID_verify = tk.StringVar()
        MobileNo_verify = tk.StringVar()
        Gender_verify = tk.StringVar()
        DOB_verify = tk.StringVar()
        Address_verify = tk.StringVar()
        password_verify = tk.StringVar()
        here = os.path.dirname(os.path.realpath(__file__))
        subdir = "Users"
        filepath = os.path.join(here, subdir)
        files = os.listdir()
        if subdir in files:
            pass
        else:
            os.mkdir(os.path.join(here, subdir))
        def register_Administrator():
            name = Name_verify.get()
            ID = ID_verify.get()
            MobileNo = MobileNo_verify.get()
            Gender = Gender_verify.get()
            DOB = DOB_verify.get()
            Address = Address_verify.get()
            password = password_verify.get()
            if ID == '1' or ID == '2' or ID == '3':  # Student Roll No.
                try:
                    f = open(filepath + '\\' + ID, 'a+')
                    f.write(name + "\n")
                    f.write(ID + "\n")
                    f.write(MobileNo + "\n")
                    f.write(Gender + "\n")
                    f.write(DOB + "\n")
                    f.write(Address + "\n")
                    f.write(password)
                    f.close()
                    tk.Label(self, text='Student has been successfully Registered!', fg='#00ff00', bg='#358597',
                             font=('Calibri', 18)).pack()
                except IOError:
                    print('Invalid Path!')
            else:
                tk.Label(self, text="Register yourself again!", fg="red", font=("Calibri", 18)).pack()
        tk.Label(self, text="Name", font=('Calibri', 15), fg='#111111' ).pack()
        # Name
        self.name = tk.Entry(self, textvariable=Name_verify,font=('italic', 15), width=22).pack()
        tk.Label(self, text="Cashier ID", font=('Calibri', 15), fg='#111111' ).pack()
        # Customer ID
        self.ID = tk.Entry(self, textvariable=ID_verify, font=('italic', 15), width=22).pack()
        # PAssword
        tk.Label(self, text="Password", font=('Calibri', 15), fg='#111111').pack()
        # Customer ID
        self.ID = tk.Entry(self, textvariable=password_verify, font=('italic', 15), width=22).pack()
        tk.Label(self, text="Mobile No", font=('Calibri', 15), fg='#111111').pack()
        # Customer Mobile No
        self.MobileNo = tk.Entry(self, textvariable=MobileNo_verify, font=('italic', 15), width=22).pack()
        tk.Label(self, text="Gender", font=('Calibri', 15), fg='#111111').pack()
        # Customer Gender
        self.gender = tk.Entry(self, textvariable=Gender_verify, font=('italic', 15), width=22).pack()
        tk.Label(self, text="DOB", font=('Calibri', 15), fg='#111111' ).pack()
        # Customer DOB
        self.DOB = tk.Entry(self, textvariable=DOB_verify, font=('italic', 15), width=22).pack()
        tk.Label(self, text="Address", font=('Calibri', 15), fg='#111111' ).pack()
        # Customer Address
        self.gender = tk.Entry(self, textvariable=Address_verify, font=('italic', 15), width=22).pack()
        Register_Button = tk.Button(self, text='Register', background='#BEBEBE',font = ('italic'),command=RegisterforCashier, relief='raised', borderwidth=3,
                                    width=30, height=2).pack(pady=10)
        Back_Button = tk.Button(self, text='Back', background='#9B1003',font = ('italic'), command=lambda: controller.show_frame("PMSforCashier"),
                                relief='raised', borderwidth=3, width=30, height=2).pack(pady=10)

class LoginforAdministrator(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.AdmID = ''
        self.password = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('italic', 60, 'bold'))
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Administrator Login ', font=('italic', 30, 'bold'))
        HeadingLabel2.pack(pady=80)
        ID_verify = tk.StringVar()
        password_verify = tk.StringVar()
        tk.Label(self, text="Administrator ID", font=('italic', 15), fg='#111111').pack(pady=10)
        # Username input
        self.AdministratorID = tk.Entry(self, textvariable=ID_verify, font=('Calibri', 15), width=22).pack(ipady=7)
        tk.Label(self, text="Password", font=('italic', 15), fg='#111111').pack(pady=10)
        # Password input
        self.password = tk.Entry(self, textvariable=password_verify, font=('Calibri', 15), width=22, show = '*').pack(ipady=7)
        def login_verify():
            ID = ID_verify.get()   #Getting variable data
            password = password_verify.get()   #Getting variable data
            here = os.path.dirname(os.path.realpath(__file__))
            subdir = 'Users'
            filepath = os.path.join(here , subdir)
            list_of_file = os.listdir('Users')
            if ID in list_of_file:   #Password checker
                file = open(filepath + '\\' + ID , 'r')
                verify = file.read().splitlines()
                if password in verify:
                    controller.show_frame('Customer')
                else:
                    tk.Label(self, text = 'Incorrect Password!', fg="red", bg="#358597", font=("Calibri", 18)).pack()
            else:
                tk.Label(self,text = 'Invalid User!', fg="red", bg="#358597", font=("Calibri", 18)).pack()
        Enter_Button = tk.Button(self, text='Enter',command =lambda: controller.show_frame("AdministratorWindow"), relief='raised',font = ('italic'),background = '#BEBEBE', borderwidth=3, width=30, height=2).pack(pady=10) #Creating an Enter button
        Back_Button = tk.Button(self, text='Back', command=lambda: controller.show_frame("PMSforAdministrator"),relief='raised',font = ('italic'),background = '#9B1003', borderwidth=3, width=30, height=2).pack(pady=10)

class LoginforOperator(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.AdmID = ''
        self.password = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('italic', 60, 'bold'))
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Operator Login ', font=('italic', 30, 'bold'))
        HeadingLabel2.pack(pady=80)
        ID_verify = tk.StringVar()
        password_verify = tk.StringVar()
        tk.Label(self, text="Operator ID", font=('italic', 15), fg='#111111').pack(pady=10)
        # Username input
        self.AdministratorID = tk.Entry(self, textvariable=ID_verify, font=('Calibri', 15), width=22).pack(ipady=7)
        tk.Label(self, text="Password", font=('italic', 15), fg='#111111').pack(pady=10)
        # Password input
        self.password = tk.Entry(self, textvariable=password_verify, font=('Calibri', 15), width=22, show = '*').pack(ipady=7)
        def login_verify():
            ID = ID_verify.get()   #Getting variable data
            password = password_verify.get()   #Getting variable data
            here = os.path.dirname(os.path.realpath(__file__))
            subdir = 'Users'
            filepath = os.path.join(here , subdir)
            list_of_file = os.listdir('Users')
            if ID in list_of_file:   #Password checker
                file = open(filepath + '\\' + ID , 'r')
                verify = file.read().splitlines()
                if password in verify:
                    controller.show_frame('Customer')
                else:
                    tk.Label(self, text = 'Incorrect Password!', fg="red", bg="#358597", font=("Calibri", 18)).pack()
            else:
                tk.Label(self,text = 'Invalid User!', fg="red", bg="#358597", font=("Calibri", 18)).pack()
        Enter_Button = tk.Button(self, text='Enter',command =lambda: controller.show_frame("OperatorWindow"), relief='raised',font = ('italic'),background = '#BEBEBE', borderwidth=3, width=30, height=2).pack(pady=10) #Creating an Enter button
        Back_Button = tk.Button(self, text='Back', command=lambda: controller.show_frame("PMSforOperator"),relief='raised',font = ('italic'),background = '#9B1003', borderwidth=3, width=30, height=2).pack(pady=10)

class LoginforTicketor(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.AdmID = ''
        self.password = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('italic', 60, 'bold'))
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Ticketor Login ', font=('italic', 30, 'bold'))
        HeadingLabel2.pack(pady=80)
        ID_verify = tk.StringVar()
        password_verify = tk.StringVar()
        tk.Label(self, text="Ticketor ID", font=('italic', 15), fg='#111111').pack(pady=10)
        # Username input
        self.AdministratorID = tk.Entry(self, textvariable=ID_verify, font=('Calibri', 15), width=22).pack(ipady=7)
        tk.Label(self, text="Password", font=('italic', 15), fg='#111111').pack(pady=10)
        # Password input
        self.password = tk.Entry(self, textvariable=password_verify, font=('Calibri', 15), width=22, show = '*').pack(ipady=7)
        def login_verify():
            ID = ID_verify.get()   #Getting variable data
            password = password_verify.get()   #Getting variable data
            here = os.path.dirname(os.path.realpath(__file__))
            subdir = 'Users'
            filepath = os.path.join(here , subdir)
            list_of_file = os.listdir('Users')
            if ID in list_of_file:   #Password checker
                file = open(filepath + '\\' + ID , 'r')
                verify = file.read().splitlines()
                if password in verify:
                    controller.show_frame('Customer')
                else:
                    tk.Label(self, text = 'Incorrect Password!', fg="red", bg="#358597", font=("Calibri", 18)).pack()
            else:
                tk.Label(self,text = 'Invalid User!', fg="red", bg="#358597", font=("Calibri", 18)).pack()
        Enter_Button = tk.Button(self, text='Enter',command =lambda: controller.show_frame("TicketorWindow"), relief='raised',font = ('italic'),background = '#BEBEBE', borderwidth=3, width=30, height=2).pack(pady=10) #Creating an Enter button
        Back_Button = tk.Button(self, text='Back', command=lambda: controller.show_frame("PMSforTicketor"),relief='raised',font = ('italic'),background = '#9B1003', borderwidth=3, width=30, height=2).pack(pady=10)

class LoginforCashier(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.AdmID = ''
        self.password = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('italic', 60, 'bold'))
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Cashier Login ', font=('italic', 30, 'bold'))
        HeadingLabel2.pack(pady=80)
        ID_verify = tk.StringVar()
        password_verify = tk.StringVar()
        tk.Label(self, text="Administrator ID", font=('italic', 15), fg='#111111').pack(pady=10)
        # Username input
        self.AdministratorID = tk.Entry(self, textvariable=ID_verify, font=('Calibri', 15), width=22).pack(ipady=7)
        tk.Label(self, text="Password", font=('italic', 15), fg='#111111').pack(pady=10)
        # Password input
        self.password = tk.Entry(self, textvariable=password_verify, font=('Calibri', 15), width=22, show = '*').pack(ipady=7)
        def login_verify():
            ID = ID_verify.get()   #Getting variable data
            password = password_verify.get()   #Getting variable data
            here = os.path.dirname(os.path.realpath(__file__))
            subdir = 'Users'
            filepath = os.path.join(here , subdir)
            list_of_file = os.listdir('Users')
            if ID in list_of_file:   #Password checker
                file = open(filepath + '\\' + ID , 'r')
                verify = file.read().splitlines()
                if password in verify:
                    controller.show_frame('Customer')
                else:
                    tk.Label(self, text = 'Incorrect Password!', fg="red", bg="#358597", font=("Calibri", 18)).pack()
            else:
                tk.Label(self,text = 'Invalid User!', fg="red", bg="#358597", font=("Calibri", 18)).pack()
        Enter_Button = tk.Button(self, text='Enter',command =lambda: controller.show_frame("CashierWindow"), relief='raised',font = ('italic'),background = '#BEBEBE', borderwidth=3, width=30, height=2).pack(pady=10) #Creating an Enter button
        Back_Button = tk.Button(self, text='Back', command=lambda: controller.show_frame("PMSforCashier"),relief='raised',font = ('italic'),background = '#9B1003', borderwidth=3, width=30, height=2).pack(pady=10)

class AdministratorWindow(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.username = ''
        self.password = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('italic', 60, 'bold'))
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Administrator', font=('italic', 30, 'bold'))
        HeadingLabel2.pack(pady=80)
        username_verify = tk.StringVar()
        password_verify = tk.StringVar()
        Register_Button = tk.Button(self, text='Register Customer detail', command=lambda: controller.show_frame("Customer"),
                                    relief='raised', borderwidth=3, width=40, height=3,background='#BEBEBE')
        Register_Button.pack(pady=10)

        update_Button = tk.Button(self, text='Update Customer detail',command=lambda: controller.show_frame("Customer"),
                                    relief='raised', borderwidth=3, width=40, height=3,background='#BEBEBE')
        update_Button.pack(pady=10)

        view_Button = tk.Button(self, text='View Customer detail',
                                  command=lambda: controller.show_frame("Customer"),
                                  relief='raised', borderwidth=3, width=40, height=3,background='#BEBEBE')
        view_Button.pack(pady=10)

        delete_Button = tk.Button(self, text='Delete Customer detail',
                                command=lambda: controller.show_frame("Customer"),
                                relief='raised', borderwidth=3, width=40, height=3,background='#BEBEBE')
        delete_Button.pack(pady=10)

        search_Button = tk.Button(self, text='Search Customer detail',
                                command=lambda: controller.show_frame("Customer"),
                                relief='raised', borderwidth=3, width=40, height=3,background='#BEBEBE')
        search_Button.pack(pady=10)

        logout_Button = tk.Button(self, text='Log out',
                                command=lambda: controller.show_frame("MainWindow"),
                                relief='raised', borderwidth=3, width=40, height=3,background='#BEBEBE')
        logout_Button.pack(pady=10)
        def login_verify():
            username = username_verify.get()  # Getting variable data
            password = password_verify.get()  # Getting variable data
            here = os.path.dirname(os.path.realpath(__file__))
            subdir = 'Users'
            filepath = os.path.join(here, subdir)
            list_of_file = os.listdir('Users')
            if username in list_of_file:  # Password checker
                file = open(filepath + '\\' + username, 'r')
                verify = file.read().splitlines()
                if password in verify:
                    controller.show_frame('Mainwin2forLib')
                else:
                    tk.Label(self, text='Incorrect Password!', fg="red", bg="#358597", font=("Calibri", 18)).pack()
            else:
                tk.Label(self, text='Invalid User!', fg="red", bg="#358597", font=("Calibri", 18)).pack()

class OperatorWindow(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.username = ''
        self.password = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('italic', 60, 'bold'))
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Operator', font=('italic', 30, 'bold'))
        HeadingLabel2.pack(pady=60)
        username_verify = tk.StringVar()
        password_verify = tk.StringVar()
        Enter_Button = tk.Button(self, text='Enter Parking slot', command=lambda: controller.show_frame("Customer"),
                                    relief='raised', borderwidth=3, width=40, height=3,background='#BEBEBE')
        Enter_Button.pack(pady=10)

        view_Button = tk.Button(self, text='View Parking slots',command=lambda: controller.show_frame("Customer"),
                                    relief='raised', borderwidth=3, width=40, height=3,background='#BEBEBE')
        view_Button.pack(pady=10)

        delete_Button = tk.Button(self, text='Delete Parking slot',
                                  command=lambda: controller.show_frame("Customer"),
                                  relief='raised', borderwidth=3, width=40, height=3,background='#BEBEBE')
        delete_Button.pack(pady=10)

        search_Button = tk.Button(self, text='Search Parking slot',
                                command=lambda: controller.show_frame("Customer"),
                                relief='raised', borderwidth=3, width=40, height=3,background='#BEBEBE')
        search_Button.pack(pady=10)

        reserve_Button = tk.Button(self, text='Reserve Parking slot',
                                command=lambda: controller.show_frame("Customer"),
                                relief='raised', borderwidth=3, width=40, height=3,background='#BEBEBE')
        reserve_Button.pack(pady=10)

        find_Button = tk.Button(self, text='Register Parking slot',
                                   command=lambda: controller.show_frame("Customer"),
                                   relief='raised', borderwidth=3, width=40, height=3, background='#BEBEBE')
        find_Button.pack(pady=10)

        logout_Button = tk.Button(self, text='Log out',
                                command=lambda: controller.show_frame("MainWindow"),
                                relief='raised', borderwidth=3, width=40, height=3,background='#BEBEBE')
        logout_Button.pack(pady=10)
        def login_verify():
            username = username_verify.get()  # Getting variable data
            password = password_verify.get()  # Getting variable data
            here = os.path.dirname(os.path.realpath(__file__))
            subdir = 'Users'
            filepath = os.path.join(here, subdir)
            list_of_file = os.listdir('Users')
            if username in list_of_file:  # Password checker
                file = open(filepath + '\\' + username, 'r')
                verify = file.read().splitlines()
                if password in verify:
                    controller.show_frame('Mainwin2forLib')
                else:
                    tk.Label(self, text='Incorrect Password!', fg="red", bg="#358597", font=("Calibri", 18)).pack()
            else:
                tk.Label(self, text='Invalid User!', fg="red", bg="#358597", font=("Calibri", 18)).pack()

class TicketorWindow(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.username = ''
        self.password = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('italic', 60, 'bold'))
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Operator', font=('italic', 30, 'bold'))
        HeadingLabel2.pack(pady=60)
        username_verify = tk.StringVar()
        password_verify = tk.StringVar()
        Update_Button = tk.Button(self, text='Update Parking slot',
                                    relief='raised', borderwidth=3, width=40, height=3,background='#BEBEBE')
        Update_Button.pack(pady=10)

        logout_Button = tk.Button(self, text='Log out',
                                command=lambda: controller.show_frame("MainWindow"),
                                relief='raised', borderwidth=3, width=40, height=3,background='#BEBEBE')
        logout_Button.pack(pady=10)
        def login_verify():
            username = username_verify.get()  # Getting variable data
            password = password_verify.get()  # Getting variable data
            here = os.path.dirname(os.path.realpath(__file__))
            subdir = 'Users'
            filepath = os.path.join(here, subdir)
            list_of_file = os.listdir('Users')
            if username in list_of_file:  # Password checker
                file = open(filepath + '\\' + username, 'r')
                verify = file.read().splitlines()
                if password in verify:
                    controller.show_frame('Mainwin2forLib')
                else:
                    tk.Label(self, text='Incorrect Password!', fg="red", bg="#358597", font=("Calibri", 18)).pack()
            else:
                tk.Label(self, text='Invalid User!', fg="red", bg="#358597", font=("Calibri", 18)).pack()

class CashierWindow(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.username = ''
        self.password = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('italic', 60, 'bold'))
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        HeadingLabel2 = tk.Label(self, text='Operator', font=('italic', 30, 'bold'))
        HeadingLabel2.pack(pady=60)
        username_verify = tk.StringVar()
        password_verify = tk.StringVar()
        Reciept_Button = tk.Button(self, text='Make a Receipt',
                                    relief='raised', borderwidth=3, width=40, height=3,background='#BEBEBE')
        Reciept_Button.pack(pady=10)

        logout_Button = tk.Button(self, text='Log out',
                                command=lambda: controller.show_frame("MainWindow"),
                                relief='raised', borderwidth=3, width=40, height=3,background='#BEBEBE')
        logout_Button.pack(pady=10)
        def login_verify():
            username = username_verify.get()  # Getting variable data
            password = password_verify.get()  # Getting variable data
            here = os.path.dirname(os.path.realpath(__file__))
            subdir = 'Users'
            filepath = os.path.join(here, subdir)
            list_of_file = os.listdir('Users')
            if username in list_of_file:  # Password checker
                file = open(filepath + '\\' + username, 'r')
                verify = file.read().splitlines()
                if password in verify:
                    controller.show_frame('Mainwin2forLib')
                else:
                    tk.Label(self, text='Incorrect Password!', fg="red", bg="#358597", font=("Calibri", 18)).pack()
            else:
                tk.Label(self, text='Invalid User!', fg="red", bg="#358597", font=("Calibri", 18)).pack()

class Customer(basepage):
    def __init__(self, parent, controller):
        super().__init__(parent,controller)
        self.CustName = ''
        self.CustID = ''
        self.CustMobileNo = ''
        self.CustGender = ''
        self.CustDOB = ''
        self.CustAddress = ''
        self.controller = controller
        self.controller.iconphoto(False, tk.PhotoImage(file='PMS.png'))
        self.controller.title("Parking Management System ")
        self.controller.state('zoomed')
        HeadingLabel1 = tk.Label(self, text="Parking Management System", font=('Calibri', 60,), foreground='#F4A896',
                                 background='#358597')
        HeadingLabel1.pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget("font"))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        space = tk.Label(self, height=8, bg='#358597').pack()
        f = tkfont.Font(HeadingLabel1, HeadingLabel1.cget('font'))
        f.configure(underline=True)
        HeadingLabel1.configure(font=f)
        space1 = tk.Label(self, height=2, bg='#358597').pack()
        HeadingLabel = tk.Label(self, text="Customer Details", font=('Calibri', 15, 'bold'),
                                bg='#358597', fg='#F4A896')
        HeadingLabel.pack()
        CustName_verify = tk.StringVar()
        CustID_verify = tk.StringVar()
        CustMobileNo_verify = tk.StringVar()
        CustGender_verify = tk.StringVar()
        CustDOB_verify = tk.StringVar()
        CustAddress_verify = tk.StringVar()
        here = os.path.dirname(os.path.realpath(__file__))
        subdir = 'Books'
        subdir2 = 'New Books'
        filepath = os.path.join(here, subdir)
        filepath2 = os.path.join(here, subdir2)
        files = os.listdir()
        if subdir in files:
            pass
        else:
            os.mkdir(os.path.join(here, subdir))
        if subdir2 in files:
            pass
        else:
            os.mkdir(os.path.join(here, subdir2))
        def Add_customer():
            name = CustName_verify.get()
            ID = CustID_verify.get()
            MobileNo = CustMobileNo_verify.get()
            Gender = CustGender_verify.get()
            DOB = CustDOB_verify.get()
            Address = CustAddress_verify.get()
            list_of_file = os.listdir('Books')
            if isbn in list_of_file:
                file = open(filepath + '\\' + name, 'r')
                file.close()
                # verify = file.read().splitlines()
                # if name in verify:
                tk.Label(self, text='This Book is already Present!', fg='red', bg='#358597',
                         font=('Calibri', 18), ).pack()
            else:
                data = open(filepath2 + '\\' + name, 'w')
                data.write(f"name: {name}\nID: {ID}\nMobileNo: {MobileNo}\nGender: {Gender}\nDOB: {DOB}\nAddress:{Address}")
                data.close()
                data = open(filepath + '\\' + name, 'w')
                data.write(f"name: {name}\nID: {ID}\nMobileNo: {MobileNo}\nGender: {Gender}\nDOB: {DOB}\nAddress:{Address}")
                data.close()
                tk.Label(self, text='Book has been Added!', fg='#00ff00', bg='#358597',
                         font=('Times New Roman', 18)).pack()
        # list_all_file = os.listdir()
        # tk.Label(self,text=list_all_file ,font = ('times New Roman' , 8),fg='black',bg = 'white' , ).pack(pady=10)
        tk.Label(self, text="Name", font=('Calibri', 15), fg='#358597', bg='#358597', ).pack()
        #Name
        self.name = tk.Entry(self, textvariable=CustName_verify, font=('Calibri', 15), width=22).pack()
        tk.Label(self, text="Cutomer ID", font=('Calibri', 15), fg='#F4A896', bg='#358597', ).pack()
        #Customer ID
        self.ID= tk.Entry(self, textvariable=CustID_verify, font=('Calibri', 15), width=22).pack()
        tk.Label(self, text="Mobile No", font=('Calibri', 15), fg='#F4A896', bg='#358597').pack()
        #Customer Mobile No
        self.MobileNo = tk.Entry(self, textvariable=CustMobileNo_verify, font=('Calibri', 15), width=22).pack()
        tk.Label(self, text="Gender", font=('Calibri', 15), fg='#F4A896', bg='#358597', ).pack()
        #Customer Gender
        self.gender = tk.Entry(self, textvariable=CustGender_verify, font=('Calibri', 15), width=22).pack()
        tk.Label(self, text="DOB", font=('Calibri', 15), fg='#F4A896', bg='#358597', ).pack()
        # Customer DOB
        self.DOB = tk.Entry(self, textvariable=CustDOB_verify, font=('Calibri', 15), width=22).pack()
        tk.Label(self, text="Address", font=('Calibri', 15), fg='#F4A896', bg='#358597', ).pack()
        # Customer Address
        self.gender = tk.Entry(self, textvariable=CustAddress_verify, font=('Calibri', 15), width=22).pack()
        Enter_Button = tk.Button(self, text='Enter', command=Add_customer, relief='raised', borderwidth=3, width=40,
                                 height=3).pack(pady=10)
        back_Button = tk.Button(self, text='Back', command=lambda: controller.show_frame("LoginforAdministrator"),
                                relief='raised', borderwidth=3, width=40, height=3).pack(pady=10)

if __name__ == "__main__":
    app = Main()
    app.mainloop()