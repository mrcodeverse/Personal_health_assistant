import os 
import csv
import playsound
'''import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')      
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')   
engine.setProperty('rate', 200)'''
from gtts import gTTS
import sys
from matplotlib import pyplot as plt
import datetime
now=datetime.datetime.now()
import mysql.connector as m
con=m.connect(host="localhost",user="root",password="samirsahadipalisaha",database="health_assist")
db=con.cursor()
db.execute("use health_assist")
db.execute("create table if not exists signup(username varchar(20),password varchar(20));")
db.execute("create table if not exists physical_info(weight float ,age float,height float ,gender char (5));")
db.execute("create table if not exists walking_data(Date date,walking_speed float,walking_duration float,calories_burned float);")
num = 1
def assistant(output):
    global num 
  
    num += 1
    print("Alessa  : ", output) 
  
    toSpeak = gTTS(text = output, lang ='en-us', slow = False) 

    file = str(num)+".mp3"
    toSpeak.save(file) 
      
    
    playsound.playsound(file, True)  
    os.remove(file) 
def say_wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        assistant("Good Morning!  ")

    elif hour>=12 and hour<18:
        assistant("Good Afternoon! ")   

    else:
        assistant("Good Evening!  ")  

    assistant("I am Alessa Sir. your personal health assistant")       
def intro():

    

    print("""
                                        ██╗  ██╗██╗    ██╗     █████╗ ███╗   ███╗    ██╗   ██╗ ██████╗ ██╗   ██╗██████╗                                          
                                        ██║  ██║██║    ██║    ██╔══██╗████╗ ████║    ╚██╗ ██╔╝██╔═══██╗██║   ██║██╔══██╗                                         
                                        ███████║██║    ██║    ███████║██╔████╔██║     ╚████╔╝ ██║   ██║██║   ██║██████╔╝                                         
                                        ██╔══██║██║    ██║    ██╔══██║██║╚██╔╝██║      ╚██╔╝  ██║   ██║██║   ██║██╔══██╗                                         
                                        ██║  ██║██║    ██║    ██║  ██║██║ ╚═╝ ██║       ██║   ╚██████╔╝╚██████╔╝██║  ██║                                         
                                        ╚═╝  ╚═╝╚═╝    ╚═╝    ╚═╝  ╚═╝╚═╝     ╚═╝       ╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝                                         
                                                                                                                                                                 
                                        ██╗  ██╗███████╗ █████╗ ██╗  ████████╗██╗  ██╗     █████╗ ███████╗███████╗██╗███████╗████████╗ █████╗ ███╗   ██╗████████╗
                                        ██║  ██║██╔════╝██╔══██╗██║  ╚══██╔══╝██║  ██║    ██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║╚══██╔══╝
                                        ███████║█████╗  ███████║██║     ██║   ███████║    ███████║███████╗███████╗██║███████╗   ██║   ███████║██╔██╗ ██║   ██║   
                                        ██╔══██║██╔══╝  ██╔══██║██║     ██║   ██╔══██║    ██╔══██║╚════██║╚════██║██║╚════██║   ██║   ██╔══██║██║╚██╗██║   ██║   
                                        ██║  ██║███████╗██║  ██║███████╗██║   ██║  ██║    ██║  ██║███████║███████║██║███████║   ██║   ██║  ██║██║ ╚████║   ██║   
 
                                                                                                                                                                        """)
    '''engine.say("hi! i am your health assistance")
    engine.runAndWait()'''
    assistant("hi, i am your health assistance")
    

    print("""
                                     _          _ _ _     _           _                                                                      _                            
                                    (_)        (_) | |   | |         | |                                 _             _                    | |                           
                                     _    _ _ _ _| | |   | |__  _____| | ____     _   _  ___  _   _    _| |_ ___     _| |_  ____ _____  ____| |  _                        
                                    | |  | | | | | | |   |  _ \| ___ | ||  _ \   | | | |/ _ \| | | |  (_   _) _ \   (_   _)/ ___|____ |/ ___) |_/ )                       
                                    | |  | | | | | | |   | | | | ____| || |_| |  | |_| | |_| | |_| |    | || |_| |    | |_| |   / ___ ( (___|  _ (                        
                                    |_|   \___/|_|\_)_)  |_| |_|_____)\_)  __/    \__  |\___/|____/      \__)___/      \__)_|   \_____|\____)_| \_)                       
                                                                        |_|      (____/                                                                                   
                                                                      _                _             _                       _       _                                _   
                                                                     | |              (_)           | |                  _  (_)     (_)  _                           | |  
                                     _   _  ___  _   _  ____    ____ | |__  _   _  ___ _  ____ _____| |    _____  ____ _| |_ _ _   _ _ _| |_ _   _    _____ ____   __| |  
                                    | | | |/ _ \| | | |/ ___)  |  _ \|  _ \| | | |/___) |/ ___|____ | |   (____ |/ ___|_   _) | | | | (_   _) | | |  (____ |  _ \ / _  |  
                                    | |_| | |_| | |_| | |      | |_| | | | | |_| |___ | ( (___/ ___ | |   / ___ ( (___  | |_| |\ V /| | | |_| |_| |  / ___ | | | ( (_| |  
                                     \__  |\___/|____/|_|      |  __/|_| |_|\__  (___/|_|\____)_____|\_)  \_____|\____)  \__)_| \_/ |_|  \__)\__  |  \_____|_| |_|\____|  
                                    (____/                     |_|         (____/                                                           (____/                        
                                     _           _                                                             ___ _                                                      
                                    | |         | |                                      _                    / __|_)  _                                                  
                                    | |__  _____| | ____     _   _  ___  _   _     ___ _| |_ _____ _   _    _| |__ _ _| |_                                                
                                    |  _ \| ___ | ||  _ \   | | | |/ _ \| | | |   /___|_   _|____ | | | |  (_   __) (_   _)                                               
                                    | | | | ____| || |_| |  | |_| | |_| | |_| |  |___ | | |_/ ___ | |_| |    | |  | | | |_                                                
                                    |_| |_|_____)\_)  __/    \__  |\___/|____/   (___/   \__)_____|\__  |    |_|  |_|  \__)                                               
                                                   |_|      (____/                                (____/                                                                  
                                                                                                                                      
                                                                                                                                      """)
    '''engine.say("I will help you to track your physical activity and help you stay fit")
    engine.runAndWait()'''
    assistant("I will help you to track your physical activity and help you stay fit")
    '''engine.say("to know about my features press any key")
    engine.runAndWait()'''
    assistant("to know about my features press any key ")
    ch=input("""
                                            ___  __                __                __   __       ___                  ___  ___      ___       __   ___  __     
                                             |  /  \    |__/ |\ | /  \ |  |     /\  |__) /  \ |  |  |      |\/| \ /    |__  |__   /\   |  |  | |__) |__  /__`    
                                             |  \__/    |  \ | \| \__/ |/\|    /~~\ |__) \__/ \__/  |      |  |  |     |    |___ /~~\  |  \__/ |  \ |___ .__/    
                                                                                                                                                                 
                                             __   __   ___  __   __                            ___                                                               
                                            |__) |__) |__  /__` /__`     /\  |\ | \ /    |__/ |__  \ /                                                           
                                            |    |  \ |___ .__/ .__/    /~~\ | \|  |     |  \ |___  |                                                            
                                                                                                                         """)


    print("""
                              ___        ______        _          _                 _                                                                                                          
                             (___)      (____  \      (_)        | |               | |                                                                                                         
                                _        ____)  )____  _     ____| |__  _____  ____| |  _ _____  ____                                                                                          
                               | |      |  __  (|    \| |   / ___)  _ \| ___ |/ ___) |_/ ) ___ |/ ___)                                                                                         
                              _| |_ _   | |__)  ) | | | |  ( (___| | | | ____( (___|  _ (| ____| |                                                                                             
                             (_____|_)  |______/|_|_|_|_|   \____)_| |_|_____)\____)_| \_)_____)_|                                                                                             
                                                                                                   """)
    
    '''engine.say("first i can calculate your body mass index and tell you how much fit you are")
    engine.runAndWait()'''
    assistant("first i can calculate your body mass index and tell you how much fit you are ")

    print("""
    

                             ______       ______           _                            _                                                                                                      
                            (_____ \     (_____ \         | |           _              | |                                                                                                     
                              ____) )     _____) )____  __| | ___     _| |_  ____ _____| |  _ _____  ____                                                                                      
                             / ____/     |  ____/ ___ |/ _  |/ _ \   (_   _)/ ___|____ | |_/ ) ___ |/ ___)                                                                                     
                            | (_____ _   | |    | ____( (_| | |_| |    | |_| |   / ___ |  _ (| ____| |                                                                                         
                            |_______|_)  |_|    |_____)\____|\___/      \__)_|   \_____|_| \_)_____)_|
                                                                                                                 """)
    '''engine.say("second with help your walking data like distance you walked and walking duration")
    engine.runAndWait()'''
   
    assistant("second with the help of your walking data like distance you walked and walking duration i can calculate how much calories did you burn ")
    print("""
                                                                                                                                                                                               
                             ______      _______       _             _               _                       _                    _                                        _            _      
                            (_____ \    (_______)     | |           (_)             | |                     (_)                  | |        _                             | |          (_)     
                             _____) )    _       _____| | ___   ____ _ _____  ___   | |__  _   _  ____ ____  _ ____   ____     __| |_____ _| |_ _____    _____ ____  _____| |_   _  ___ _  ___ 
                            (_____ (    | |     (____ | |/ _ \ / ___) | ___ |/___)  |  _ \| | | |/ ___)  _ \| |  _ \ / _  |   / _  (____ (_   _|____ |  (____ |  _ \(____ | | | | |/___) |/___)
                             _____) )   | |_____/ ___ | | |_| | |   | | ____|___ |  | |_) ) |_| | |   | | | | | | | ( (_| |  ( (_| / ___ | | |_/ ___ |  / ___ | | | / ___ | | |_| |___ | |___ |
                            (______(_)   \______)_____|\_)___/|_|   |_|_____|___/   |____/|____/|_|   |_| |_|_|_| |_|\___ |   \____\_____|  \__)_____|  \_____|_| |_\_____|\_)__  (___/|_(___/ 
                                                                                                                    (_____|                                                 (____/             

                                                                                                                                                                                   """)
    '''engine.say("third i will store your calories burning data and plot a graph for you so that you can analyse your calories burning data")
    engine.runAndWait()'''
    assistant("third i will store your calories burning data and plot a graph for you so that you can analyse your calories burning data")
    print("\n1. IF YOU ARE A NEW USER PRESS 1 \n2. IF YOU ARE EXIXTING USER PRESS 2")
    while True :
        ch=int(input("ENTER YOUR CHOICE : "))
        if ch==1:
            print(phyc_data())
            break
        if ch==2:
            assistant("Do you want me to speak the menu, type y for yes and n for no ")
            me_choice=input("enter your choice : ")
            if me_choice=='n':
                assistant("ok sir")
                print(menu())
            if me_choice=='y':
                assistant("ok sir")
                print(speak_menu())
            break
            
        else:
            continue

def security():
    print(say_wish())
    print("""
                                                    >>>>>>>>>>>>>>>>>>>>>>>>>>>>------------------------------------------------<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                        This software is for physical activity tracking purpose , so we also keep you data privately accessible
                                                        to ensure enought security . we will ask you for log in details . initially you need to signup first
                                                    >>>>>>>>>>>>>>>>>>>>>>>>>>>>------------------------------------------------<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                                                                                            """)
   
   
    '''engine.say("This software is for physical activity tracking purpose , so we also keep you data privately accessible ,to ensure enought security , we will ask you for login details . initially you need to signup first")

    engine.runAndWait()'''
    assistant("This software is for physical activity tracking purpose , so we also keep you data privately accessible ,to ensure enought security , we will ask you for login details . initially you need to signup first")
    

    db.execute("create table if not exists signup(username varchar(20),password varchar(20))")

    while True:
        print("""
                                    +-------------------------------------------+
                                    |        Choose one option from below       |
                                    +-------------------------------------------+
                                    |                 1. Signup                 | 
                                    +-------------------------------------------+
                                    |                 2. Login                  |
                                    +-------------------------------------------+
                                                                                                        """)
        
        print("""
                           
                                  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.  .-----------------. .----------------. 
                                | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
                                | | _____  _____ | || |      __      | || |  _______     | || | ____  _____  | || |     _____    | || | ____  _____  | || |    ______    | |
                                | ||_   _||_   _|| || |     /  \     | || | |_   __ \    | || ||_   \|_   _| | || |    |_   _|   | || ||_   \|_   _| | || |  .' ___  |   | |
                                | |  | | /\ | |  | || |    / /\ \    | || |   | |__) |   | || |  |   \ | |   | || |      | |     | || |  |   \ | |   | || | / .'   \_|   | |
                                | |  | |/  \| |  | || |   / ____ \   | || |   |  __ /    | || |  | |\ \| |   | || |      | |     | || |  | |\ \| |   | || | | |    ____  | |
                                | |  |   /\   |  | || | _/ /    \ \_ | || |  _| |  \ \_  | || | _| |_\   |_  | || |     _| |_    | || | _| |_\   |_  | || | \ `.___]  _| | |
                                | |  |__/  \__|  | || ||____|  |____|| || | |____| |___| | || ||_____|\____| | || |    |_____|   | || ||_____|\____| | || |  `._____.'   | |
                                | |              | || |              | || |              | || |              | || |              | || |              | || |              | |
                                | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
                                 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
                           
                                                                                                                                                         """)
        assistant("Warning for privacy reasons i format every saved data from the databases when you are a existing user and  select signup again ,so that any other person cannot able to acces your data. Be careful while entering your choice  ")
        assistant("press 1 for signup, press 2 for login")
        ch=int(input("Signup/Login(1,2):"))


        if ch==1:
            db.execute("delete from signup;")
            db.execute("delete from physical_info;")
            db.execute("delete from walking_data ;")
            
            assistant("enter your username ")
            username=input("USERNAME:")
            assistant("enter your password")
            pw=input("PASSWORD:")
            db.execute("insert into signup values('"+username+"','"+pw+"')")
            con.commit()
            assistant("your login data has succesfully recorded ")
            


        elif ch==2:
            assistant("enter your username ")

            username=input("USERNAME:")

            db.execute("select username from signup where username='"+username+"'")
            pot=db.fetchone()

            if pot is not None:
                print("VALID USERNAME!!!!!!")
                assistant("enter your password")

                pw=input("PASSWORD:")

                db.execute("select password from signup where password='"+pw+"'")
                a=db.fetchone()

                if a is not None:
                    print("""
                            +++++++++++++++++++++++
                            +++LOGIN SUCCESSFULL+++
                            +++++++++++++++++++++++
                                                        """)
                    assistant("Login succesfull , good to see you back sir  ")


                    

                    
                    print(intro())
                    break
                else:
                    print("""
                            ++++++++++++++++++++++
                            ++INCORRECT PASSWORD++
                            ++++++++++++++++++++++
                                                        """)
                    assistant("incorrect password , access denied ")
                    
                    break


            else:
                print("""
                         ++++++++++++++++++++
                         ++INVALID USERNAME++
                         ++++++++++++++++++++
                                                """)
                assistant("incorrect username , access denied")
                
                break
        else:
            print("INVALID INPUT!")
            print(security())
   




def menu():
    assistant("please read the menu carefully and enter your choice")

    '''engine.say("please read the menu carefully and enter your choice")
    engine.runAndWait()'''
    print('''
                                    +----------------------------------------------------------+
                                    |        Choose one option from below                      |
                                    +----------------------------------------------------------+
                                    | 1. Check your bmi                                        | 
                                    +----------------------------------------------------------+
                                    | 2. Check how much calories did you burn during walking   |
                                    +----------------------------------------------------------+
                                    | 3. Take a look at your physical data                     | 
                                    +----------------------------------------------------------+
                                    | 4. Update your physical data                             | 
                                    +----------------------------------------------------------+
                                    | 5. Top 6 high calories burning cardio exercise or games  | 
                                    +----------------------------------------------------------+
                                    | 6. Take a look at your walking record                    | 
                                    +----------------------------------------------------------+
                                    | 7. Analyse your calories burning record                  |
                                    +----------------------------------------------------------+
                                    | 8. Exit                                                  |
                                    +----------------------------------------------------------+


                                                                                                                                ''')
    

    '''engine.say("press one to check your bmi , press two to calculate how much calories did you burn during walking , press three to take a look at your physical data press four to update your physical data, press five to get to know about high calorie burning cardio exercises ,press six take a look at walking record,press seven to visualise your calories burning record ,press 8 to exit ")
    engine.runAndWait()'''
    choi=int(input("enter your choice (1/2/3/4/5/6/7/8) : "))
    if choi==1:
        print(BMI_checker())
    if choi==2:
        print(pedo_tracker())
    if choi==3:
        print(see())
    if choi==4:
        print(up_data())
    if choi==5:
        print(work())
    if choi==6:
        print(see_walk())
    if choi==8:
        print(connect_termination())
    if choi==7:
        print(visualise())
    if choi==8:
        print(connect_termination())
def speak_menu():
    assistant("I am reading  the menu please lisen carefully and enter your choice")

    '''engine.say("please read the menu carefully and enter your choice")
    engine.runAndWait()'''
    print('''
                                    +----------------------------------------------------------+
                                    |        Choose one option from below                      |
                                    +----------------------------------------------------------+
                                    | 1. Check your bmi                                        | 
                                    +----------------------------------------------------------+
                                    | 2. Check how much calories did you burn during walking   |
                                    +----------------------------------------------------------+
                                    | 3. Take a look at your physical data                     | 
                                    +----------------------------------------------------------+
                                    | 4. Update your physical data                             | 
                                    +----------------------------------------------------------+
                                    | 5. Top 6 high calories burning cardio exercise or games  | 
                                    +----------------------------------------------------------+
                                    | 6. Take a look at your walking record                    | 
                                    +----------------------------------------------------------+
                                    | 7. Analyse your calories burning record                  |
                                    +----------------------------------------------------------+
                                    | 8.analyse your calories burning record                   |
                                    +----------------------------------------------------------+


                                                                                                                                ''')
    

    '''engine.say("press one to check your bmi , press two to calculate how much calories did you burn during walking , press three to take a look at your physical data press four to update your physical data, press five to get to know about high calorie burning cardio exercises ,press six take a look at walking record,press seven to visualise your calories burning record ,press 8 to exit ")

    engine.runAndWait()'''
    assistant("press one to check your bmi , press two to calculate how much calories did you burn during walking , press three to take a look at your physical data press four to update your physical data, press five to get to know about high calorie burning cardio exercises ,press six take a look at walking record , press seven to visualise your calories burning record , press 8 to exit ")

    choi=int(input("enter your choice (1/2/3/4/5/6/7/8) : "))
    if choi==1:
        print(BMI_checker())
    if choi==2:
        print(pedo_tracker())
    if choi==3:
        print(see())
    if choi==4:
        print(up_data())
    if choi==5:
        print(work())
    if choi==6:
        print(see_walk())
    if choi==8:
        print(connect_termination())
    if choi==7:
        print(visualise())
    if choi==8:
        print(connect_termination())

        
    

def phyc_data():
    db.execute("delete from physical_info")
    assistant("please enter your physical data carefully it will be used for further calulations ")
    '''engine.say("please enter your physical data carefully it will be used for further calulations ")
    engine.runAndWait()'''
    assistant("please enter your weight in kg")
    wgt=float(input("please enter your weight in kg(s) : "))
    assistant("enter your age")
    age=int(input(" enter your age : "))
    assistant("enter your height in cm : ")
    hgt=float(input("enter your height in cm : "))
    assistant("Please enter your gender")
    gen=input("please enter your gender (m/f) :")
    insert_data=(
    "INSERT INTO physical_info(weight,age,height,gender)"
    "VALUES (%s,%s,%s,%s)"
    )
    data=(wgt,age,hgt,gen)
    try:


        db.execute(insert_data,data)
        con.commit()
        print("""YOUR DATA HAS BEEN INSERTED :)
              """)
        assistant("your data has succesfully recorded")
        '''engine.say("your data has succesfully inserted")
        engine.runAndWait()'''
    except:
        db.roolback()
    print(see())
    assistant("Do you want me to speak the menu, type y for yes and n for no ")
    menu_choice=input("enter your choice")
    if menu_choice=='n':
        assistant("ok sir")
        print(menu())
    if menu_choice=='y':
        assistant("ok sir")
        print(speak_menu())
    

            



def connect_termination():
    print("Bye bye sir have a nice day ")
    assistant("Bye bye sir have a nice day")
    sys.exit()


def BMI_checker():
    print("CALCULATING YOUR BODY MASS INDEX........")
    assistant("calculating your body mass index")
    '''engine.say(" calculating your body mass index........")
    engine.runAndWait()'''        
    db.execute("use health_assist")
    s=("select weight from physical_info;")
    db.execute(s)

    data=db.fetchall()
    wei=data[0][0]
    print(wei)
    l=("select height from physical_info;")
    db.execute(l)
    data=db.fetchall()
    hei=data[0][0]
    cov=hei*1/100
    print(cov)
    bmi=wei/(cov**2)
    
    print("Your BMI is: {0} and you are: ".format(bmi), end='')

    #conditions
    if ( bmi < 16):
       print("severely underweight")
       assistant(" you are severely underweigth")

    elif ( bmi >= 16 and bmi < 18.5):
       print("underweight")
       assistant("you are underweight")

    elif ( bmi >= 18.5 and bmi < 25):
       print("Healthy")
       assistant("bingo! you are healthy")

    elif ( bmi >= 25 and bmi < 30):
       print("overweight")
       assistant("you are overweight ")

    elif ( bmi >=30):
        print("severely overweight")
        assistant("you are severely overweight")
    
        '''engine.say("bad news you are obesed and there is high chances of heart attack , hypertension you should start regular workout to recover your health")
        engine.runAndWait()'''
    assistant("Do you want me to speak the menu  type y for yes and n for no ")
    me_choice=input("enter your choice")
    if me_choice=='n':
        assistant("ok sir")
        print(menu())
    if me_choice=='y':
        assistant("ok sir")
        print(speak_menu())


    
    
def pedo_tracker():



    print("""
                                 (                     (                   (        )     (        )     *                            (        )   (    (         (     
                                 )\ )        *   )  (  )\ )     (          )\ )  ( /(     )\ )  ( /(   (  `              (     (      )\ )  ( /(   )\ ) )\ )      )\ )  
                                (()/(  (   ` )  /(  )\(()/(   ( )\     (  (()/(  )\())   (()/(  )\())  )\))(   (         )\    )\    (()/(  )\()) (()/((()/( (   (()/(  
                                 /(_)) )\   ( )(_))((_)/(_))  )((_)    )\  /(_))((_)\     /(_))((_)\  ((_)()\  )\      (((_)((((_)(   /(_))((_)\   /(_))/(_)))\   /(_)) 
                                (_))  ((_) (_(_())    (_))   ((_)_  _ ((_)(_))   _((_)   (_))    ((_) (_()((_)((_)     )\___ )\ _ )\ (_))    ((_) (_)) (_)) ((_) (_))   
                                | |   | __||_   _|    / __|   | _ )| | | || _ \ | \| |   / __|  / _ \ |  \/  || __|   ((/ __|(_)_\(_)| |    / _ \ | _ \|_ _|| __|/ __|  
                                | |__ | _|   | |      \__ \   | _ \| |_| ||   / | .` |   \__ \ | (_) || |\/| || _|     | (__  / _ \  | |__ | (_) ||   / | | | _| \__ \  
                                |____||___|  |_|      |___/   |___/ \___/ |_|_\ |_|\_|   |___/  \___/ |_|  |_||___|     \___|/_/ \_\ |____| \___/ |_|_\|___||___||___/  """)
                                                                                                                                        



    print("""
                                   _                                  _                                           _       _                                __       _ _        
                             _ __ | | ___  __ _ ___  ___    ___ _ __ | |_ ___ _ __   _   _  ___  _   _ _ __    __| | __ _| |_ __ _    ___ __ _ _ __ ___   / _|_   _| | |_   _  
                            | '_ \| |/ _ \/ _` / __|/ _ \  / _ \ '_ \| __/ _ \ '__| | | | |/ _ \| | | | '__|  / _` |/ _` | __/ _` |  / __/ _` | '__/ _ \ | |_| | | | | | | | | 
                            | |_) | |  __/ (_| \__ \  __/ |  __/ | | | ||  __/ |    | |_| | (_) | |_| | |    | (_| | (_| | || (_| | | (_| (_| | | |  __/ |  _| |_| | | | |_| | 
                            | .__/|_|\___|\__,_|___/\___|  \___|_| |_|\__\___|_|     \__, |\___/ \__,_|_|     \__,_|\__,_|\__\__,_|  \___\__,_|_|  \___| |_|  \__,_|_|_|\__, | 
                            |_|                                                      |___/                                                                              |___/  

                                                                                                                                                                                            """)
   

    print("""
                                                                ****************************************************************
                                                                                FIRST LET US CALCULATE YOUR BMR
                                                                ****************************************************************""")
    '''engine.say("first let us calculate your bmr ")
    engine.runAndWait()'''
    assistant("first let us calculate your bmr ")
    print("""
                                      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ABOUT BMR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                        Basal metabolic rate is the number of calories your body needs to accomplish its most basic (basal) life-sustaining functions.
                                      >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<""")
    '''engine.say("bmr is basal metabolic rate is the number of calories your body needs to accomplish its most basic life-sustaining functions.")
    engine.runAndWait()'''
    assistant("bmr is basal metabolic rate is the number of calories your body needs to accomplish its most basic (basal) life-sustaining functions.")

    assistant("fetching your data from databases ")


    try:
        db.execute("use health_assist")
        s=("select weight from physical_info;")
        db.execute(s)
        w_data=db.fetchall()
        w=w_data[0][0]
        l=("select height from physical_info;")
        db.execute(l)
        h_data=db.fetchall()
        h=h_data[0][0] 
        k=("select age from physical_info;")
        db.execute(k)
        a_data=db.fetchall()
        a=a_data[0][0]
        z=("select gender from physical_info;")
        db.execute(z)
        g_data=db.fetchall()
        g=g_data[0][0]
        
        if g=="m":
            bmr=66.47+(13.75*w)+(5.003*h)-(6.755*a)
                
            """**********************************************"""

            print("Your bmr is  : ",bmr)
        if g=="f":
            bmr=655.1+(9.563*w)+(1.85*h)-(4.676*a)
            
            """**********************************************"""

            print("Your bmr is  : ",bmr)
    
        '''engine.say("enter your walking speed")
        engine.runAndWait()'''
        assistant("enter your walking speed in kilometer per hour")
        
    
           
        speed=float(input("Enter your walking speed (km/h) : "))
    
        a=3.2
        b=4.0
        c=4.8
        d=5.6
        e=6.4
        f=7.2
        g=8.0
        if speed<=a:
            mets=2.0
        if speed==a:
            mets=2.8
        if speed==b:
            mets=3.0
        if speed==c:
            mets=3.5
        if speed==d:
            mets=4.3
        if speed==e:
            mets=5.0
        if speed==f:
            mets=7.0
        if speed==g:
            mets=8.3

        
        '''engine.say("enter your walking duration in hour")
        engine.runAndWait()'''
        assistant("enter your walking duration in hour")


        dur=int(input(" Enter your walking duration (in hour): "))
        print("""
                                                     >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                                 NOW CALCULATING HOW MUCH CALORIES DID YOU BURN!.......
                                                     <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                                                      """)
        '''engine.say("now calculating how much calories you burn")
        engine.runAndWait()'''
        assistant("calculating how much calories you burn")
        cal=bmr*mets/24*dur
        print("""
                                                    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                                                         CONGRAGULATION YOU BURN A TOTAL OF : """,cal,"calories","""
                                                    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                                                                                                                     """)

        
        print("KEEP IT UP ;) ")   
        data_in=int(input("DO YOU WANT TO INSERT YOUR WALKING DATA (YES-TYPE 1 , NO TYPE-2 ) : "))
        if data_in==1:
            print('''             DATA WILL BE INSERTED ARE AS FOLLOWS
                                                                                ''')
            print('''
                                  DATA INSERTION DATE :''',now
                                                                                )
            print('''
                                  WALKING SPEED : ''',speed
                                                                    )
            print('''
                                  WALKING DURATION :''',dur
                                                                        )
            print('''
                                  CALORIES BURNED :''',cal
                                                                        )
            '''engine.say("proccesing your data insertion request......")
            engine.runAndWait()'''
            assistant("Proccesing your data insertion request")
            sql="INSERT INTO walking_data(Date , walking_speed , walking_duration , calories_burned) values(%s,%s,%s,%s)"
            val=(now,speed,dur,cal)
            db.execute(sql,val)
            con.commit()
            print('''
                                  Your data has succesfully recorded!
                                                                                            ''')
            '''engine.say("data insertion succesfully compleated")
            engine.runAndWait()'''
            assistant("Your data has succesfully recorded!")
    except:
        print("""
                            ------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!----------------
                                              PLEASE STORE YOUR PHYSICAL DATA FIRST, WE CALUCULATE THINGS THROUGHT YOUR STORED DATA
                            ------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!----------------
                                                                                                                                                         """)
        '''engine.say("warning please store your physical data first , we calculate things throught your stored data")
        engine.runAndWait()'''
        assistant("warning please store your physical data first , we calculate things throught your stored data")
        
        print(phyc_data())

    
    assistant("Do you want me to speak out the menu , type y for yes and n for no ")
    me_choice=input("enter your choice")
    if me_choice=='n':
        assistant("ok sir")
        print(menu())
    if me_choice=='y':
        assistant("ok sir")
        print(speak_menu())


    
    
def up_data():    
    db.execute("delete from physical_info;")    
    print("Previous data deleted")
    wgt=float(input("please enter your weight in kg(s) : "))
    age=int(input(" enter your age : "))
    hgt=float(input("enter your height in cm : "))
    gen=input("please enter your gender (M/F/others) :")
    insert_data=(
    "INSERT INTO physical_info(weight,age,height,gender)"
    "VALUES (%s,%s,%s,%s)"
    )
    data=(wgt,age,hgt,gen)
    try:


        db.execute(insert_data,data)
        con.commit()
        print("""   
                        YOUR DATA HAS BEEN INSERTED :)
                                                            """)
    except:
        con.roolback()
    
    assistant("Do you want me to speak out the menu , type y for yes and n for no ")
    me_choice=input("enter your choice")
    if me_choice=='n':
        assistant("ok sir")
        print(menu())
    if me_choice=='y':
        assistant("ok sir")
        print(speak_menu())


def visualise():
    print("""
                              VISUALISING YOUR DATA..........
                                                                                """)
    assistant("visualising your data")
    com=("select Date,calories_burned from walking_data;")
    db.execute(com)
    data=db.fetchall()
    row1=[]
    row2=[]

    for row in data:
        row1.append(row[0])
        row2.append(row[1])
    plt.xlabel('Date')  
# naming the y axis  
    plt.ylabel('Calories burned')  
    
# giving a title to my graph  
    plt.title('Calories burning record')  
    plt.plot(row1,row2,'-')
    plt.show()
    assistant("Do you want me to speak out the menu , type y for yes and n for no ")
    me_choice=input("enter your choice")
    if me_choice=='n':
        assistant("ok sir")
        print(menu())
    if me_choice=='y':
        assistant("ok sir")
        print(speak_menu())

        
    
            
def see():
    show_t_data="select*from physical_info"
    db.execute(show_t_data)
    records=db.fetchall()
    
    print("\nprinting the record")
    for row in records:
        print("WEIGHT = ",row[0],)
        print("---------------------------")
        print("AGE = ",row[1],)
        print("---------------------------")              
        print("HEIGHT = ",row[2],)
        print("---------------------------")
        print("GENDER = ",row[3],)
        print("---------------------------")

    
    assistant("Do you want me to speak out the menu , type y for yes and n for no ")
    me_choice=input("enter your choice")
    if me_choice=='n':
        assistant("ok sir")
        print(menu())
    if me_choice=='y':
        assistant("ok sir")
        print(speak_menu())


def see_walk():
    show_w_data="select*from walking_data"
    db.execute(show_w_data)
    rec=db.fetchall()
    print("total no of data in database : ",db.rowcount)
    print("\nprinting the record")
    for row in rec:
        print("DATE = ",row[0],)
        
        print("""---------------------------""")
        
        print("WALKING SPEED = ",row[1],)
        
        print("---------------------------")        
        
        print("WALKING DURATION = ",row[2],)
        
        print("---------------------------")
        
        print("CALORIES BURNED = ",row[3],)
        
        print("---------------------------")

    
    assistant("Do you want me to speak out the menu , type y for yes and n for no ")
    me_choice=input("enter your choice")
    if me_choice=='n':
        assistant("ok sir")
        print(menu())
    if me_choice=='y':
        assistant("ok sir")
        print(speak_menu())


    
    



def work():     
    f=open("workout.csv","w")
    w=csv.writer(f)    
    l=['Workout name','Calories burned per hour']
    s=['RUNNING', '755 CALORIES/HOUR']
    run=['RUNNING UP STAIRS', '819 CALORIES/HOUR']
    swim=['VIGOUROUS SWIMMING', '892 CALORIES/HOUR']
    soc=['SOCCER', '937 CALORIES/HOUR']
    jump=['JUMP ROPE', '1074 CALORIES/HOUR']
    w.writerow(l)
    w.writerow(s)
    w.writerow(run)
    w.writerow(swim)
    w.writerow(soc)
    w.writerow(jump)
    f.close()
    f=open("workout.csv","r")
    airw=csv.reader(f)
    for i in airw:
        print(i)
    f.close()
    
    assistant("Do you want me to speak out the menu , type y for yes and n for no ")
    me_choice=input("enter your choice")
    if me_choice=='n':
        assistant("ok sir")
        print(menu())
    if me_choice=='y':
        assistant("ok sir")
        print(speak_menu())



        
    


print(security())



