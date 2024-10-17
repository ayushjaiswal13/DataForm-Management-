from tkinter import*
from PIL import ImageTk,Image 
from tkinter import messagebox
from tkinter import ttk
import mysql.connector as sqltr
import time
doc=open("iithpswd.txt","a+")
doc.seek(0)
x=doc.readlines()
if len(x)==0:
    print("HELO!! USER, WELCOME TO THE PROGRAM")
    print("PLEASE PROVIDE SOME DETAILS BEFORE MOVING FORWARD...")
    uname=input("ENTER YOUR FULL NAME:")
    doc.write(uname)
    doc.write("\n")
    mpswd=input("PLEASE ENTER YOUR MYSQL PASSWORD:")
    doc.write(mpswd)
    print("THANK YOU")
    print("(CHECK FOR THE WINDOW IN BACKGROUND)")
    doc.close()
else:
    doc.seek(0)
    l=doc.readlines()
    uname=l[0]
    mpswd=l[1]
    doc.close()

def mainwc():
    updb=sqltr.connect(host="localhost",user="root",password=mpswd)
    if updb.is_connected():
        print("BRAVO!! YOU HAVE BEEN SUCCESSFULLY CONNECTED TO MYSQL DATABASE.")
    else:
        print("WE FEEL EXTREMELY SORRY TO TELL YOU THAT WE FACED SOME PROBLEM IN CONNECTING YOU WITH MYSQL DATABASE.")
        print("WE REQUEST YOU TO TRY CONNECTING AGAIN")
        return
    usor=updb.cursor()
    usor.execute("create database if not exists upsc")
    usor.execute("use upsc")
    usor.execute("create table if not exists candidate_info(CANDIDATE_NAME VARCHAR(30), USERNAME VARCHAR(30), EMAIL_ID VARCHAR(50), PASSWORD VARCHAR(20))")
    usor.execute("create table if not exists pdetail(FATHER_NAME VARCHAR(50),MOTHER_NAME VARCHAR(50),DOB VARCHAR(20),GENDER CHAR(2),CATEGORY CHAR(7),PHONE_NO VARCHAR(10),USERNAME VARCHAR(30))") ,
    usor.execute("create table if not exists adrsdetail(ADDRESS VARCHAR(50), CITY CHAR(20), STATE CHAR(20), PINCODE VARCHAR(7),USERNAME VARCHAR(30))")
    usor.execute("create table if not exists acdmdetail(X_PERCENTAGE VARCHAR(2),XII_PERCENTAGE VARCHAR(2),GRADUATION VARCHAR(15),GRADUATION_PERCENTAGE VARCHAR(2),POST_GRADUATE CHAR(3),USERNAME VARCHAR(30))")

    #=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=    
    #UPSC Registration System
    global ty,image8,crtrs,image7,bg,image1,union,image2,upscer,image3,apsmatr,image4,wlcm,image14
    page=Toplevel() 
    page.geometry("1400x800")
    page.attributes("-fullscreen", True)
    
    page.bind("<F11>", lambda event: page.attributes("-fullscreen",not page.attributes("-fullscreen")))
    page.bind("<Escape>", lambda event: page.attributes("-fullscreen", False))
    page.configure(bg='gray5')
    page.title("---Data collection Form---")

    Label(page,text="DATA FORM MANAGEMENT SYSTEM",width="35",bg='gray5',fg='antique white',font=("Avengero",25)).place(x=350,y=20)
    Label(page,text="IIT HYDERABAD",width="35",bg='gray5',fg='antique white',font=("Avengero",37)).place(x=300,y=90)
    #Label(page,text="''Every morning we are born again. What we do today is what matters most!!''",width="90",fg='antique white',bg='gray5',font=("a Anti Corona",16)).place(x=130,y=220)

    publc=Image.open('upsc.PNG')
    image2=publc.resize((840,550),Image.Resampling.LANCZOS)
    union=ImageTk.PhotoImage(image2)
    picture1=Label(page,image=union).place(x=530,y=270)
    
    apsmat=Image.open('iithlogo.PNG')
    image4=apsmat.resize((450,150),Image.Resampling.LANCZOS)
    apsmatr=ImageTk.PhotoImage(image4)
    picture4=Label(page,bg='gray5',image=apsmatr).place(x=1070,y=1)
    
    upsceer=Image.open('natemb.PNG')
    image3=upsceer.resize((190,250),Image.Resampling.LANCZOS)
    upscer=ImageTk.PhotoImage(image3)
    picture3=Label(page,bg='gray5',image=upscer).place(x=10,y=0)
    
    crtrs=Image.open('crtrs.PNG')
    image7=crtrs.resize((210,149),Image.Resampling.LANCZOS)
    crtrs=ImageTk.PhotoImage(image7)
    picture7=Label(page,bg='gray5',image=crtrs).place(x=115,y=610)
    
    ty=Image.open('ty.PNG')
    image8=ty.resize((153,48),Image.Resampling.LANCZOS)
    ty=ImageTk.PhotoImage(image8)
    picture8=Label(page,bg='gray5',image=ty).place(x=140,y=545)
    
    
    def closesystem():
        exit()
#------------------------------------------------------------------------------------------------------------
    #REGISTRATION SYSTEM
        
    def reg1():
        page11=Tk()
        page11.geometry("1400x800")
        page11.configure(bg='gray5')
        page11.title("SUBMIT YOUR INFORMATION")

        #LABELS AND ENTRIES FOR REGISTRATION WINDOW
        
        Label(page11,text="PERSONAL INFORMATION",width="25",bg='gray5',fg='sky blue',font=("a Anti Corona",19,"bold","underline")).place(x=40,y=20)
        Label(page11,text="CANDIDATE'S NAME :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",14)).place(x=50,y=70)
        CandidateName=Entry(page11,bd=3)
        CandidateName.place(x=300,y=70)
        Label(page11,text="DATE OF BIRTH :",bg='gray5',fg='antique white',width="25",font=("a Anti Corona",14)).place(x=42,y=120)
        DOB=Entry(page11,bd=3)
        DOB.place(x=300,y=120)
        Label(page11,text="GENDER :",bg='gray5',fg='antique white',width="20",font=("a Anti Corona",14)).place(x=60,y=170)
        gndr=StringVar()
        Gender=ttk.Combobox(page11,width=18,textvariable=gndr)
        Gender['values']=('--CHOOSE--','M','F')
        Gender.place(x=300,y=170)
        Gender.current(0)
        Label(page11,text="CATEGORY  :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",14)).place(x=38,y=220)
        ctgry=StringVar()
        Category=ttk.Combobox(page11,width=18,textvariable=ctgry)
        Category['values']=('--CHOOSE--','GENRAL','OBC','SC/ST')
        Category.place(x=300,y=220)
        Category.current(0)
        Label(page11,text="FATHER'S NAME :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",14)).place(x=45,y=270)
        FatherName=Entry(page11,bd=3)
        FatherName.place(x=300,y=270)
        Label(page11,text="MOTHER'S NAME :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",14)).place(x=45,y=320)
        MotherName=Entry(page11,bd=3)
        MotherName.place(x=300,y=320)
        Label(page11,text="PHONE NO. :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",14)).place(x=45,y=370)
        PhoneNo=Entry(page11,bd=3)
        PhoneNo.place(x=300,y=370)
        Label(page11,text="EMAIL ID :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",14)).place(x=45,y=420)
        EmailID=Entry(page11,bd=3)
        EmailID.place(x=300,y=420)
        Label(page11,text="ADDRESS :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",14)).place(x=45,y=470)
        Address=Entry(page11,bd=3)
        Address.place(x=300,y=470)
        Label(page11,text="CITY :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",14)).place(x=45,y=520)
        City=Entry(page11,bd=3)
        City.place(x=300,y=520)
        Label(page11,text="STATE :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",14)).place(x=45,y=570)
        State=Entry(page11,bd=3)
        State.place(x=300,y=570)
        Label(page11,text="PIN CODE :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",14)).place(x=45,y=620)
        PinCode=Entry(page11,bd=3)
        PinCode.place(x=300,y=620)
        Label(page11,text="ACADEMIC INFORMATION",width="25",bg='gray5',fg='sky blue',font=("a Anti Corona",19,"bold","underline")).place(x=750,y=20)
        Label(page11,text="(ALL PERCENTAGES TO BE FILLED IN ROUND FIGURES)",width="60",bg='gray5',fg='antique white',font=("a Anti Corona",8)).place(x=755,y=51)
        Label(page11,text=" X PERCENTAGE :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",14)).place(x=750,y=80)
        XPercentage=Entry(page11,bd=3)
        XPercentage.place(x=1000,y=80)
        Label(page11,text="XII PERCENTAGE :",bg='gray5',fg='antique white',width="25",font=("a Anti Corona",14)).place(x=750,y=130)
        XIIPercentage=Entry(page11,bd=3)
        XIIPercentage.place(x=1000,y=130)
        Label(page11,text="GRADUATED WITH :",bg='gray5',fg='antique white',width="20",font=("a Anti Corona",14)).place(x=760,y=180)
        Graduation=Entry(page11,bd=3)
        Graduation.place(x=1000,y=180)
        Label(page11,text="GRADUATE % :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",14)).place(x=750,y=230)
        GPercentage=Entry(page11,bd=3)
        GPercentage.place(x=1000,y=230)
        Label(page11,text="POST GRADUATE (if any) :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",14)).place(x=720,y=280)
        pg=StringVar()
        Pgraduate=ttk.Combobox(page11,width=18,textvariable=pg)
        Pgraduate['values']=('--CHOOSE--','YES','NO')
        Pgraduate.place(x=1000,y=280)
        Pgraduate.current(0)
        Label(page11,text="USERNAME :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",14)).place(x=750,y=380)
        Username=Entry(page11,bd=3)
        Username.place(x=1000,y=380)
        Label(page11,text="PASSWORD :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",14)).place(x=750,y=420)
        Password=Entry(page11,bd=3,show='*')
        Password.place(x=1000,y=420)
        Label(page11,text="CONFIRM PASSWORD :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",14)).place(x=720,y=460)
        Cpassword=Entry(page11,bd=3,show='*')
        Cpassword.place(x=1000,y=460)
        CandidateName.focus()
        def changepnt1(event):
            DOB.focus()
        CandidateName.bind('<Return>',changepnt1)
        def changepnt2(event):
            Gender.focus()
        DOB.bind('<Return>',changepnt2)
        def changepnt3(event):
            Category.focus()
        Gender.bind('<Return>',changepnt3)
        def changepnt4(event):
            FatherName.focus()
        Category.bind('<Return>',changepnt4)
        def changepnt5(event):
            MotherName.focus()
        FatherName.bind('<Return>',changepnt5)
        def changepnt6(event):
            PhoneNo.focus()
        MotherName.bind('<Return>',changepnt6)
        def changepnt7(event):
            EmailID.focus()
        PhoneNo.bind('<Return>',changepnt7)
        def changepnt8(event):
            Address.focus()
        EmailID.bind('<Return>',changepnt8)
        def changepnt9(event):
            City.focus()
        Address.bind('<Return>',changepnt9)
        def changepnt10(event):
            State.focus()
        City.bind('<Return>',changepnt10)
        def changepnt11(event):
            PinCode.focus()
        State.bind('<Return>',changepnt11)
        def changepnt12(event):
            XPercentage.focus()
        PinCode.bind('<Return>',changepnt12)
        def changepnt13(event):
            XIIPercentage.focus()
        XPercentage.bind('<Return>',changepnt13)
        def changepnt14(event):
            Graduation.focus()
        XIIPercentage.bind('<Return>',changepnt14)
        def changepnt15(event):
            GPercentage.focus()
        Graduation.bind('<Return>',changepnt15)
        def changepnt16(event):
            Pgraduate.focus()
        GPercentage.bind('<Return>',changepnt16)
        def changepnt17(event):
            Username.focus()
        Pgraduate.bind('<Return>',changepnt17)
        def changepnt18(event):
            Password.focus()
        Username.bind('<Return>',changepnt18)
        def changepnt19(event):
            Cpassword.focus()
        Password.bind('<Return>',changepnt19)

        def check(event):    
            if (CandidateName.get() and Username.get() and EmailID.get() and Password.get() and Cpassword.get() and DOB.get() and FatherName.get()
                and MotherName.get() and PhoneNo.get() and Address.get() and City.get() and State.get() and PinCode.get() and XPercentage.get()
                and XIIPercentage.get() and Graduation.get() and GPercentage.get()):
                usor.execute('select USERNAME, EMAIL_ID from candidate_info')
                total=usor.fetchall()
                username=[]
                exist_emailid=[]
                prcntg=[]
                for j in range(1,101):
                    a=j
                    prcntg.append(a)
                for i in total:
                    username.append(i[0])
                    exist_emailid.append(i[1])
                if Username.get() in username:
                    messagebox.showwarning("ALERT","USERNAME ENTERED ALREADY EXISTS")
                    Username.delete(0,END)
                elif EmailID.get() in exist_emailid:
                    messagebox.showwarning("ALERT","EMAIL ID ENTERED ALREADY EXISTS")
                    EmailID.delete(0,END)
                elif Password.get()!=Cpassword.get():
                    messagebox.showwarning("ALERT","PASSWORD DID NOT MATCH")
                    Cpassword.delete(0,END)
                elif Gender.get() not in ['M','F']:
                    messagebox.showwarning("ALERT","PLEASE SELECT GENDER FROM GIVEN CHOICES")
                    Gender.delete(0,END)
                elif Category.get() not in ['GENRAL','OBC','SC/ST']:
                    messagebox.showwarning("ALERT","PLEASE SELECT CATEGORY FROM GIVEN CHOICES")
                    Category.delete(0,END)
                elif Pgraduate.get() not in ['YES','NO']:
                    messagebox.showwarning("ALERT","PLEASE SELECT POST GRADUATE FROM GIVEN CHOICES")
                    Pgraduate.delete(0,END)
                elif len(PhoneNo.get())!=10:
                    messagebox.showerror("ALERT","INVALID PHONE NUMBER ENTERED")
                    PhoneNo.delete(0,END)
                elif len(PinCode.get())!=6:
                    messagebox.showerror("ALERT","INVALID PIN CODE ENTERED")
                    PinCode.delete(0,END)
                elif float(XPercentage.get()) not in prcntg:
                    messagebox.showerror("REGISTRATION DENIED","X PERCENTAGE INAPPROPRIATE")
                    XPercentage.delete(0,END)
                elif float(XIIPercentage.get()) not in prcntg:
                    messagebox.showerror("REGISTRATION DENIED","XII PERCENTAGE INAPPROPRIATE")
                    XIIPercentage.delete(0,END)
                elif float(GPercentage.get()) not in prcntg:
                    messagebox.showerror("REGISTRATION DENIED","GRADUATION PERCENTAGE INAPPROPRIATE")
                    GPercentage.delete(0,END)
                else:
                    usor.execute("insert into candidate_info values('{}','{}','{}','{}')".format(CandidateName.get(),Username.get(),EmailID.get(),Password.get()))
                    usor.execute("insert into pdetail values('{}','{}','{}','{}','{}','{}','{}')".format(FatherName.get(),MotherName.get(),DOB.get(),Gender.get(),Category.get(),PhoneNo.get(),Username.get()))
                    usor.execute("insert into adrsdetail values('{}','{}','{}','{}','{}')".format(Address.get(),City.get(),State.get(),PinCode.get(),Username.get()))
                    usor.execute("insert into acdmdetail values('{}','{}','{}','{}','{}','{}')".format(XPercentage.get(),XIIPercentage.get(),Graduation.get(),GPercentage.get(),Pgraduate.get(),Username.get()))
                    updb.commit()
                    page11.destroy()
                    messagebox.showinfo("INFORMATION","REGISTRATION SUCCESSFULL")
                              
            else:
                messagebox.showwarning("ALERT","ALL ENTRIES MUST BE FILLED")
        Button(page11,text="SUBMIT",bg='gray5',fg='antique white',width=7,height=1,font=("a Absolute Empire",16,"italic","bold"),command=lambda:check(None)).place(x=860,y=500)
        Cpassword.bind('<Return>',check)
            
    #=========================================================================================================================================================
        
    #LOGIN SYSTEM
        
    def reg2():
        global t1,t2,UserName,PassWord
        page2=Toplevel()
        page2.geometry("400x400")
        page2.configure(bg='gray5')
        page2.title("LOGIN WINDOW")
        
        def f2():
            global page3
            page2.destroy()
            page3=Toplevel()
            page3.geometry("1400x800")
            page3.configure(bg='gray5')
            page3.title("LOGIN SUCESSFULL")
            Label(page3,text="YOUR INFORMATION",width="25",bg='gray5',fg='sky blue',font=("a Anti Corona",19,"bold","underline")).pack(padx=5,pady=10)
            Label(page3,text="PERSONAL INFORMATION",width="25",bg='gray5',fg='sky blue',font=("a Anti Corona",19,"bold","italic","underline")).place(x=40,y=50)
            Label(page3,text="ACADEMIC INFORMATION",width="25",bg='gray5',fg='sky blue',font=("a Anti Corona",19,"bold","italic","underline")).place(x=770,y=50)
            
            usor.execute("select * from candidate_info where username='{}'".format(t1.get()))
            data=usor.fetchall()
            usor.execute("select * from pdetail where username='{}'".format(t1.get()))
            data1=usor.fetchall()
            usor.execute("select * from adrsdetail where username='{}'".format(t1.get()))
            data2=usor.fetchall()
            usor.execute("select * from acdmdetail where username='{}'".format(t1.get()))
            data3=usor.fetchall()
            
            Label(page3,text="CANDIDATE'S NAME :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",13)).place(x=45,y=90)
            Label(page3,text=data[0][0],width="20",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=250,y=90)
            Label(page3,text="DATE OF BIRTH    :",bg='gray5',fg='antique white',width="25",font=("a Anti Corona",13)).place(x=45,y=140)
            Label(page3,text=data1[0][2],width="20",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=250,y=140)
            Label(page3,text="FATHER'S NAME    :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",13)).place(x=45,y=190)
            Label(page3,text=data1[0][0],width="20",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=250,y=190)
            Label(page3,text="MOTHER'S NAME    :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",13)).place(x=45,y=240)
            Label(page3,text=data1[0][1],width="20",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=250,y=240)
            Label(page3,text="PHONE NO.  :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",13)).place(x=45,y=290)
            Label(page3,text=data1[0][5],width="20",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=250,y=290)
            Label(page3,text="GENDER     :",bg='gray5',fg='antique white',width="20",font=("a Anti Corona",13)).place(x=65,y=340)
            Label(page3,text=data1[0][3],width="20",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=250,y=340)
            Label(page3,text="CATEGORY   :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",13)).place(x=45,y=390)
            Label(page3,text=data1[0][4],width="20",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=250,y=390)
            Label(page3,text="EMAIL ID   :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",13)).place(x=45,y=440)
            Label(page3,text=data[0][2],width="20",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=250,y=440)
            Label(page3,text="ADDRESS    :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",13)).place(x=45,y=490)
            Label(page3,text=data2[0][0],width="20",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=250,y=490)
            Label(page3,text="CITY       :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",13)).place(x=55,y=540)
            Label(page3,text=data2[0][1],width="20",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=250,y=540)
            Label(page3,text="STATE      :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",13)).place(x=53,y=590)
            Label(page3,text=data2[0][2],width="20",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=250,y=590)
            Label(page3,text="PIN CODE   :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",13)).place(x=45,y=640)
            Label(page3,text=data2[0][3],width="20",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=250,y=640)
            Label(page3,text="X PERCENTAGE :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",13)).place(x=750,y=100)
            Label(page3,text=data3[0][0],width="6",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=950,y=100)
            Label(page3,text="XII PERCENTAGE :",bg='gray5',fg='antique white',width="25",font=("a Anti Corona",13)).place(x=750,y=150)
            Label(page3,text=data3[0][1],width="6",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=950,y=150)
            Label(page3,text="GRADUATED WITH :",bg='gray5',fg='antique white',width="20",font=("a Anti Corona",13)).place(x=760,y=200)
            Label(page3,text=data3[0][2],width="15",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=920,y=200)
            Label(page3,text="GRADUATE % :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",13)).place(x=750,y=250)
            Label(page3,text=data3[0][3],width="6",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=950,y=250)
            Label(page3,text="POST GRADUATE (if any) :",width="25",bg='gray5',fg='antique white',font=("a Anti Corona",13)).place(x=720,y=300)
            Label(page3,text=data3[0][4],width="6",bg='gray5',fg='khaki1',font=("a Anti Corona",13)).place(x=950,y=300) 
            global lgot,image13
            lgot=Image.open('logut.PNG')
            image13=lgot.resize((115,54),Image.Resampling.LANCZOS)
            lgot=ImageTk.PhotoImage(image13)
            picture13=Button(page3,image=lgot,activebackground='gray5',bg='gray5',bd=0,command=distry).place(x=850,y=550)
               
        def submitt(event):
            usor.execute('select USERNAME, PASSWORD from candidate_info')
            total=usor.fetchall()
            username=t1.get()
            password=t2.get()
            for i in total:
                if username== i[0] and password== i[1]:
                    return f2()
                elif username==i[0] and password!=i[1]:
                    messagebox.showerror('ALERT!!','PLEASE ENTER CORRECT PASSWORD')
                    PassWord.delete(0,END)
                    break
            else:
                messagebox.showerror('INFORMATION','NO SUCH REGISTRATION HAS BEEN MADE BY USER')
                UserName.delete(0,END)
                PassWord.delete(0,END)

        def distry():
            page3.destroy()
            messagebox.showinfo('INFORMATION','LOGGED OUT SUCCESSFULLY')
       
        def changepnt(event):
            PassWord.focus()    
        t1=StringVar()
        t2=StringVar()
        UserName=Entry(page2,bd=3,textvariable=t1)
        UserName.place(x=170,y=120)
        PassWord=Entry(page2,bd=3,show='*',textvariable=t2)
        PassWord.place(x=170,y=180)
        global lgp,urnam,paswdd,smt,image9,image11,image10,image12
        
        lgp=Image.open('lgp.PNG')
        image9=lgp.resize((390,60),Image.Resampling.LANCZOS)
        lgp=ImageTk.PhotoImage(image9)
        picture9=Label(page2,bg='gray5',image=lgp).place(x=2,y=10)
        
        urnam=Image.open('usrnm.PNG')
        image10=urnam.resize((107,31),Image.Resampling.LANCZOS)
        urnam=ImageTk.PhotoImage(image10)
        picture10=Label(page2,bg='gray5',image=urnam).place(x=40,y=115)
        
        paswdd=Image.open('pwdd.PNG')
        image11=paswdd.resize((107,31),Image.Resampling.LANCZOS)
        paswdd=ImageTk.PhotoImage(image11)
        picture11=Label(page2,bg='gray5',image=paswdd).place(x=40,y=175)
        
        smt=Image.open('submt.PNG')
        image12=smt.resize((145,56),Image.Resampling.LANCZOS)
        smt=ImageTk.PhotoImage(image12)
        picture12=Button(page2,bg='gray5',activebackground='gray5',image=smt,bd=0,command= lambda: submitt(None)).place(x=120,y=270)
        UserName.bind('<Return>',changepnt)
        PassWord.bind('<Return>',submitt)
        
#=================================================================================================================================================
    #DISPLAY REGISTRATION SYSTEM
    def reg3():
        page14=Tk()
        page14.geometry("1380x780")            
        page14.configure(bg='gray5')
        page14.title("DISPLAYING REGISTRATIONS...")
        usor.execute("select count(*) from CANDIDATE_INFO")
        n=usor.fetchone()
        usor.execute("select CANDIDATE_NAME, USERNAME, EMAIL_ID from CANDIDATE_INFO")
        Label(page14,text="CANDIDATE NAME",width="20",bg='gray5',fg='sky blue',font=("a Absolute Empire",20,"italic")).grid(row=0,column=0)
        Label(page14,text="USERNAME",width="20",bg='gray5',fg='sky blue',font=("a Absolute Empire",20,"italic")).grid(row=0,column=1)
        Label(page14,text="EMAIL ID",width="20",bg='gray5',fg='sky blue',font=("a Absolute Empire",20,"italic")).grid(row=0,column=2) 
        if n[0]>0:
            for i in range(2,n[0]+2):
                res=usor.fetchone()
                for j in range(0,3):
                    Label(page14,text=res[j],bg='gray5',fg='antique white',width="25",font=("a Anti Corona",15,"italic")).grid(row=i+2,column=j)
        else:
            messagebox.showinfo("INFORMATION","NO REGISTRATIONS YET!!")

#=================================================================================================================================================
    #INSTRUCTIONS
    def reg4():
        page15=Tk()
        page15.geometry("1380x780")            
        page15.configure(bg='gray5')
        page15.title("INSTRUCTIONS...")
        Label(page15,text="INSTRUCTIONS",width="35",bg='gray5',fg='antique white',font=("Death Markers",50)).place(x=120,y=20)
        Label(page15,text="Please read the instructions carefully before you proceed to register.",width="90",fg='antique white',bg='gray5',font=("a Anti Corona",16)).place(x=130,y=120)

        global itrn,image15
        itrn=Image.open('insrtn.PNG')
        image15=itrn.resize((1067,600),Image.Resampling.LANCZOS)
        itrn=ImageTk.PhotoImage(image15)
        picture15=Label(page15,bg='gray5',image=itrn).place(x=50,y=10)
        
#================================================================================================================================================
    #BUTTONS OF HOME PAGE
    Button(page,text="REGISTER  YOUR  PROFILE",width=25,height=1,bg='gray5',fg='antique white',font=("a Absolute Empire",16,"italic","bold"),command=reg1).place(x=50,y=260)
    Button(page,text="LOGIN  TO  YOUR  PROFILE",width=25,height=1,bg='gray5',fg='antique white',font=("a Absolute Empire",16,"italic","bold"),command=reg2).place(x=50,y=315)
    Button(page,text="DISPLAY  REGISTRATIONS",width=25,height=1,bg='gray5',fg='antique white',font=("a Absolute Empire",16,"italic","bold"),command=reg3).place(x=50,y=370)
    Button(page,text="INSTRUCTIONS",width=25,height=1,bg='gray5',fg='antique white',font=("a Absolute Empire",16,"italic","bold"),command=reg4).place(x=50,y=425)
    Button(page,text="CLOSE  SYSTEM",width=25,height=1,bg='gray5',fg='antique white',font=("a Absolute Empire",16,"italic","bold"),command=closesystem).place(x=50,y=480)
    
ldng=Tk()
ldng.geometry("550x130")
ldng.title("LOADING...")
def correct():
    for x in range(100):
        prgl.config(text=prg['value'])
        prg['value']+=1
        time.sleep(0.02)
        percent.set(str(prg['value'])+"%    Loading Completed")
        ldng.update_idletasks()
    if prg['value']==100:
        mainwc()
        ldng.iconify()
percent=StringVar()
prgl=Label(ldng,text="Loading the program :)",fg='purple',font=("a Astro Space",20,"italic","bold"))
prgl.place(x=50,y=10)
prg=ttk.Progressbar(ldng,orient= HORIZONTAL, length = 300, mode = 'determinate',value=0)
prg.place(x=100,y=55)
prgl=Label(ldng,fg='gray5',font=("a Astro Space",20,"italic","bold"),textvariable=percent)
prgl.place(x=50,y=85)
correct()
correct()
