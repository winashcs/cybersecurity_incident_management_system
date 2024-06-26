from tkinter import* # for creating graphic user interface
from tkinter import ttk  # (themed tk) we use ttk for modern widgets like buttons, labels, and other GUI elements
from PIL import Image,ImageTk # helps for image processing in gui
from tkcalendar import Calendar # for date

class CC: #i used CC here because CyberCrime will be a long keyword
    def __init__(self,root):
        self.root=root
        self.root.geometry('1366x768+0+0')
        self.root.title('Cybersecurity Incident Management System') 
        self.root.iconbitmap('images/icon.ico')
        
        title=Label(self.root,text='Cybersecurity Incident Management System',font=('Brush Script MT',45,'bold'),bg='#006400',fg='#F5F5DC')
        title.place(x=0,y=0,width=1366,height=70)
        
        logo1_open=Image.open('images/logo.png')
        logo1_open=logo1_open.resize((100,65), Image.LANCZOS)
        self.image_logo1=ImageTk.PhotoImage(logo1_open)
        self.logo1=Label(self.root,image=self.image_logo1)
        self.logo1.place(x=123,y=3,width=100,height=65)
        
        logo2_open=Image.open('images/logo.png')
        logo2_open=logo2_open.resize((100,65), Image.LANCZOS)
        self.image_logo2=ImageTk.PhotoImage(logo2_open)
        self.logo2=Label(self.root,image=self.image_logo2)
        self.logo2.place(x=1143,y=3,width=100,height=65)
        
        frame1=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        frame1.place(x=0,y=70,width=1366,height=130)
        
        i1=Image.open('images/i1.jpg')
        i1=i1.resize((455,130), Image.LANCZOS)
        self.i11=ImageTk.PhotoImage(i1)
        self.i111=Label(frame1,image=self.i11)
        self.i111.place(x=0,y=0,width=455,height=130)
        
        i2=Image.open('images/i3.jpg')
        i2=i2.resize((455,130), Image.LANCZOS)
        self.i22=ImageTk.PhotoImage(i2)
        self.i222=Label(frame1,image=self.i22)
        self.i222.place(x=455,y=0,width=455,height=130)
        
        i3=Image.open('images/i1.jpg')
        i3=i3.resize((455,130), Image.LANCZOS)
        self.i33=ImageTk.PhotoImage(i3)
        self.i333=Label(frame1,image=self.i33)
        self.i333.place(x=910,y=0,width=455,height=130)
        
        frame2=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        frame2.place(x=10,y=200,width=1336,height=495)
        
        frame2_1=LabelFrame(frame2,bd=2,relief=RIDGE,text='Cybersecurity Alerts',font=("Garamond",15,'bold'),fg='dark green',bg='white')
        frame2_1.place(x=10,y=10,width=1316,height=238)
        
        b1=Label(frame2_1,text='Case ID :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b1.grid(row=0,column=0,padx=2,sticky=W,pady=2)
        b11=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b11.grid(row=0,column=1,padx=2,sticky=W,pady=2)
        
        b2=Label(frame2_1,text='Victim Name :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b2.grid(row=1,column=0,padx=2,sticky=W,pady=2)
        b22=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b22.grid(row=1,column=1,padx=2,sticky=W,pady=2)
        
        b3=Label(frame2_1,text='Victim Gender :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b3.grid(row=2,column=0,padx=2,sticky=W,pady=2)
        victim_gender = StringVar()
        b33_male = ttk.Radiobutton(frame2_1, text='Male', variable=victim_gender, value='Male', style='TRadiobutton')
        b33_male.grid(row=2, column=1, padx=5, sticky=W)
        b33_female = ttk.Radiobutton(frame2_1, text='Female', variable=victim_gender, value='Female', style='TRadiobutton')
        b33_female.grid(row=2, column=1, padx=65, sticky=W)
        
        b4=Label(frame2_1,text='Victim Details :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b4.grid(row=3,column=0,padx=2,sticky=W,pady=2)
        b44=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b44.grid(row=3,column=1,padx=2,sticky=W,pady=2)
        
        b5=Label(frame2_1,text='Date of incident :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b5.grid(row=4,column=0,padx=2,sticky=W,pady=2)
        def show_calendar(event):
            top = Toplevel(root)
            top.iconbitmap('images/icon.ico')
            cal = Calendar(top, selectmode='day', year=2023, month=1, day=1)
            cal.pack(fill='both', expand=True)            
            def select_date():
                selected_date = cal.get_date()
                b55.delete(0, END)
                b55.insert(0, selected_date)
                top.destroy()            
            ok_button = ttk.Button(top, text="OK", command=select_date)
            ok_button.pack(pady=10)        
        b55 = ttk.Entry(frame2_1, width=20, font=("Times New Roman", 10, 'bold'))
        b55.grid(row=4, column=1, padx=2, sticky=W, pady=2)
        b55.bind('<Button-1>', show_calendar)
        
        b6=Label(frame2_1,text='Type of cybercrime :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b6.grid(row=0,column=2,padx=2,sticky=W,pady=2)
        b66=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b66.grid(row=0,column=3,padx=2,sticky=W,pady=2)
        
        b7=Label(frame2_1,text='Type of cyberattack :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b7.grid(row=1,column=2,padx=2,sticky=W,pady=2)
        b77=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b77.grid(row=1,column=3,padx=2,sticky=W,pady=2)
        
        b8=Label(frame2_1,text='Impact Assessment :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b8.grid(row=2,column=2,padx=2,sticky=W,pady=2)
        b88=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b88.grid(row=2,column=3,padx=2,sticky=W,pady=2)
        
        b9=Label(frame2_1,text='IP address :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b9.grid(row=3,column=2,padx=2,sticky=W,pady=2)
        b99=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b99.grid(row=3,column=3,padx=2,sticky=W,pady=2)
        
        b10=Label(frame2_1,text='Device Information :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b10.grid(row=4,column=2,padx=2,sticky=W,pady=2)
        b1010=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b1010.grid(row=4,column=3,padx=2,sticky=W,pady=2)
        
        b11=Label(frame2_1,text='Related Incident :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b11.grid(row=0,column=4,padx=2,sticky=W,pady=2)
        b1111=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b1111.grid(row=0,column=5,padx=2,sticky=W,pady=2)
        
        b12=Label(frame2_1,text='Suspect Name :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b12.grid(row=1,column=4,padx=2,sticky=W,pady=2)
        b1212=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b1212.grid(row=1,column=5,padx=2,sticky=W,pady=2)
        
        b13=Label(frame2_1,text='Suspect Gender :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b13.grid(row=2,column=4,padx=2,sticky=W,pady=2)
        suspect_gender = StringVar()
        b1313_male = ttk.Radiobutton(frame2_1, text='Male', variable=suspect_gender, value='Male', style='TRadiobutton')
        b1313_male.grid(row=2, column=5, padx=5, sticky=W)
        b1313_female = ttk.Radiobutton(frame2_1, text='Female', variable=suspect_gender, value='Female', style='TRadiobutton')
        b1313_female.grid(row=2, column=5, padx=65, sticky=W)
        
        b14=Label(frame2_1,text='Suspect Details :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b14.grid(row=3,column=4,padx=2,sticky=W,pady=2)
        b1414=ttk.Entry(frame2_1,width=20,font=("Times New Roman",10,'bold'))
        b1414.grid(row=3,column=5,padx=2,sticky=W,pady=2)
        
        b15=Label(frame2_1,text='Status :',font=("Ebrima",10,'bold'),fg='black',bg='white')
        b15.grid(row=4,column=4,padx=2,sticky=W,pady=2)
        selected = StringVar(frame2_1)
        selected.set("SELECT ▼")
        b1515 = OptionMenu(frame2_1, selected,"ONGOING", "CLOSED", "PENDING")
        b1515.configure(font=("Arial", 8,'bold'), bg='white',highlightthickness=1, highlightbackground='grey',activebackground='white',indicatoron=0)
        b1515['menu'].configure(font=("Times New Roman", 10, 'bold'), bg='white')
        b1515.grid(row=4, column=5, padx=2, pady=2, sticky=W)
        
        bf=Frame(frame2_1,bd=2,relief=RIDGE,bg='white')
        bf.place(x=3,y=150,width=613,height=45)
        
        bt1=Button(bf,text='SAVE',font=("Comic Sans MS", 10, 'bold'),bg='#fee01c',width=17,fg='black')
        bt1.grid(row=0,column=0,padx=3,pady=3)
        bt2=Button(bf,text='UPDATE',font=("Comic Sans MS", 10, 'bold'),bg='#fee01c',width=17,fg='black')
        bt2.grid(row=0,column=1,padx=3,pady=3)
        bt3=Button(bf,text='DELETE',font=("Comic Sans MS", 10, 'bold'),bg='#fee01c',width=17,fg='black')
        bt3.grid(row=0,column=2,padx=3,pady=3)
        bt4=Button(bf,text='CLEAR',font=("Comic Sans MS", 10, 'bold'),bg='#fee01c',width=17,fg='black')
        bt4.grid(row=0,column=3,padx=3,pady=3)
        
        i4=Image.open('images/i2.jpg')
        i4=i4.resize((437,222), Image.LANCZOS)
        self.i44=ImageTk.PhotoImage(i4)
        self.i444=Label(frame2_1,image=self.i44)
        self.i444.place(x=875,y=-10,width=437,height=222)
        
        frame2_2=LabelFrame(frame2,bd=2,relief=RIDGE,text='Cybersecurity Alert Dashboard',font=("Garamond",15,'bold'),fg='dark green',bg='white')
        frame2_2.place(x=10,y=248,width=1316,height=238)
        
        frame2_2_1=LabelFrame(frame2_2,bd=2,relief=RIDGE,text='Search Record',font=("Lucida Sans Unicode",10,'bold'),fg='black',bg='white')
        frame2_2_1.place(x=0,y=0,width=1306,height=50)

if __name__=="__main__":
    root=Tk()
    obj=CC(root)
    root.mainloop()
