import tkinter as tk
from tkinter import PhotoImage
from tkinter import ttk 
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
import bcrypt 
from datetime import datetime,timedelta

def destroying_theird_window(theird_window):
    theird_window.destroy()
    login_window()
 
def login_window(first_window):
    first_window.destroy()
    
    second_window=tk.Tk()
    second_window.title("Internshp Vacancy Finder")
    second_window.configure(bg="white")
    second_window.geometry("2000x2000") 

    bg=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\si.jpg")
    bg_img = bg.resize((640, 655), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_img)
    labe1=tk.Label(second_window,image=bg_photo,bg="white")
    labe1.place(x=680,y=10)

    icon_image=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\lg.png")
    icon_photo=ImageTk.PhotoImage(icon_image)
    second_window.iconphoto(False,icon_photo)

    background_image=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\p.png")
    background_image=background_image.resize((180,180),Image.Resampling.LANCZOS)
    background_photo=ImageTk.PhotoImage(background_image)
    label2=tk.Label(second_window,image=background_photo,bg="white")
    label2.place(x=250,y=60)
    
    signin_label=tk.Label(second_window,bg="white",text="Sign In",font=("bold",30))
    signin_label.place(x=270,y=250)

    def on_enter(event):
        name=user_name.get()
        if name=="user name":
            user_name.delete(0,"end")
        
    def on_leave(event):
        name=user_name.get()
        if name=="":
            user_name.insert(0, "user name")

    user_name=tk.Entry(second_window,width=35,fg="black", bg="white",font=("bold",13))
    user_name.place(x=180,y=355)
    user_name.insert(0,"user name")

    user_name.bind("<FocusIn>",on_enter)
    user_name.bind("<FocusOut>",on_leave)

    frame=tk.Frame(second_window,width=319,height=2,bg="black").place(x=180,y=375)

    def on_enter2(event):
        code=user_password.get()
        if code =="password" :
             user_password.delete(0,"end")
    
        if code!= "password" or code!= "" :
            user_password.config (show="*")     

    def on_leave2(event):
        code=user_password.get()
        if code=="":
            user_password.insert(0, "password")
            user_password.config (show="")

    user_password=tk.Entry(second_window,width=35,fg="black", bg="white",font=("bold",13))
    user_password.place(x=180,y=400)
    user_password.insert(0,"password")

    user_password.bind("<FocusIn>",on_enter2)
    user_password.bind("<FocusOut>",on_leave2)

    frame1=tk.Frame(second_window,width=319,height=2,bg="black").place(x=180,y=420)
  
    registered_username=None

    def login_user(secon_window):

        
        global registered_username

        entered_username = user_name.get()
        entered_userpassword = user_password.get()

        registered_username=entered_username
        
        
        print(f"Entered username: {entered_username}")
        print(f"Entered password: {entered_userpassword}")

        if ( entered_username == "user name") or ( entered_userpassword == "password"):
            tk.messagebox.showerror("Entry Error", "Please enter your User Name and Password correctly!")
            return
            
        connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",  
        database="mydatabase"
        )
        print("Database connection successful!")  
       

        query = connection.cursor()
        query.execute("SELECT * FROM user WHERE name=%s ", (entered_username))
        result = query.fetchone()
        print(result)

        
        if result == None:
            tk.messagebox.showerror("invalid log in", "Please enter your User Name and Password correctly!")
               
        else:
            stored_hashed_password = result[8]
            print(stored_hashed_password)
        

            if bcrypt.checkpw(entered_userpassword.encode('utf-8'), stored_hashed_password.encode('utf-8')):  
                second_window.destroy()
                information_window()  
            else:
                tk.messagebox.showerror("Invalid Login", "Incorrect username or password!")
            

            query.close()
            connection.close()
            

    def touch_button2(event):
        event.widget["background"]="light blue"
        event.widget["foreground"]="black"
    def exit_button2(event):
        event.widget["background"]="#0096FF"
        event.widget["foreground"]="white"

    login_button=tk.Button(second_window,text="Login",bg="#0096FF",fg="white",width=28,font=("bold",15),command=lambda:login_user(second_window))
    login_button.place(x=180,y=450)
 
    login_button.bind("<Enter>",touch_button2)
    login_button.bind("<Leave>",exit_button2)

    new_label= tk.Label(second_window, width=20,bg="white", text="New Here?", font=("Helvetica", 20,"bold" ))
    new_label.place(x=75,y=540)

    signup_button=tk.Button(second_window,text="SING UP",bg="red",fg="white",width=28,font=("bold",14),command=lambda:singup_window(second_window))
    signup_button.place(x=180,y=600)

    def touch_button3(event):
        event.widget["background"]="green"
        event.widget["foreground"]="white"
 
    def exit_button3(event):
        event.widget["background"]="red"
        event.widget["foreground"]="white"

    signup_button.bind("<Enter>",touch_button3)
    signup_button.bind("<Leave>",exit_button3)

    second_window.mainloop()


def singup_window(second_window):
    
    second_window.destroy()
   
    theird_window=tk.Tk()
    theird_window.title("Internshp Vacancy Finder")
    theird_window.geometry("2000x2000")
    theird_window.configure(bg="white")

    background_image2=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\sup.png")
    background_image2=background_image2.resize((300,300),Image.Resampling.LANCZOS)
    background_photo2=ImageTk.PhotoImage(background_image2)
    labe20=tk.Label(theird_window,image=background_photo2,bg="white")
    labe20.place(x=860,y=100)
    
    icon_image=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\lg.png")
    icon_photo=ImageTk.PhotoImage(icon_image)
    theird_window.iconphoto(False,icon_photo)

    sentence_label = tk.Label(theird_window, text="Sign up and discover a great amount of", font=("bold", 20),bg="white")
    sentence_label.place(x=750, y=450)
    sentence_label2 = tk.Label(theird_window, text="New OPPORTUNITIES !", font=("bold", 20),bg="white") 
    sentence_label2.place(x=750, y=490)

    fname_label = tk.Label(theird_window, text="First Name :", font=("bold", 14),bg="white")
    fname_label.place(x=100, y=60)
    firstname_entry = tk.Entry(theird_window, font=("bold", 14), width=35,bg="light blue")
    firstname_entry.place(x=200, y=60)

    lname_label = tk.Label(theird_window, text="Last Name :", font=("bold", 14),bg="white")
    lname_label.place(x=100, y=120)
    lastname_entry = tk.Entry(theird_window, font=("bold", 14), width=35,bg="light blue")
    lastname_entry.place(x=200, y=120)

    age_label = tk.Label(theird_window, text="Age :", font=("bold", 14),bg="white")
    age_label.place(x=100, y=180)
    age_entry = tk.Entry(theird_window, font=("bold", 14), width=35,bg="light blue")
    age_entry.place(x=200, y=180)

    email_label = tk.Label(theird_window, text="Email :", font=("bold", 14),bg="white")
    email_label.place(x=100, y=240)
    email_entry = tk.Entry(theird_window, font=("bold", 14), width=35,bg="light blue")
    email_entry.place(x=200, y=240)

    tp_label = tk.Label(theird_window, text="Tp. number :", font=("bold", 14),bg="white")
    tp_label.place(x=100, y=300)
    telno_entry = tk.Entry(theird_window, font=("bold", 14), width=35,bg="light blue")
    telno_entry.place(x=200, y=300)

    gender_label = tk.Label(theird_window, text="Gender :", font=("bold", 14),bg="white")
    gender_label.place(x=100, y=360)
    gender_entry = tk.Entry(theird_window, font=("bold", 14), width=35,bg="light blue")
    gender_entry.place(x=200, y=360)

    position_label= tk.Label(theird_window, text="Position :", font=("bold", 14),bg="white")
    position_label.place(x=100, y=420)
    position_entry = tk.Entry(theird_window, font=("bold", 14), width=35,bg="light blue")
    position_entry.place(x=200, y=420)

    username_label = tk.Label(theird_window, text="User Name :", font=("bold", 14),bg="white")
    username_label.place(x=100, y=480)
    username_entry = tk.Entry(theird_window, font=("bold", 14), width=35,bg="light blue")
    username_entry.place(x=200, y=480)

    pw_label = tk.Label(theird_window, text="Password :", font=("bold", 14),bg="white")
    pw_label.place(x=100, y=540)
    password_entry = tk.Entry(theird_window, font=("bold", 14), width=35, show="*",bg="light blue")
    password_entry.place(x=200, y=540)

    
   
    def register(): 

      
        connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",  
        database="mydatabase")
    
        print("database connection successful")

        fname=firstname_entry.get()
        lname=lastname_entry.get()
        age=age_entry.get()
        email=email_entry.get()
        telno=telno_entry.get()
        gender=gender_entry.get()
        position=position_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        print(f"Registering username: {username}, password: {password}")

        
        if  fname == "" or lname == "" or age == " " or email == " " or telno == "" or gender == "" or position == ""  or  username == "" or password == "":
            tk.messagebox.showerror("Error", "All fields are required")

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        query = connection.cursor()
        query.execute("SELECT * FROM user WHERE name=%s", (username,))
        result = query.fetchall()
    
        if result:
            tk.messagebox.showerror("Error", "This username has already been taken")
            return
        else:
            query.execute("INSERT INTO user (first_name,last_name,age,email,telephone_number,gender,position,name,password) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s)",
            (fname,lname,age,email,telno,gender,position,username, hashed_password))
        connection.commit()  

        query.close()
        connection.close()
        
        theird_window.destroy()
        login_window()

   
    submit_button = tk.Button(theird_window, text="Submit", bg="green", fg="white", width=17, font=("bold", 14), command=register)
    submit_button.place(x=100, y=620)


    def touch_button4(event):
        event.widget["background"] = "blue"
        event.widget["foreground"] = "white"

    def exit_button4(event):
        event.widget["background"] = "green"
        event.widget["foreground"] = "white"
    
    submit_button.bind("<Enter>", touch_button4)
    submit_button.bind("<Leave>", exit_button4)

    back_button = tk.Button(theird_window, text="Back", bg="red", fg="white", width=17, font=("bold", 14), command=lambda:destroying_theird_window(theird_window))
    back_button.place(x=360, y=620)

    def touch_button5(event):
        event.widget["background"] = "black"
        event.widget["foreground"] = "white"

    def exit_button5(event):
        event.widget["background"] = "red"
        event.widget["foreground"] = "white"
        
    
    back_button.bind("<Enter>", touch_button5)
    back_button.bind("<Leave>", exit_button5)
    

    theird_window.mainloop()

def calling_infromation_window(fifth_window):
    fifth_window.destroy()
    information_window()


def calling_infromation_window2(sixth_window):
    sixth_window.destroy()
    information_window()

def calling_infromation_window3(seventh_window):
    seventh_window.destroy()
    information_window()    


def information_window():
    
    forth_window=tk.Tk()
    forth_window.title("Internshp Vacancy Finder")
    forth_window.geometry("2000x2000")
    forth_window.configure(bg="#000080")
    
    icon_image=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\lg.png")
    icon_photo=ImageTk.PhotoImage(icon_image)
    forth_window.iconphoto(False,icon_photo)
   
    frame2=tk.Frame(forth_window,width=385,height=650,bg="light blue").place(x=30,y=30)
    frame3=tk.Frame(forth_window,width=385,height=650,bg="light blue").place(x=480,y=30)
    frame4=tk.Frame(forth_window,width=385,height=650,bg="light blue").place(x=930,y=30)

    frame5=tk.Frame(forth_window,width=60,height=4,bg="blue").place(x=200,y=650)
    frame6=tk.Frame(forth_window,width=60,height=4,bg="blue").place(x=650,y=650)
    frame7=tk.Frame(forth_window,width=60,height=4,bg="blue").place(x=1100,y=650)

    background_image5=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\bg1.jpg")
    background_image5=background_image5.resize((300,300),Image.Resampling.LANCZOS)
    background_photo5=ImageTk.PhotoImage(background_image5)
    label=tk.Label( forth_window,image=background_photo5)
    label.place(x=70,y=65)
    
    background_image6=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\bg2.jfif")
    background_image6=background_image6.resize((300,300),Image.Resampling.LANCZOS)
    background_photo6=ImageTk.PhotoImage(background_image6)
    label2=tk.Label( forth_window,image=background_photo6)
    label2.place(x=520,y=65)

    background_image7=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\bg3.jfif")
    background_image7=background_image7.resize((300,300),Image.Resampling.LANCZOS)
    background_photo7=ImageTk.PhotoImage(background_image7)
    label3=tk.Label( forth_window,image=background_photo7,bg="white")
    label3.place(x=970,y=65)

    
    def touch_button6(event):
        event.widget["background"]="blue"
        event.widget["foreground"]="white"
    def exit_button6(event):
        event.widget["background"]="red"
        event.widget["foreground"]="white"
    FIV_label = tk.Label(forth_window, text="Find Internship Vacancies", font=("bold", 14),bg="light blue")
    FIV_label.place(x=55, y=450)
    Avacancy_button=tk.Button(forth_window,text="Available Vacancy",bg="red",fg="white",width=28,font=("bold",14),command=lambda:see_vacancy(forth_window))
    Avacancy_button.place(x=55,y=500)
    Avacancy_button.bind("<Enter>",touch_button6)
    Avacancy_button.bind("<Leave>",exit_button6)

    def touch_button7(event):
        event.widget["background"]="blue"
        event.widget["foreground"]="white"
    def exit_button7(event):
        event.widget["background"]="red"
        event.widget["foreground"]="white"
    OFAP_label = tk.Label(forth_window, text="Only for Authorized Parties", font=("bold", 14),bg="light blue")
    OFAP_label.place(x=510, y=450)
    OFAP_button=tk.Button(forth_window,text="Update Vacancy ",bg="red",fg="white",width=28,font=("bold",14),command=lambda:check_update(forth_window ))
    OFAP_button.place(x=510,y=500)
    OFAP_button.bind("<Enter>",touch_button7)
    OFAP_button.bind("<Leave>",exit_button7) 

    leave_button = tk.Button(forth_window, text="Exit", bg="blue", fg="white", width=28, font=("bold", 14), command=forth_window.destroy)
    leave_button.place(x=510, y=580)
    def touch_button(event):
        event.widget["background"]="red"
        event.widget["foreground"]="white"
    def exit_button(event):
        event.widget["background"]="blue"
        event.widget["foreground"]="white"
    leave_button.bind("<Enter>", touch_button) 
    leave_button.bind("<Leave>", exit_button)

    def touch_button8(event):
        event.widget["background"]="blue"
        event.widget["foreground"]="white"
    def exit_button8(event):
        event.widget["background"]="red"
        event.widget["foreground"]="white"
    dyourself_label = tk.Label(forth_window, text="Contact Us", font=("bold", 14),bg="light blue")
    dyourself_label.place(x=960, y=450)
    about_us_button=tk.Button(forth_window,text="About Us ",bg="red",fg="white",width=28,font=("bold",14),command=lambda:aboutus(forth_window))
    about_us_button.place(x=960,y=500)
    about_us_button.bind("<Enter>",touch_button8)
    about_us_button.bind("<Leave>",exit_button8)

    forth_window.mainloop()


def see_vacancy(forth_window):

    forth_window.destroy()

    fifth_window=tk.Tk()
    fifth_window.title("Internshp Vacancy Finder")
    fifth_window.geometry("2000x2000")
    fifth_window.configure(bg="white")
    
    icon_image=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\lg.png")
    icon_photo=ImageTk.PhotoImage(icon_image)
    fifth_window.iconphoto(False,icon_photo) 

    background_image3=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\telescope.png")
    background_image3=background_image3.resize((300,300),Image.Resampling.LANCZOS)
    background_photo3=ImageTk.PhotoImage(background_image3)
    labe23=tk.Label(fifth_window,image=background_photo3,bg="white")
    labe23.place(x=860,y=170)

    department_label = tk.Label(fifth_window, text="Enter your department", font=("bold", 14),bg="white")
    department_label.place(x=80, y=60)
    department_entry = tk.Entry(fifth_window, font=("bold", 14), width=25,bg="light blue")
    department_entry.place(x=280, y=60)

    def touch_button9(event):
        event.widget["background"]="green"
        event.widget["foreground"]="white"
 
    def exit_button9(event):
        event.widget["background"]="blue"
        event.widget["foreground"]="white"

    seevacancy_button=tk.Button(fifth_window,text="See Vacancy",bg="blue",fg="white",width=28,font=("bold",14),command=lambda:display_vacancy(department_entry))
    seevacancy_button.place(x=80,y=120)

    seevacancy_button.bind("<Enter>",touch_button9)
    seevacancy_button.bind("<Leave>",exit_button9)

    
    company_label = tk.Label(fifth_window, text="Company :", font=("bold", 14),bg="white")
    company_label.place(x=80, y=200)
       
    post_label = tk.Label(fifth_window, text="Post :", font=("bold", 14),bg="white")
    post_label.place(x=80, y=250)
      
    location_label = tk.Label(fifth_window, text="Location :", font=("bold", 14),bg="white")
    location_label.place(x=80, y=300)
       
    req_label = tk.Label(fifth_window, text="Basic Requirements :", font=("bold", 14),bg="white")
    req_label.place(x=80, y=350)
      
    cemail_label = tk.Label(fifth_window, text="Company Email Address :", font=("bold", 14),bg="white")
    cemail_label.place(x=80, y=400)

    duration_label = tk.Label(fifth_window, text="Duration :", font=("bold", 14),bg="white")
    duration_label.place(x=80, y=450)
       
    source_label = tk.Label(fifth_window, text="Source :", font=("bold", 14),bg="white")
    source_label.place(x=80, y=500)

    date_label= tk.Label(fifth_window, text="Updated Date and Time :", font=("bold", 14),bg="white")
    date_label.place(x=80, y=550)

    def touch_button10(event):
        event.widget["background"]="green"
        event.widget["foreground"]="white"
 
    def exit_button10(event):
        event.widget["background"]="blue"
        event.widget["foreground"]="white"

    pvacancy_button=tk.Button(fifth_window,text="Previous Vacancy",bg="blue",fg="white",width=28,font=("bold",14))
    pvacancy_button.place(x=80,y=620)
    pvacancy_button.bind("<Enter>",touch_button10)
    pvacancy_button.bind("<Leave>",exit_button10)


    def touch_button11(event):
        event.widget["background"]="green"
        event.widget["foreground"]="white"
 
    def exit_button11(event):
        event.widget["background"]="blue"
        event.widget["foreground"]="white"

    nvacancy_button=tk.Button(fifth_window,text="Next Vacancy",bg="blue",fg="white",width=28,font=("bold",14))
    nvacancy_button.place(x=450,y=620)

    nvacancy_button.bind("<Enter>",touch_button11)
    nvacancy_button.bind("<Leave>",exit_button11)


    def touch_button12(event):
        event.widget["background"]="black"
        event.widget["foreground"]="white"
 
    def exit_button12(event):
        event.widget["background"]="red"
        event.widget["foreground"]="white"

    back_button=tk.Button(fifth_window,text="Back",bg="red",fg="white",width=28,font=("bold",14),command=lambda:calling_infromation_window(fifth_window))
    back_button.place(x=820,y=620)
    back_button.bind("<Enter>",touch_button12)
    back_button.bind("<Leave>",exit_button12)


    def result_from_db(department):

        connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",  
        database="mydatabase")
    
        print("database connection successful2")

        query = connection.cursor()
        query.execute("SELECT company, post, location, req,email,duration, source,date FROM vacancy WHERE department = %s", (department,))
        db_result= query.fetchall()
        
        print(db_result)
        connection.close()
        return db_result

    def display_vacancy(department_entry):
        department=department_entry.get()
        print(2)

               
        if department=="":
            tk.messagebox.showerror("Error", "Please enter your department")
            return
        print(f"Department entered: {department}")
        vacancies=result_from_db(department)

        if vacancies:
            vacancy_index=0
            print(0)
        else:
            tk.messagebox.showerror("No Vacancies", "No Vacancies Available For This Department")    
           
        for i in vacancies:
            print(i)

        def show_vacancy(index):

            company_label.config(text=f"Company :   {vacancies[index][0]}")
            post_label.config(text=f"Post:    {vacancies[index][1]}")
            location_label.config(text=f"Location :    {vacancies[index][2]}")
            req_label.config(text=f"Basic Requirements :   {vacancies[index][3]}")
            cemail_label.config(text=f"Company Email Address :   {vacancies[index][4]}")
            duration_label.config(text=f"Duration :    {vacancies[index][5]}")
            source_label.config(text=f"Source :    {vacancies[index][6]}")
            date_label.config(text=f"Updated Date and Time :   {vacancies[index][7]}")

        def next_vacancy():

            nonlocal vacancy_index
            if vacancy_index < len(vacancies)-1:
                vacancy_index=vacancy_index+1
                show_vacancy(vacancy_index)

        def previous_vacancy():
            nonlocal vacancy_index
            if vacancy_index >0:
                vacancy_index=vacancy_index-1
                show_vacancy(vacancy_index)

        pvacancy_button.config(command=previous_vacancy)
        nvacancy_button.config(command=next_vacancy)

       
        show_vacancy(vacancy_index)    
  
   
    fifth_window.mainloop()

def check_update(forth_window):


    forth_window.destroy()

    connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",  
    database="mydatabase")

    query = connection.cursor()
    query.execute("SELECT position,name FROM user WHERE name = %s", (registered_username,))
    check_result= query.fetchall()
    print(check_result)

    if  check_result[0][0] != "student" and check_result[0][1][0] == "0": 
        update()
       

    else:
        tk.messagebox.showerror("User Not Allowed", " You are not allowed to update vacancies ") 
        query.close()
        connection.close() 
    
       
def update():

    global registered_username
    print("issue resoveled",registered_username)
    
    sixth_window=tk.Tk()
    sixth_window.title("Internshp Vacancy Finder")
    sixth_window.geometry("2000x2000")
    sixth_window.configure(bg="white")
    
    icon_image=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\lg.png")
    icon_photo=ImageTk.PhotoImage(icon_image)
    sixth_window.iconphoto(False,icon_photo)

    background_image4=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\software.png")
    background_image4=background_image4.resize((300,300),Image.Resampling.LANCZOS)
    background_photo4=ImageTk.PhotoImage(background_image4)
    label=tk.Label(sixth_window,image=background_photo4,bg="white")
    label.place(x=860,y=170)

    connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",  
    database="mydatabase")
    
    print("database connection successful3")
        
        
    cname_label = tk.Label(sixth_window, text="Company Name :", font=("bold", 12),bg="white")
    cname_label.place(x=100, y=60)
    companyname_entry = tk.Entry(sixth_window, font=("bold", 14), width=35,bg="light blue")
    companyname_entry.place(x=300, y=60)

    vacancy_label = tk.Label(sixth_window, text="Vacancy :", font=("bold", 12),bg="white")
    vacancy_label.place(x=100, y=120)
    vacancy_entry = tk.Entry(sixth_window, font=("bold", 14), width=35,bg="light blue")
    vacancy_entry.place(x=300, y=120)

    location_label = tk.Label(sixth_window, text="Location :", font=("bold", 12),bg="white")
    location_label.place(x=100, y=180)
    location_entry = tk.Entry(sixth_window, font=("bold", 14), width=35,bg="light blue")
    location_entry.place(x=300, y=180)

    breq_label = tk.Label(sixth_window, text="Basic Requirements :", font=("bold", 12),bg="white")
    breq_label.place(x=100, y=240)
    req_entry = tk.Entry(sixth_window, font=("bold", 14), width=35,bg="light blue")
    req_entry.place(x=300, y=240)

    cemail_label = tk.Label(sixth_window, text="Company Email :", font=("bold", 12),bg="white")
    cemail_label.place(x=100, y=300)
    email_entry = tk.Entry(sixth_window, font=("bold", 14), width=35,bg="light blue")
    email_entry.place(x=300, y=300)

    duration_label = tk.Label(sixth_window, text="Duration :", font=("bold", 12),bg="white")
    duration_label.place(x=100, y=360)
    duration_entry = tk.Entry(sixth_window, font=("bold", 14), width=35,bg="light blue")
    duration_entry.place(x=300, y=360)

    department_label = tk.Label(sixth_window, text="Depatment :", font=("bold", 12),bg="white")
    department_label.place(x=100, y=420)
    dep_entry = tk.Entry(sixth_window, font=("bold", 14), width=35,bg="light blue")
    dep_entry.place(x=300, y=420)


    def new_vacancy():

        query = connection.cursor()
        query.execute("SELECT name FROM user WHERE name = %s", (registered_username,))
        sresult= query.fetchone()
        print(sresult)

        comname=companyname_entry.get()
        post=vacancy_entry.get()
        location=location_entry.get()
        req=req_entry.get()
        email=email_entry.get()
        duration=duration_entry.get()
        department=dep_entry.get()
       
        print(f"updated companyname: {comname}")

        
        if  comname == "" or post == "" or location == "" or req == "" or email == "" or duration =="" or department == "" :
            tk.messagebox.showerror("Error", "All fields are required") 
            

        else:
            query = connection.cursor()
            query.execute("INSERT INTO vacancy (company,post,location,req,email,duration,source,department) VALUES (%s, %s,%s, %s,%s,%s,%s,%s)",
            (comname,post,location,req,email,duration,sresult,department))
            connection.commit()  
            print("update successfull")
            query.close()
            connection.close()
    
    update_button = tk.Button(sixth_window, text="Update", bg="green", fg="white", width=28, font=("bold", 14),command=new_vacancy)
    update_button.place(x=100, y=580)
    def touch_button(event):
        event.widget["background"]="blue"
        event.widget["foreground"]="white"
 
    def exit_button(event):
        event.widget["background"]="green"
        event.widget["foreground"]="white"

    update_button.bind("<Enter>",touch_button)
    update_button.bind("<Leave>",exit_button)


    back_button = tk.Button(sixth_window, text="Back", bg="blue", fg="white", width=28, font=("bold", 14), command=lambda:calling_infromation_window2(sixth_window))
    back_button.place(x=500, y=580) 
    def touch_button(event):
        event.widget["background"]="red"
        event.widget["foreground"]="white"
 
    def exit_button(event):
        event.widget["background"]="blue"
        event.widget["foreground"]="white"

    back_button.bind("<Enter>",touch_button)
    back_button.bind("<Leave>",exit_button)

    
    sixth_window.mainloop()

def aboutus(forth_window):

    forth_window.destroy()

    seventh_window=tk.Tk()
    seventh_window.title("Internshp Vacancy Finder")
    seventh_window.geometry("2000x2000")
    seventh_window.configure(bg="white")
    
    icon_image=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\lg.png")
    icon_photo=ImageTk.PhotoImage(icon_image)
    seventh_window.iconphoto(False,icon_photo)

    image=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\fb.webp")
    image=image.resize((80,80),Image.Resampling.LANCZOS)
    photo=ImageTk.PhotoImage(image)
    label=tk.Label(seventh_window,image=photo,bg="white")
    label.place(x=80,y=100)

    image1=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\whtspp.webp")
    image1=image1.resize((80,80),Image.Resampling.LANCZOS)
    photo1=ImageTk.PhotoImage(image1)
    label=tk.Label(seventh_window,image=photo1,bg="white")
    label.place(x=80,y=200)

    image2=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\phone.png")
    image2=image2.resize((80,80),Image.Resampling.LANCZOS)
    photo2=ImageTk.PhotoImage(image2)
    label=tk.Label(seventh_window,image=photo2,bg="white")
    label.place(x=80,y=300)

    image3=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\gmail.png")
    image3=image3.resize((80,80),Image.Resampling.LANCZOS)
    photo3=ImageTk.PhotoImage(image3)
    label=tk.Label(seventh_window,image=photo3,bg="white")
    label.place(x=80,y=400)
    
    fb_label=tk.Label(seventh_window,text="Kavindu Abeysinghe",font=(20),bg="white")
    fb_label.place(x=200,y=140)

    whatsapp_label=tk.Label(seventh_window,text="0761257338",font=(20),bg="white")
    whatsapp_label.place(x=200,y=240)

    tp_label=tk.Label(seventh_window,text="0761257339",font=(20),bg="white")
    tp_label.place(x=200,y=340)

    email_label=tk.Label(seventh_window,text="kavindudihara@gmail.com",font=(20),fg="blue",bg="white")
    email_label.place(x=200,y=440)
    
    image4=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\last.jpg")
    image4=image4.resize((600,450),Image.Resampling.LANCZOS)
    photo4=ImageTk.PhotoImage(image4)
    label=tk.Label(seventh_window,image=photo4,bg="white")
    label.place(x=600,y=80)       

    back_button = tk.Button(seventh_window, text="Back", bg="light blue", fg="black", width=28, font=("bold", 14),command=lambda:calling_infromation_window3(seventh_window))
    back_button.place(x=100, y=580)
    def touch_button(event):
        event.widget["background"]="red"
        event.widget["foreground"]="white"
 
    def exit_button(event):
        event.widget["background"]="light blue"
        event.widget["foreground"]="black"

    back_button.bind("<Enter>",touch_button)
    back_button.bind("<Leave>",exit_button)

    
    leave_button = tk.Button(seventh_window, text="Exit", bg="blue", fg="white", width=28, font=("bold", 14), command=seventh_window.destroy)
    leave_button.place(x=500, y=580)

    def touch_button(event):
        event.widget["background"]="red"
        event.widget["foreground"]="white"
 
    def exit_button(event):
        event.widget["background"]="blue"
        event.widget["foreground"]="white"

    leave_button.bind("<Enter>", touch_button) 
    leave_button.bind("<Leave>", exit_button) 

  
    seventh_window.mainloop()
    
    
def opening_window():

    first_window=tk.Tk()     
    first_window.title("Internshp Vacancy Finder")
    first_window.configure(bg="white")
    first_window.geometry("2000x2000")
    
    icon_image=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\lg.png")
    icon_photo=ImageTk.PhotoImage(icon_image)
    first_window.iconphoto(False,icon_photo)


    app_logo = icon_image.resize((290, 290), Image.Resampling.LANCZOS)
    app_logo_photo = ImageTk.PhotoImage(app_logo)
    label=tk.Label(first_window,image=app_logo_photo,bg="white")
    label.place(x=130,y=125)

    canvas=tk.Canvas(first_window,width=220,height=50,bg="#522C5D")
    canvas.place(x=90,y=500)
    canvas.create_text(100, 30, text="Find More", font=("Helvetica", 15, 'bold'), fill="white")

    canvas1=tk.Canvas(first_window,width=220,height=50,bg="#ffe3d8")
    canvas1.place(x=300,y=500)
    canvas1.create_text(110, 30, text="DISCOVER", font=("Helvetica", 15, 'bold'), fill="#522C5D")
   
    background_image=Image.open("C:\\Users\\iFix Technology\\Desktop\\Internship Vacancy Finder\\bgblue.jpg")
    background_image=background_image.resize((700, 700), Image.Resampling.LANCZOS)
    background_photo=ImageTk.PhotoImage(background_image)
    
    canvas2 = tk.Canvas(first_window, width=1500, height=900)
    canvas2.place(x=650,y=0)

    canvas2.create_image(0, 0, image=background_photo, anchor="nw")

    canvas2.create_text(150, 220, text="Welcome!", font=("Helvetica", 37, 'bold'), fill="white")

    canvas2.create_text (30,300,text="May Your Journey Lead You To Exciting Opprtunities And A Bright Future.Unlock Your Futuer ,Find The Perfect Internship !",
    font=("Helvetica",16),fill="white" ,width=650, anchor="nw") 

    canvas2.create_text (30,370,text="Unlock Your Futue ,Find The Perfect Internship!",
    font=("Helvetica",16),fill="white" ,width=650, anchor="nw") 
    
    canvas2.create_text (30,425,text="Log in to get started!!!",font=("Helvetica",18),fill="white" ,width=650, anchor="nw") 
 
    connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",  
    database="mydatabase")
    
    print("database connection successful for delt vacancy")

    query=connection.cursor()

    cutoff_date = datetime.now() - timedelta(days=30)
    query.execute("DELETE FROM vacancy WHERE date < %s", (cutoff_date,))
    connection.commit()
    connection.close()
 
    print("old record delete successfully")
      
    button=tk.Button(first_window,text="LOG IN",bg="light blue",font=("bold",14),width=21,command=lambda:login_window(first_window))
    button.place(x=980,y=500) 
     
    def touch_button(event):
        event.widget["background"]="#0096FF"
        event.widget["foreground"]="white"
 
    def exit_button(event):
        event.widget["background"]="light blue"
        event.widget["foreground"]="black"

    button.bind("<Enter>",touch_button)
    button.bind("<Leave>",exit_button)

    button1=tk.Button(first_window,text="EXIT",bg="light blue",font=("bold",14),width=21,command=first_window.destroy)
    button1.place(x=680,y=500) 
       
    def touch_button1(event):
        event.widget["background"]="red"
        event.widget["foreground"]="white"
 
    def exit_button1(event):
        event.widget["background"]="light blue"
        event.widget["foreground"]="black"

    button1.bind("<Enter>",touch_button1)
    
    button1.bind("<Leave>",exit_button1)
    
    first_window.mainloop()
           
opening_window()
