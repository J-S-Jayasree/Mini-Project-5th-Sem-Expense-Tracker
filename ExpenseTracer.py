from tkinter import ttk
from AskExisting import existing
from LanguageChatBot import *
import time
import string
import random
from AskExpenseApp import *
from PIL import ImageTk, Image
# SINGLE LEVEL INHERITANCE
class SampleApp(tk.Tk):
# FUNCTION 1 : SHOWS GUI TO REGISTER THE USER
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("500x500")
        self.title("Registration of New User !! ")
        self.label8 = tk.Label(self, text="BE A PART TO GUIDE THROUGH YOUR EXPENSES!!").place(x=100)
        self.label = tk.Label(self, text="What is your Name? (max character 15)").place(x=50, y=30)
        self.entry = tk.Entry(self)
        self.entry.place(x=300, y=30)
        self.label2 = tk.Label(self, text="Enter your Phone Number :").place(x=50, y=70)
        self.entry2 = tk.Entry(self)
        self.entry2.place(x=300, y=70)
        self.label4 = tk.Label(self, text="Enter your Mail-Id :", width=20).place(x=28, y=110)
        self.entry4 = tk.Entry(self)
        self.entry4.place(x=300, y=110)
        self.label6 = tk.Label(self, text="Select Security Question :").place(x=47, y=150)
        self.questions = tk.ttk.Combobox(self, width=50, state="readonly")
        self.questions.place(x=100, y=180)
        self.questions['values'] = ('~~~None selected~~~', ' What is your Nick-Name ?',
                                    ' What is your Grandmother\'s name?(Mother side)',
                                    ' Which is Your Favourite place?',
                                    ' What is your Best Friend\'s name?',
                                    ' What is your Grandfather\'s Occupation?(Father side)',
                                    ' Who is the Internet Service Provider(at home)?',
                                    ' Which is your favourite book?',
                                    ' What is the name of your First School?',
                                    )
        self.questions.current(0)
        self.entry6 = tk.Entry(self)
        self.entry6.place(x=100, y=230)


        '''self.button1 = tk.Button(self, text="Capture Photo", command=self.capture)
        # self.button1.grid(row=16, column=1)
        self.button1.place(bordermode=OUTSIDE, x=100, y=300, width=200, height=50)'''

        self.button = tk.Button(self, text="Submit", command=self.on_button)
        self.button.place(bordermode=OUTSIDE, x=100, y=400, width=200, height=50)
# FUNCTION 2: CALLED WHEN SUBMIT IS CLICKED TO CHECK THE VALID DETAILS IS ENTERED BY USER OR NOT
    def on_button(self):
        flag = 1
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        name = self.entry.get()
        phone = self.entry2.get()
        email = self.entry4.get()
        option1 = self.entry6.get()
        current = str(self.questions.get());
        if len(name) <= 0 or len(name) > 15:
            flag = 0
            self.label1 = tk.Label(self, text='* Invalid Name! Entered *', fg='red').place(x=300, y=50)
        if len(phone) > 10 or len(phone) < 10:
            flag = 0
            self.label3 = tk.Label(self, text='* Invalid Phone Number! *', fg='red').place(x=300, y=90)
        if (not re.search(regex, email)):
            flag = 0
            self.label5 = tk.Label(self, text='* Invalid Email *', fg='red').place(x=300, y=130)
        if len(option1) == 0:
            flag = 0
            self.label7 = tk.Label(self, text='* Enter the Answer for the Question Chosen *', fg='red').place(x=100,y=250)
        if (flag == 1):
            temp = self.password()
            messagebox.showinfo("Password is:", temp)
            time.sleep(2)
            messagebox.showinfo("Welcome", "Successful registration")
            self.destroy()
            top.destroy()
            s1 = sql()
            s1.insert(name,phone,email,current,option1,temp)
            s1.insertexpenseintoApp()

    '''def capture(self):
        time.sleep(5)
        videoCaptureObject = cv2.VideoCapture(0)
        result = True
        while (result):
            ret, frame = videoCaptureObject.read()
            time.sleep(10)
            cv2.imwrite(self.entry.get() + ".jpg", frame)
            result = False
            videoCaptureObject.release()
            cv2.destroyAllWindows()'''
# FUNCTION 3: TO AUTO GENERATE PASSWORD
    def password(self):
        combinedstring = string.ascii_letters + string.digits + string.punctuation
        print(type(combinedstring))
        userpassword = ""
        for i in range(8):
            userpassword = userpassword + random.choice(combinedstring)
        return userpassword

top = Tk()
top.title("EXPENSE TRACKER !!")
top.geometry("500x500")
photo = ImageTk.PhotoImage(Image.open("C:/Python/ExpenseTracker/Picture/ControlyourExpense.webp"))
logo = Label(top, image=photo).place(x=50, y=50)
B = Button(top, text="New User", command=SampleApp, activebackground="yellow", activeforeground="red",
           highlightcolor='green')
B.place(x=200, y=300)
# FUNCTION OF EXPENSE TRACER MODULE CALLED WHEN EXISTING USER VISITS
def check():
    def nameandpass():
        print('Hrllo')
        un=Existing.entry2.get()
        up=Existing.entry3.get()
        if len(un)==0 or len(up)==0:
            alert = Tk()
            alert.geometry("100x100")
            messagebox.showwarning("Warning", "Please enter !!")
            alert.mainloop()
            alert.destroy()

        print(un,up)
        mydb1 = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="indira@123"
        )
        mycursor1 = mydb1.cursor()
        mycursor1.execute("use expense_tracker_app;")
        mycursor1.execute("SELECT * FROM `v1` WHERE Username='%s';" % (un))
        userrecord = mycursor1.fetchall()
        b=userrecord[0]
        print(b)
        if not userrecord:
            alert = Tk()
            alert.geometry("100x100")
            messagebox.showwarning("Warning", " Please Register")
            alert.mainloop()
        else:
            a = userrecord[0]
            userid=a[0]
            username=a[1]
            userpassword=a[2]
            userq=a[3]
            usera=a[4]
            if userpassword==up:
                msg2 = messagebox.showinfo("Welcome", "Successful Login")
                Existing.destroy()

                def securityquestion():
                    answer = Existing1.entry2.get()
                    if len(answer) == 0 or answer != usera:
                        alert = Tk()
                        alert.geometry("100x100")
                        messagebox.showwarning("Warning", "Please enter valid answer!!")
                        alert.mainloop()
                        alert.destroy()
                    elif answer == usera:
                        msg2 = messagebox.showinfo("Welcome", "Successful Login")
                        Existing1.destroy()
                        e1=existing(username,userpassword,userq,usera,userid)
                        e1.update()
                Existing1=Tk()
                Existing1.title("SECURITY QUESTION!!")
                Existing1.geometry("400x400")
                Existing1.label1 = tk.Label(Existing1, text=" Please enter Answer for the quesion: !!", font=('Helvetica', 10, 'bold')).place(x=100, y=10)

                Existing1.label2 = tk.Label(Existing1, text=userq).place(x=20, y=50)
                Existing1.entry2 = tk.Entry(Existing1)
                Existing1.entry2.place(x=100, y=100)

                Existing1.button1 = tk.Button(Existing1, text="Login", command=securityquestion)
                Existing1.button1.place(bordermode=OUTSIDE, x=100, y=200, width=70, height=50)
                Existing1.mainloop()
            else:
                alert = Tk()
                alert.geometry("100x100")
                messagebox.showwarning("Warning", "Password Wrong !!")
                alert.mainloop()


    Existing=Tk()
    Existing.title("LOG IN!!")
    Existing.geometry("250x250")
    Existing.label1=tk.Label(Existing,text="LOGIN !!",font=('Helvetica',10,'bold')).place(x=250,y=10)

    Existing.label2=tk.Label(Existing,text="Username :").place(x=20,y=50)
    Existing.entry2 = tk.Entry(Existing)
    Existing.entry2.place(x=100, y=50)

    Existing.label3=tk.Label(Existing,text="Password :").place(x=20,y=90)
    Existing.entry3 = tk.Entry(Existing,show='*')
    Existing.entry3.place(x=100, y=90)

    Existing.button1 = tk.Button(Existing, text="Submit", command=nameandpass)
    Existing.button1.place(bordermode=OUTSIDE, x=100, y=150, width=70, height=50)
    Existing.mainloop()

B1 = Button(top, text="Existing User", command=check)
B1.place(x=190, y=400)
chatty()
top.mainloop()
app = SampleApp()
app.mainloop()


