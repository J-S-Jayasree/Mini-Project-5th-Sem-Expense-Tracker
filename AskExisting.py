import mysql as mysql
import mysql.connector
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
class existing:
    def __init__(self,name,password,question,answer,userid):
        self.name=name
        self.password=password
        self.question=question
        self.answer=answer
        self.userid=userid
    def update(self):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="indira@123"
        )
        mycursor = mydb.cursor()
        mycursor.execute("use expense_tracker_app;")
        mycursor.execute("update `admin` set Lastaccess=NOW() WHERE Userid='%s';"%(self.userid))
        mydb.commit()
        print(mycursor.lastrowid, "record inserted.")
        print(mycursor.rowcount)

        self.insertexpenseintoApp1()
        print('I')
    def insertexpenseintoApp1(self):
        category_expense = dict()
        def submit():
            def check(k,n):
                try:
                    d=float(n)
                    category_expense[k]=n
                except ValueError:
                    category_expense[k]=0.00


            num=App1.entry3.get()
            print(num)
            num1=App1.entry4.get()
            num2=App1.entry5.get()
            print(num2)
            num3=App1.entry6.get()
            num4=App1.entry7.get()
            num5=App1.entry8.get()
            num6=App1.entry9.get()
            num7=App1.entry10.get()
            num8=App1.entry11.get()
            num9=App1.entry12.get()
            num10=App1.entry13.get()
            num11=App1.entry14.get()
            num12=App1.entry15.get()
            num13=App1.entry16.get()
            num14=App1.entry17.get()

            if len(num) > 9 or len(num1) > 9 or len(num3) > 9 or len(num4) > 9 or len(num5) > 9 or len(num6) > 9 or len(num7) > 9 or len(num8) > 9 or len(num9) > 9 or len(num10) > 9 or len(num11) > 9 or len(num12) > 9 or len(num13) > 9 or len(num14) > 9:
                alert= Tk()
                alert.geometry("100x100")
                messagebox.showwarning("Warning", " Max 9 digits")
                alert.mainloop()

            if App1.month.current()==0:
                alert1 = Tk()
                alert1.geometry("100x100")
                messagebox.showwarning("Warning", " Choose a month ")
                alert1.mainloop()
            check('Grocery', num)
            check('Medicine',num1)
            check('Shopping',num2)
            check('Entertainment',num3)
            check('Tax',num4)
            check('Houserent',num5)
            check('Houseeb',num6)
            check('Housewb',num7)
            check('Housefurniture',num8)
            check('Houseelectronic',num9)
            check('Housegas',num10)
            check('Personal',num11)
            check('Loan',num12)
            check('Insurance',num13)
            check('Education',num14)
            print(category_expense)

            self.insertexpenseintodb1(category_expense, App1.month.get(),self.name,self.password,self.question,self.answer,self.userid)


        App1=Tk()
        App1.title("EXPENSE DETAILS !!")
        App1.geometry("700x1100")
        App1.label = tk.Label(App1, text="RECORDING YOUR EXPENSES !!",font=("Helvetica", 10,'bold')).place(x=250,y=10)

        App1.label1=tk.Label(App1,text='Select month :').place(x=10,y=50)
        App1.month = tk.ttk.Combobox(App1, width=40, state="readonly")
        App1.month.place(x=400,y=50)
        App1.month['values'] = ('~~~None selected~~~',' Jan',' Feb', ' Mar', ' Apr',' May ', ' June ',' July ',
                                    ' Aug ',' Sep ',' Oct ',' Nov ',' Dec ')
        App1.month.current(0)

        App1.label2=tk.Label(App1,text='Current year').place(x=10,y=90)
        App1.label18=tk.Label(App1,text="* Max no. of characters allowed 9 for expense field *",fg='red').place(x=400,y=110)
        import datetime
        x = datetime.datetime.now()
        App1.label2=tk.Label(App1,text=x.year).place(x=400,y=90)

        App1.label3=tk.Label(App1,text="Enter the amount spent on Grocery :",font=("Helvetica",10)).place(x=10,y=130)
        App1.entry3=tk.Entry(App1)
        App1.entry3.place(x=400, y=130)

        App1.label4 = tk.Label(App1, text="Enter Medical expenses :",font=("Helvetica",10)).place(x=10, y=170)
        App1.entry4 = tk.Entry(App1)
        App1.entry4.place(x=400, y=170)

        App1.label5 = tk.Label(App1, text="Enter Shopping expenses :",font=("Helvetica",10)).place(x=10, y=210)
        App1.entry5 = tk.Entry(App1)
        App1.entry5.place(x=400, y=210)

        App1.label6= tk.Label(App1, text="Enter Entertainment expenses :",font=("Helvetica",10)).place(x=10, y=250)
        App1.entry6 = tk.Entry(App1)
        App1.entry6.place(x=400, y=250)

        App1.label7 = tk.Label(App1, text="Enter Tax expenses :", font=("Helvetica",10)).place(x=10, y=290)
        App1.entry7 = tk.Entry(App1)
        App1.entry7.place(x=400, y=290)

        App1.label8 = tk.Label(App1, text="Enter House-rent expenses :", font=("Helvetica",10)).place(x=10, y=330)
        App1.entry8 = tk.Entry(App1)
        App1.entry8.place(x=400, y=330)

        App1.label9= tk.Label(App1, text="Enter House-EB expenses :", font=("Helvetica",10)).place(x=10, y=370)
        App1.entry9= tk.Entry(App1)
        App1.entry9.place(x=400, y=370)

        App1.label10 = tk.Label(App1, text="Enter House-WaterBill expenses :", font=("Helvetica",10)).place(x=10, y=410)
        App1.entry10 = tk.Entry(App1)
        App1.entry10.place(x=400, y=410)

        App1.label11 = tk.Label(App1, text="Enter House-Furniture expenses :", font=("Helvetica",10)).place(x=10, y=450)
        App1.entry11 = tk.Entry(App1)
        App1.entry11.place(x=400, y=450)

        App1.label12 = tk.Label(App1, text="Enter House-Electronic expenses :", font=("Helvetica", 10)).place(x=10,y=490)
        App1.entry12 = tk.Entry(App1)
        App1.entry12.place(x=400, y=490)

        App1.label13= tk.Label(App1, text="Enter House-Gas expenses :", font=("Helvetica",10)).place(x=10, y=530)
        App1.entry13= tk.Entry(App1)
        App1.entry13.place(x=400, y=530)

        App1.label14 = tk.Label(App1, text="Enter Personal expenses :", font=("Helvetica",10)).place(x=10, y=570)
        App1.entry14 = tk.Entry(App1)
        App1.entry14.place(x=400, y=570)

        App1.label15= tk.Label(App1, text="Enter Loan expenses :", font=("Helvetica",10)).place(x=10, y=610)
        App1.entry15 = tk.Entry(App1)
        App1.entry15.place(x=400, y=610)

        App1.label16= tk.Label(App1, text="Enter Insurance expenses :", font=("Helvetica",10)).place(x=10, y=650)
        App1.entry16 = tk.Entry(App1)
        App1.entry16.place(x=400, y=650)

        App1.label17= tk.Label(App1, text="Enter Educational expenses :", font=("Helvetica",10)).place(x=10, y=690)
        App1.entry17 = tk.Entry(App1)
        App1.entry17.place(x=400, y=690)

        App1.button = tk.Button(App1, text="Submit", command=submit)
        App1.button.place(bordermode=OUTSIDE, x=250, y=730, width=200, height=50)

        App1.mainloop()

    def insertexpenseintodb1(self, d, m,n,p,q,a,u):
            import datetime
            x = datetime.datetime.now()
            final_dict = dict()
            for i in d:
                if float(d[i]) > 0.00:
                    final_dict[i] = d[i]

            total = 0.0
            for i in final_dict:
                total += float(final_dict[i])

            print(total)
            mydb1 = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="indira@123"
            )
            mycursor1 = mydb1.cursor()
            mycursor1.execute("use expense_tracker_app;")

            sql1 = """INSERT INTO `expense_tracker_app`.`cumulativeexpense` (`Userid`, `UserMonth`, `Currentyear`, `Totalexpense`) VALUES (%s, %s, %s,%s);"""
            values1 = (u, m, x.year, total)
            mycursor1.execute(sql1, values1)
            mydb1.commit()
            for i in final_dict:
                mycursor1 = mydb1.cursor()
                mycursor1.execute("use expense_tracker_app;")
                # un='Grocery'
                mycursor1.execute("SELECT idCategory FROM `category` WHERE Category_name='%s';" % (i))
                userid = mycursor1.fetchone()
                print(userid)
                print(type(userid))
                sql1 = """INSERT INTO `expense_tracker_app`.`monthlyexpense` (`Userid`, `Month`, `idCategory`, `Amount`) VALUES (%s, %s, %s,%s);"""
                values1 = (u, m, userid[0], float(final_dict[i]))
                mycursor1.execute(sql1, values1)
                mydb1.commit()
            op1=[]
            mycursor2=mydb1.cursor()
            mycursor2.execute("use expense_tracker_app;")
            mycursor2.execute("select Month, count(*) from monthlyexpense where Userid = '%s' group by(Month)" %(u))
            output=mycursor2.fetchall()
            print(output, len(output), type(output))
            if len(output)==2:
                lim = output[0][1]
                mycursor2.execute("select Month, Category_Name, Amount from monthlyexpense, admin, category where admin.Userid = monthlyexpense.Userid and monthlyexpense.idCategory = category.idCategory and monthlyexpense.Userid = %s limit %s" % (u, lim))
                op2 = mycursor2.fetchall()
                print(op2)
                op1=op2[:]
            else:
                lim1 = 0
                for i in range(0,len(output)-2):
                    lim1+=output[i][1]
                lim2 = output[-2][1]
                print(lim1, lim2, type(lim1), type(lim2))
                mycursor2.execute("select Month, Category_Name, Amount from monthlyexpense, admin, category where admin.Userid = monthlyexpense.Userid and monthlyexpense.idCategory = category.idCategory and monthlyexpense.Userid = %s limit %s,%s" % (u, lim1, lim2))
                op2 = mycursor2.fetchall()
                print(op2)
                op1=op2[:]
            mydb1.commit()
            m2=op1[0][0]
            cat=dict()
            for i in op1:
                cat[i[1]]=i[2]
            l1=[] #latest month
            l2=[] #fetched one month
            graphx=[]
            print(cat)
            for i in final_dict:
                if i in cat:
                    l1.append(float(final_dict[i]))
                    l2.append(cat[i])
                    graphx.append(i)
                else:
                    l1.append(float(final_dict[i]))
                    l2.append(0)
                    graphx.append(i)
            print(l1,l2,graphx)

            barWidth=0.25
            fig1,ax= plt.subplots(1)
            br1 = np.arange(len(l1))
            br2 = [x + barWidth for x in br1]

            sum1=sum2=0
            for i in l1:
                sum1=sum1+i
            for i in l2:
                sum2=sum2+i
            plt.title("Expense Analysis for the month" + m2 + m +" "+str(x.year))
            rects1=plt.bar(br2,l2, color='r', width=barWidth,edgecolor='brown',label=m2) # returns containers with all the bars
            rects2=plt.bar(br1,l1, color='g', width=barWidth,edgecolor='brown',label=m)
            plt.xlabel('Expense Category', fontweight='bold')
            plt.ylabel('Amount (in Rs)', fontweight='bold')
            plt.legend([m2, m], loc='upper left')
            plt.xticks([r + barWidth for r in range(len(l1))],graphx)
            plt.xticks(rotation=30, horizontalalignment="center")
            for rect in rects1:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height), #position where annotation begins
                            xytext=(0, 3),  # 3 points vertical offset,position where text is placed
                            textcoords="offset points",#offest given in points and not in pixels
                            ha='center', va='bottom')
            for rect in rects2:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')
            fig1.tight_layout()
            fig1.show()


            #Graph2

            names=[]
            values=[]
            fig2=plt.figure(2)
            names.append(m2)
            names.append(m)
            values.append(sum2)
            values.append(sum1)
            plt.subplot(132)
            plt.scatter(names, values)
            plt.suptitle('Month-wise Plotting')
            fig2.show()





